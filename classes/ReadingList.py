from classes.Book import Book
from api import google_books_api
import sqlite3

class ReadingList:

    def __init__(self):
        self.books = Book.create_reading_list()

    # handles logic for menu choice 1
    def search_for_books(self):
        print(""" 
---------------------------
STARTING SEARCH FOR NEW BOOKS:
 """)
        user_input = input("What would you like to search for?\n")
        new_url = google_books_api.url_constructor(user_input)
        json_obj = google_books_api.api_request(new_url)
        raw_book_list = google_books_api.api_json_return(json_obj)
        filtered_book_list = list(map(google_books_api.book_filter, raw_book_list))
        book_obj_list = []
        for index, book in enumerate(filtered_book_list):
            index += 1
            author = book['author']
            title = book['title']
            publishing_company = book['publishing_company']
            book_obj_list.append(Book(index, author, title, publishing_company))
        # initial display of choices for the user
        print(book_obj_list)
        while True:
            user_selection = int(input("""

Which of these books would you like to add to your reading list?

If you don't see anything you like,
select 6 to go back to the main menu.
"""))

            if user_selection == 6:
                break
            if int(user_selection) > 0 and user_selection < 6:
                user_book_selection = book_obj_list[user_selection-1]
                print(f""" 
You have selected to add:
{user_book_selection}
 """)
                self.add_book(user_book_selection)
                print("Book added to reading list")
                break
            # displays to user again if not a good input
            else:
                print(book_obj_list)

    # handles logic for menu choice 2
    def display_reading_list(self):
        print(""" 
---------------------------
CURRENT READING LIST BELOW:
 """)   
        for book in self.books:
            print(book)
        
        print("""
END READING LIST
---------------------------
 """)


    def add_book(self, book):
        conn = sqlite3.connect('./data/reading_list.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO books VALUES (NULL,?,?,?)",(book.author, book.title, book.publishing_company))
        conn.commit()
        conn.close()
        self.books = Book.create_reading_list()