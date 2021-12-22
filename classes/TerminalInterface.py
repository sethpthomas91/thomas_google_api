# This class will handle recieving inputs from the user. It will also clean the data to protect against invalid input.

from .ReadingList import ReadingList
from .TerminalMessage import TerminalMessage
from .GoogleList import GoogleList

class TerminalInterface:

    def __init__(self):
        self.reading_list = ReadingList()
        self.google_search = GoogleList()

    # main control for the user menu
    def run(self):

        TerminalMessage.welcome_msg()

        while True:
            mode = input(TerminalMessage.initial_menu())
            if mode == '1':
                self.google_search.search_for_books()
                self.google_search.display_search_list()
                self.google_search.get_selected_book()
                self.reading_list.add_book(self.google_search.selected_book)
            elif mode == '2':
                self.reading_list.display_reading_list()
            elif mode == '3':
                TerminalMessage.exit_msg()
                break


            

            