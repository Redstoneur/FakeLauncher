import csv
import subprocess
import tkinter as tk
from tkinter import messagebox
from typing import List, Optional, TypedDict


class DataFileStructure(TypedDict):
    name: str
    delimiter: str
    quotechar: str
    newline: str


class Game(TypedDict):
    name: str
    lunch_command: str


class Games:
    csv_file: DataFileStructure
    games: List[Game]

    def __init__(self, csv_file: DataFileStructure):
        self.csv_file = csv_file
        self.games: List[Game] = []

        self.load_games()

    def add_game(self, name: str, lunch_command: str):
        self.games.append({'name': name, 'lunch_command': lunch_command})

    def load_games(self):
        self.games: List[Game] = []
        with open(self.csv_file['name'], newline=self.csv_file['newline']) as f:
            reader = csv.reader(f, delimiter=self.csv_file['delimiter'], quotechar=self.csv_file['quotechar'])
            headerPassed = False
            for row in reader:
                if not headerPassed:
                    if not (len(row) == 2 and row[0] == 'name' and row[1] == 'lunch_command'):
                        break
                    headerPassed = True
                    continue
                if len(row) == 2:
                    self.add_game(row[0], row[1])

    def get_game(self, name: str) -> Optional[Game]:
        for g in self.games:
            if g['name'] == name:
                return g
        return None

    def get_game_names(self) -> List[str]:
        return [g['name'] for g in self.games]

    def get_game_lunch_command(self, name: str) -> Optional[str]:
        g = self.get_game(name)
        if g is not None:
            return g['lunch_command']
        return None


class Application(tk.Tk):
    games: Games

    def __init__(self, name: str, version: str, csv_file: DataFileStructure):
        super().__init__()

        self.games = Games(csv_file)

        self.title(f'{name} {version}')
        self.resizable(False, False)

        # zone de recherche
        self.search_zone = tk.Frame(self)

        self.search_entry = tk.Entry(self.search_zone)
        self.search_entry.pack(side=tk.LEFT)
        self.search_button = tk.Button(self.search_zone, text='Search', command=self.search)
        self.search_button.pack(side=tk.LEFT)

        self.search_zone.pack()

        # zone de résultats liste des jeux bouton avec une scrollbar
        self.list_zone = tk.Frame(self)

        self.list_list = tk.Listbox(self.list_zone)
        self.list_list.pack(side=tk.LEFT)

        self.list_scrollbar = tk.Scrollbar(self.list_zone)

        self.list_list.config(yscrollcommand=self.list_scrollbar.set)
        self.list_scrollbar.config(command=self.list_list.yview)

        self.list_scrollbar.pack(side=tk.LEFT)

        self.list_zone.pack()

        # zone de lancement
        self.launch_zone = tk.Frame(self)

        self.launch_button = tk.Button(self.launch_zone, text='Launch', command=self.launch)
        self.launch_button.pack()

        self.launch_zone.pack()

        # lancement de la recherche
        self.search()
        # lancement de la boucle principale
        self.mainloop()

    def search(self):
        # si la recherche est vide, on affiche tous les jeux
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

    def launch(self):
        selected_game = self.list_list.get(self.list_list.curselection())
        lunch_command = self.games.get_game_lunch_command(selected_game)
        if lunch_command is not None:
            try:
                res = subprocess.run(lunch_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     text=True)
                if res != 0:
                    raise Exception(f'Error code {res.returncode}\n{res.stderr}')
            except Exception as e:
                messagebox.showerror('Error', f'Error while launching {selected_game}:\n{e}')
            else:
                messagebox.showinfo('Success', f'{selected_game} launched')

        else:
            messagebox.showerror('Error', f'No lunch command found for {selected_game}')


if __name__ == '__main__':
    try:
        app = Application(
            name='FakeLauncher',
            version='v1.0.0',
            csv_file=DataFileStructure(name="games.csv", delimiter=",", quotechar='"', newline='\n')
        )
        exit(0)
    except Exception as e:
        messagebox.showerror('Error', f'Error executing the application:\n{e}')
        exit(1)
