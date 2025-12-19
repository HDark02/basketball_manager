
---

# Basketball Manager

Ce projet est une application de gestion de joueurs de basket, développée avec Kivy et KivyMD. L'application permet de gérer les informations des joueurs, leurs compétences et de visualiser un classement basé sur leurs compétences.

## Fonctionnalités principales :

* **Gestion des joueurs** : Ajouter, modifier et supprimer des joueurs.
* **Classement** : Calculer et afficher un classement des joueurs en fonction de leurs compétences (tir, défense, passe, dribble).
* **Authentification** : Un système de connexion pour un utilisateur admin. L'authentification est gérée via un fichier JSON.
* **Personnalisation** : Les utilisateurs peuvent ajouter une image de profil pour chaque joueur.

## Installation

### Prérequis

Avant de pouvoir exécuter l'application, assurez-vous d'avoir Python et les bibliothèques suivantes installées sur votre machine :

* [Kivy](https://kivy.org/#home)
* [KivyMD](https://kivymd.readthedocs.io/en/latest/)
* [Plyer](https://plyer.readthedocs.io/en/latest/)

Vous pouvez installer ces bibliothèques avec pip :

```bash
pip install kivy kivymd plyer
```

### Cloner le projet

Vous pouvez cloner ce projet sur votre machine en utilisant Git :

```bash
git clone https://github.com/HDark02/Basketball-Manager.git
cd Basketball-Manager
```

## Usage

1. Exécutez le fichier principal du projet :

```bash
python main.py
```

2. L'application s'ouvrira avec une interface de connexion. Si vous n'avez pas encore de compte, vous pouvez vous inscrire.
3. Après vous être connecté, vous pouvez ajouter des joueurs, voir leur classement et plus encore.

## Structure du projet

Le projet est structuré comme suit :

* `main.py`: Le fichier principal contenant la logique de l'application.
* `welcome.kv`, `login.kv`, `sign_up.kv`, `home.kv`, `print_lab.kv`, `add.kv`, `parameter.kv`: Fichiers KV qui définissent l'interface utilisateur de l'application.
* `user_data.json`: Contient les informations d'utilisateur (nom, email, etc.).
* `joueurs.json`: Contient les données des joueurs (nom, compétences, image de profil).

## Fonctionnalités détaillées

* **Connexion/Inscription** : L'utilisateur peut se connecter avec un nom d'utilisateur et un mot de passe. Si l'utilisateur n'a pas de compte, il peut s'inscrire avec un nouveau nom, email et mot de passe.
* **Gestion des joueurs** : Les joueurs peuvent être ajoutés, modifiés ou supprimés. Chaque joueur a des compétences qui affectent son classement général.
* **Classement des joueurs** : Les joueurs sont classés en fonction de leurs compétences cumulées (tir, défense, passe, dribble).
* **Gestion des images de profil** : Les utilisateurs peuvent ajouter des images pour chaque joueur via un gestionnaire de fichiers intégré.

## Capture d'écran

![Exemple d'écran de l'application](screenshots/example.png)  <!-- Ajoute un lien vers une capture d'écran si tu en as -->

## Contributions

Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer le projet, n'hésitez pas à soumettre une pull request ou à ouvrir un issue.

## Auteurs

* **HDark02** (Développeur principal)

## Licence

Ce projet est sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---
