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

FakeLauncher is a Python application that allows you to launch games from a user interface. The games and their launch commands are stored in a CSV file.

## Installation

1. Make sure you have Python installed on your computer.
2. Clone this repository to your local computer.

   ```bash
   git clone https://github.com/Redstoneur/FakeLauncher.git FakeLauncher
   cd FakeLauncher
   ```

3. Install the project dependencies by running the following command in the project directory:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the `main.py` file to launch the application.

   ```bash
   python main.py
   ```

## Usage

1. Fill in the games and their launch commands in the `games.csv` file using the following format:

   ```csv
   "name","lunch_command"
   "game_name","game_lunch_command"
   ```

    - `game_name`: Replace this with the name of the game you want to add.
    - `game_lunch_command`: Replace this with the command needed to launch the game. If the command has multiple parts (e.g., a path and arguments), separate them with a `#`.

   For example, if you want to add a game that launches with the command `dir C:`, you would add the following line:

   ```csv
   "dir","dir#C:"
   ```

   Note that the `games.csv` file must be in the same directory as the `main.py` file.

2. Launch the application.
3. In the search area, type the name of the game you want to launch.
4. Select the game from the list of results.
5. Click the "Launch" button to launch the game.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
