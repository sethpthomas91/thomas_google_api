# This class will be in responsible for calling the API

from ..api import google_books_api
from .Book import Book

class GoogleList:

    def __init__(self):
        self.search_list = []
    
    def reset_search_list(self):
        self.search_list = []

    # handles logic for menu choice 1
    def search_for_books(self, user_input):
        
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
 
    # takes in a selection from the search list and returns that book object
    def get_selected_book(self, user_selection):
        
        while True:
            if user_selection == 6:
                break

            elif user_selection > 0 and user_selection < 6:
                user_book_selection = self.search_list[user_selection-1]
            
                # reset search list
                self.reset_search_list()

                return user_book_selection
            # displays to user again if not a good input
            else:
                print(self.search_list)

    