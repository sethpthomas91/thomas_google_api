from .ReadingList import ReadingList

class TerminalInterface:

    def __init__(self):
        self.reading_list = ReadingList()

    # main control for the user menu
    def run(self):
        while True:
            mode = input(self.initial_menu())
            if mode == '1':
                self.reading_list.search_for_books()
            elif mode == '2':
                self.reading_list.display_reading_list()
            elif mode == '3':
                print(""" 
Have a nice day!
""")
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
            

            