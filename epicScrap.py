import requests
from bs4 import BeautifulSoup
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

URL = "https://www.pcgamer.com/epic-games-store-free-games-list/"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_SENDER = os.environ["EMAIL_SENDER"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_RECEIVER = os.environ["EMAIL_RECEIVER"]

# =====================================================
# SCRAPING
# =====================================================

def get_free_games():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    games = []

    paragraphs = soup.find_all(["p", "h2", "h3"])

    for p in paragraphs:

        text = p.get_text(strip=True)

        if "Free to keep" in text and "|" in text:

            title = text.split("|")[0].strip()

            if 2 < len(title) < 100:
                games.append(title)

    # suppression doublons
    games = list(dict.fromkeys(games))

    return games[:2]

# =====================================================
# EMAIL
# =====================================================

def send_email(games):

    if games:

        games_text = "\n".join(
            [f"{i+1}. {game}" for i, game in enumerate(games)]
        )

    else:
        games_text = "Aucun jeu trouvé."

    body = f"""
Bonjour,

Voici les jeux gratuits Epic Games de cette semaine :

{games_text}

Epic Games :
https://store.epicgames.com/fr/free-games

Date :
{datetime.now().strftime("%d/%m/%Y %H:%M")}
"""

    msg = MIMEMultipart()

    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = "🎮 Jeux gratuits Epic Games"

    msg.attach(MIMEText(body, "plain", "utf-8"))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    server.starttls()

    server.login(EMAIL_SENDER, EMAIL_PASSWORD)

    server.send_message(msg)

    server.quit()

    print("Mail envoyé.")

# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    try:

        games = get_free_games()

        print("Jeux trouvés :")

        if games:
            for game in games:
                print("-", game)
        else:
            print("Aucun jeu trouvé.")

        send_email(games)

    except Exception as e:
        print("Erreur :", e)
        raise