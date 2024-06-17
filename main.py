########################################################################################################################
#### IMPORTS ###########################################################################################################
########################################################################################################################

import csv
import subprocess
import tkinter as tk
from tkinter import messagebox
from typing import List, Optional, TypedDict


########################################################################################################################
#### CLASSES ###########################################################################################################
########################################################################################################################

class DataFileStructure(TypedDict):
    """
    Data structure for CSV files

    name: str -> file name
    delimiter: str -> delimiter
    quotechar: str -> quote character
    newline: str -> newline character
    """
    name: str
    delimiter: str
    quotechar: str
    newline: str
    nb_columns: int
    command_delimiter: str


class Game(TypedDict):
    """
    Data structure for games

    name: str -> game name
    launch_command: str -> launch command
    """
    name: str
    launch_command: str


class Games:
    """
    Class to manage games

    csv_file: DataFileStructure -> data structure for CSV files
    games: List[Game] -> list of games
    """
    csv_file: DataFileStructure
    games: List[Game]

    def __init__(self, csv_file: DataFileStructure):
        """
        Class constructor

        :param csv_file: DataFileStructure -> data structure for CSV files
        """
        self.csv_file = csv_file
        self.games: List[Game] = []

        self.load_games()

    def add_game(self, name: str, launch_command: str) -> None:
        """
        Adds a game to the list

        :param name: game name
        :param launch_command: launch command
        :return: None
        """
        self.games.append({'name': name, 'launch_command': launch_command})

    def load_games(self) -> None:
        """
        Loads games from the CSV file

        :return: None
        """
        self.games: List[Game] = []
        with open(self.csv_file['name'], newline=self.csv_file['newline']) as f:
            reader = csv.reader(f, delimiter=self.csv_file['delimiter'], quotechar=self.csv_file['quotechar'])
            headerPassed = False
            for row in reader:
                if not headerPassed:
                    if not (len(row) == self.csv_file['nb_columns'] and row[0] == 'name' and row[
                        1] == 'lunch_command'):
                        break
                    headerPassed = True
                    continue
                if len(row) == self.csv_file['nb_columns']:
                    self.add_game(row[0], row[1])

    def get_game(self, name: str) -> Optional[Game]:
        """
        Retrieves a game by its name

        :param name: game name
        :return: Optional[Game] -> game
        """
        for g in self.games:
            if g['name'] == name:
                return g
        return None

    def get_game_names(self) -> List[str]:
        """
        Retrieves the list of game names
        :return: List[str] -> list of game names
        """
        return [g['name'] for g in self.games]

    def get_game_launch_command(self, name: str) -> Optional[str]:
        """
        Retrieves the launch command of a game by its name

        :param name: game name
        :return: Optional[str] -> launch command
        """
        g = self.get_game(name)
        if g is not None:
            return g['launch_command']
        return None

    def get_command_delimiter(self) -> str:
        """
        Retrieves the command delimiter

        :return: str -> command delimiter
        """
        return self.csv_file['command_delimiter']


class Application(tk.Tk):
    """
    Class for the application

    games: Games -> games
    search_zone: tk.Frame -> search area
    search_entry: tk.Entry -> search field
    search_button: tk.Button -> search button
    list_zone: tk.Frame -> results area
    list_list: tk.Listbox -> list of games
    list_scrollbar: tk.Scrollbar -> scrollbar for the list
    launch_zone: tk.Frame -> launch area
    launch_button: tk.Button -> launch button
    """
    games: Games

    # widgets
    search_zone: tk.Frame
    search_entry: tk.Entry
    search_button: tk.Button
    list_zone: tk.Frame
    list_list: tk.Listbox
    list_scrollbar: tk.Scrollbar
    launch_zone: tk.Frame
    launch_button: tk.Button

    def __init__(self, name: str, version: str, csv_file: DataFileStructure):
        """
        Class constructor

        :param name: str -> application name
        :param version: str -> application version
        :param csv_file: DataFileStructure -> data structure for CSV files
        """
        super().__init__()

        self.games = Games(csv_file)

        self.title(f'{name} {version}')
        self.resizable(False, False)

        # search area
        self.search_zone = tk.Frame(self)

        self.search_entry = tk.Entry(self.search_zone)
        self.search_entry.pack(side=tk.LEFT)
        self.search_button = tk.Button(self.search_zone, text='Search', command=self.search)
        self.search_button.pack(side=tk.LEFT)

        self.search_zone.pack()

        # results area game list button with a scrollbar
        self.list_zone = tk.Frame(self)

        self.list_list = tk.Listbox(self.list_zone)
        self.list_list.pack(side=tk.LEFT)

        self.list_scrollbar = tk.Scrollbar(self.list_zone)

        self.list_list.config(yscrollcommand=self.list_scrollbar.set)
        self.list_scrollbar.config(command=self.list_list.yview)

        self.list_scrollbar.pack(side=tk.LEFT)

        self.list_zone.pack()

        # launch area
        self.launch_zone = tk.Frame(self)

        self.launch_button = tk.Button(self.launch_zone, text='Launch', command=self.launch)
        self.launch_button.pack()

        self.launch_zone.pack()

        # start the search
        self.search()
        # start the main loop
        self.mainloop()

    def search(self) -> None:
        """
        Searches for games

        :return: None
        """
        # if the search is empty, display all games
        search = self.search_entry.get()
        if search == '':
            games = self.games.get_game_names()
        elif len(search) == 1:
            games = [g for g in self.games.get_game_names() if search.lower() == g[0].lower()]
        else:
            games = [g for g in self.games.get_game_names() if search.lower() in g.lower()]
        self.list_list.delete(0, tk.END)
        for g in games:
            self.list_list.insert(tk.END, g)

    def launch(self) -> None:
        """
        Launches a game

        :return: None
        """
        try:
            selected_game = self.list_list.get(self.list_list.curselection())
        except tk.TclError:
            messagebox.showerror('Error', 'No game selected')
            return
        launch_command = self.games.get_game_launch_command(selected_game)
        if launch_command is not None:
            command_tab = launch_command.split(self.games.get_command_delimiter())
            try:
                res = subprocess.run(
                    command_tab, shell=True, text=True,  # capture_output=True, check=True
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                if res.returncode != 0:
                    raise Exception(f'Error code {res.returncode}\n{res.stderr}')
            except Exception as e:
                messagebox.showerror('Error', f'Error while launching {selected_game}:\n{e}')
            else:
                messagebox.showinfo('Success', f'{selected_game} launched')

        else:
            messagebox.showerror('Error', f'No launch command found for {selected_game}')


########################################################################################################################
#### MAIN ##############################################################################################################
########################################################################################################################


if __name__ == '__main__':
    try:
        app = Application(
            name='FakeLauncher',
            version='v1.0.0',
            csv_file=DataFileStructure(
                name="games.csv", delimiter=",", quotechar='"',
                newline='\n', nb_columns=2, command_delimiter='#'
            )
        )
        exit(0)
    except Exception as e:
        messagebox.showerror('Error', f'Error executing the application:\n{e}')
        exit(1)

########################################################################################################################
#### END OF FILE #######################################################################################################
########################################################################################################################
