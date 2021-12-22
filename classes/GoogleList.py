# This class will be in responsible for calling the API

from api import google_books_api
from classes import TerminalInterface
from .TerminalMessage import TerminalMessage
from .Book import Book

class GoogleList:

    def __init__(self):
        self.search_list = []
        self.selected_book = None
    
    def reset_search_list(self):
        self.search_list = []

    # handles logic for menu choice 1
    def search_for_books(self):

        TerminalMessage.start_search_books_msg()

        user_input = input(TerminalMessage.search_book_prompt())
        
        # API logic chain
        new_url = google_books_api.url_constructor(user_input)
        json_obj = google_books_api.api_request(new_url)
        raw_book_list = google_books_api.api_json_return(json_obj)
        filtered_book_list = list(map(google_books_api.book_filter, raw_book_list))

        for index, book in enumerate(filtered_book_list):
            index += 1
            author = book['author']
            title = book['title']
            publishing_company = book['publishing_company']
            self.search_list.append(Book(index, author, title, publishing_company))

    # only displays search list
    def display_search_list(self):

        for book in self.search_list:
            print(book)

    
    def get_selected_book(self):
        
        while True:
            user_selection = input(TerminalMessage.user_selection_prompt())
            # if user input not verified it can throw a base 10 error when converting string to int
            if len(user_selection) == 1:

                if int(user_selection) == 6:
                    break

                elif int(user_selection) > 0 and int(user_selection) < 6:
                    user_book_selection = self.search_list[int(user_selection)-1]
                    
                    print(TerminalMessage.user_has_selected_msg(user_book_selection))
                
                self.selected_book = user_book_selection

                # reset search list
                self.reset_search_list()

                break
            # displays to user again if not a good input
            else:
                print(self.search_list)

    