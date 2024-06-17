# FakeLauncher

---

![License](https://img.shields.io/github/license/Redstoneur/FakeLauncher)
![Top Language](https://img.shields.io/github/languages/top/Redstoneur/FakeLauncher)
![Python Version](https://img.shields.io/badge/python-3.8-blue)
![Size](https://img.shields.io/github/repo-size/Redstoneur/FakeLauncher)
![Contributors](https://img.shields.io/github/contributors/Redstoneur/FakeLauncher)
![Last Commit](https://img.shields.io/github/last-commit/Redstoneur/FakeLauncher)
![Issues](https://img.shields.io/github/issues/Redstoneur/FakeLauncher)
![Pull Requests](https://img.shields.io/github/issues-pr/Redstoneur/FakeLauncher)

---

![Forks](https://img.shields.io/github/forks/Redstoneur/FakeLauncher)
![Stars](https://img.shields.io/github/stars/Redstoneur/FakeLauncher)
![Watchers](https://img.shields.io/github/watchers/Redstoneur/FakeLauncher)

---

![Latest Release](https://img.shields.io/github/v/release/Redstoneur/FakeLauncher)
![Release Date](https://img.shields.io/github/release-date/Redstoneur/FakeLauncher)

---

## Description

FakeLauncher est une application Python qui permet de lancer des jeux à partir d'une interface utilisateur. Les jeux et
leurs commandes de lancement sont stockés dans un fichier CSV.

## Installation

1. Assurez-vous d'avoir Python installé sur votre machine.
2. Clonez ce dépôt sur votre machine locale.

   ```bash
   git clone https://github.com/Redstoneur/FakeLauncher.git FakeLauncher
   cd FakeLauncher
   ```

3. Installez les dépendances du projet en exécutant la commande suivante dans le répertoire du projet :

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Exécutez le fichier `main.py` pour lancer l'application.

   ```bash
   python main.py
   ```

## Utilisation

1. Renseigner les jeux et leurs commandes de lancement dans le fichier `games.csv` en respectant le format suivant :

   ```csv
   "name","lunch_command"
   "nom_du_jeu","commande_de_lancement"
   ```

    - `nom_du_jeu` : Remplacez cela par le nom du jeu que vous souhaitez ajouter.
    - `commande_de_lancement` : Remplacez cela par la commande nécessaire pour lancer le jeu. Si la commande contient
      plusieurs parties (par exemple, un chemin d'accès et des arguments), séparez-les par un `#`.

   Par exemple, si vous voulez ajouter un jeu qui se lance avec la commande `dir C:`, vous ajouterez la ligne suivante :

   ```csv
   "dir","dir#C:"
   ```

   Notez que le fichier `games.csv` doit être dans le même répertoire que le fichier `main.py`

2. Lancez l'application.
3. Dans la zone de recherche, tapez le nom du jeu que vous souhaitez lancer.
4. Sélectionnez le jeu dans la liste des résultats.
5. Cliquez sur le bouton "Launch" pour lancer le jeu.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.