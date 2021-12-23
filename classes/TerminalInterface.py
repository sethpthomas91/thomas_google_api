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
            mode = self.get_integer_input(TerminalMessage.initial_menu(), TerminalMessage.not_a_number_msg())

            if mode == 1:
                try:
                    self.google_search.search_for_books()
                    self.google_search.display_search_list()
                    self.google_search.get_selected_book()
                    self.reading_list.add_book(self.google_search.selected_book)
                except AttributeError:
                    print(TerminalMessage.abort_msg())
                    
            elif mode == 2:
                self.reading_list.display_reading_list()
            elif mode == 3:
                TerminalMessage.exit_msg()
                break

    def get_integer_input(self, prompt, error_msg):
        while True:
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError:
                print(error_msg)

                

            