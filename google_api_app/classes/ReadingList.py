# This class will generate the user's current reading list. It will also add books to the local reading list database.

import sqlite3
from .Book import Book
from .TerminalMessage import TerminalMessage
DATA_BASE = './google_api_app/data/reading_list.db'

class ReadingList:

    def __init__(self):
        self.books = Book.create_reading_list()

    # handles logic for menu choice 2
    def display_reading_list(self):

        TerminalMessage.start_display_msg()

        for book in self.books:
            print(book)

        TerminalMessage.end_display_msg()

    # adds a book to the sqlite database
    def add_book(self, book, db=DATA_BASE):
        conn = sqlite3.connect(db)
        curs = conn.cursor()
        curs.execute("INSERT INTO books VALUES (NULL,?,?,?)",(book.author, book.title, book.publishing_company))
        conn.commit()
        conn.close()

        # create a new reading list with the current books in the database
        self.books = Book.create_reading_list()

        TerminalMessage.book_added_msg()


    