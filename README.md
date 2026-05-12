# 🎮 Epic Free Games Mail Bot

Bot Python permettant de récupérer automatiquement les jeux gratuits du moment sur l'Epic Games Store via PC Gamer puis d'envoyer un mail récapitulatif chaque semaine grâce à GitHub Actions.

Le script fonctionne entièrement dans le cloud via GitHub Actions, donc :

- ✅ pas besoin de laisser son PC allumé
- ✅ exécution automatique chaque semaine
- ✅ gratuit
- ✅ simple à configurer

---

# 📦 Fonctionnalités

- Scraping automatique des jeux gratuits Epic Games
- Envoi automatique d'un email
- Exécution hebdomadaire via GitHub Actions
- Compatible Gmail
- Déclenchement manuel possible depuis GitHub

---

# 📁 Structure du projet

```text
.
├── .github/
│   └── workflows/
│       └── epic_free_games.yml
│
├── main.py
├── requirements.txt
└── README.md


🚀 Installation
1. Cloner le projet
git clone https://github.com/VOTRE_REPO.git
cd VOTRE_REPO
📧 Configuration Gmail

Le projet utilise Gmail SMTP pour envoyer les emails.

⚠️ Le mot de passe Gmail classique ne fonctionne pas.

Il faut créer un mot de passe d'application Google.

Créer un mot de passe d'application
(Pour avoir accès aux mots de passe d'application il faut que faut que le compte ait l'authentification à deux facteurs activée)

Ouvrir :

https://myaccount.google.com/apppasswords

Puis :

Donner un nom au mot de passe d'application
Copier le mot de passe généré

Exemple :
abcd efgh ijkl mnop

🔐 Configuration des secrets GitHub

Dans le dépôt GitHub :

Settings
→ Secrets and variables
→ Actions
→ New repository secret

Créer les 3 secrets suivants :

EMAIL_SENDER
Adresse Gmail utilisée pour envoyer les mails.

Exemple :
monadresse@gmail.com

EMAIL_PASSWORD
Mot de passe d'application Google.

Exemple :
abcd efgh ijkl mnop

EMAIL_RECEIVER
Adresse email qui recevra les notifications.

Exemple :
destinataire@gmail.com

▶️ Lancer le workflow manuellement

Dans GitHub :

Actions
→ Epic Free Games
→ Run workflow

Le mail sera envoyé immédiatement.

⏰ Exécution automatique

Le workflow est configuré pour s'exécuter automatiquement chaque jeudi.

Configuration actuelle :

schedule:
  - cron: '0 18 * * 4'

⚠️ GitHub Actions utilise le fuseau UTC.

🕒 Modifier l'heure d'exécution

Modifier dans :

.github/workflows/epic_free_games.yml

Exemples :

Heure	Cron
Jeudi 18h	0 18 * * 4
Jeudi 20h	0 20 * * 4
Tous les jours 9h	0 9 * * *

🧪 Test local

Installer les dépendances :

pip install -r requirements.txt

Puis définir les variables d'environnement :

Windows PowerShell
$env:EMAIL_SENDER="monadresse@gmail.com"
$env:EMAIL_PASSWORD="mot_de_passe"
$env:EMAIL_RECEIVER="destinataire@gmail.com"
Linux / macOS
export EMAIL_SENDER="monadresse@gmail.com"
export EMAIL_PASSWORD="mot_de_passe"
export EMAIL_RECEIVER="destinataire@gmail.com"

Puis lancer :

python main.py

📬 Exemple de mail reçu :

🎮 Jeux gratuits Epic Games
1. Arranger: A Role-Puzzling Adventure
2. Trash Goblin

🛠 Dépendances
Python 3.11+
requests
beautifulsoup4

📄 Licence
MIT
