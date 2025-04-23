# 📧 BULLETPROOF EMAIL SENDER v3.4 (FINAL)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![SMTP](https://img.shields.io/badge/SMTP-Gmail-success)
![Status](https://img.shields.io/badge/Version-3.4-final-green)

> Script Python sécurisé pour l’envoi automatique d’e-mails en masse, idéal pour des candidatures de stage ou de travail. Envoie des e-mails personnalisés avec pièces jointes à plusieurs destinataires via SMTP Gmail.

---

## 🧩 Fonctionnalités

- 🔐 Connexion sécurisée au serveur SMTP (Gmail)
- 📄 Envoi d’un fichier PDF en pièce jointe
- 📨 Corps de mail et objet aléatoires
- ⏲️ Délai aléatoire entre les envois
- ♻️ Relance automatique en cas d’échec (3 tentatives)
- 🧵 Envoi par batch (8 emails) avec pause entre chaque lot

---

## 🛠️ Configuration

Avant d'exécuter le script, modifiez les valeurs suivantes dans le code :
- `SENDER_EMAIL` → Adresse email de l'expéditeur
- `APP_PASSWORD` → Mot de passe d’application Gmail (🔒 NE PAS METTRE EN CLAIR DANS GITHUB)
- `CV_PATH` → Chemin vers le CV en PDF

## 🚀 Installation & Exécution

1. **Cloner le projet**
   ```bash
   git clone https://github.com/HamzaBraik01/automated-email-deployer.git
   cd automated-email-deployer

