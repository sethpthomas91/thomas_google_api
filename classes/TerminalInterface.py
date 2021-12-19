import sqlite3
from .ReadingList import ReadingList

class TerminalInterface:

    def __init__(self):
        self.reading_list = ReadingList()

    # main control for the user menu
    def run(self):
        while True:
            mode = input(self.initial_menu())
            if mode == '1':
                print("Will search for books")
            elif mode == '2':
                self.reading_list.display_reading_list()
            elif mode == '3':
                print("Exits application")
                break

    def initial_menu(self):
        return """
Welcome user!
This is an application where you can search for books through your terminal.
Please select a number that corresponds to what you want to do:
1. Search for books
2. View your current reading list
3. Exit the application
"""
            

            