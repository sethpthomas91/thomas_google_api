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
        
        # API logic chain
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
        for book in book_obj_list:
            print(book)
        while True:
            user_selection = input("""

Which of these books would you like to add to your reading list?

If you don't see anything you like,
select 6 to go back to the main menu.
""")
            # if user input not verified it can throw a base 10 error when converting string to int
            if len(user_selection) == 1:

                if int(user_selection) == 6:
                    break

                elif int(user_selection) > 0 and int(user_selection) < 6:
                    user_book_selection = book_obj_list[int(user_selection)-1]
                    print(f""" 
You have selected to add:
{user_book_selection}
 """)
                self.add_book(user_book_selection)
                print(""" 
Book added to reading list!
""")
                print(""" 
ENDING SEARCH FOR NEW BOOKS.
---------------------------              
""")
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

    # adds a book to the sqlite database
    def add_book(self, book):
        conn = sqlite3.connect('./data/reading_list.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO books VALUES (NULL,?,?,?)",(book.author, book.title, book.publishing_company))
        conn.commit()
        conn.close()
        self.books = Book.create_reading_list()

    