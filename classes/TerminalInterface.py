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

        # runs until a valid user input
        while True:
            mode = self.get_integer_input(TerminalMessage.initial_menu(), TerminalMessage.not_a_number_msg(), 3)

            if mode == 1:
                try:
                    # get user input
                    TerminalMessage.start_search_books_msg()
                    user_search = self.get_search_input(TerminalMessage.search_book_prompt())

                    # execute API search
                    self.google_search.search_for_books(user_search)
                    self.google_search.display_search_list()

                    # get the user's selection
                    user_selection = self.get_integer_input(TerminalMessage.user_selection_prompt(), TerminalMessage.not_a_number_msg(), 6)
                    new_book = self.google_search.get_selected_book(user_selection)
                    
                    # Add book to the database
                    TerminalMessage.user_has_selected_msg(new_book)
                    TerminalMessage.book_added_msg()
                    self.reading_list.add_book(new_book)
                except:
                    print(TerminalMessage.abort_msg())
                    
            elif mode == 2:
                self.reading_list.display_reading_list()
            elif mode == 3:
                TerminalMessage.exit_msg()
                break

    # handles user input for all menu choices. Cleans the input and provides error messages to the user.
    def get_integer_input(self, prompt, error_msg, choice_limit):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input > 0 and user_input <= choice_limit:
                    return user_input
                else:
                    print(error_msg)
            except ValueError:
                print(error_msg)

    # handles getting search input for books
    def get_search_input(self, prompt):   
        user_input = input(prompt)
        return user_input
                

            