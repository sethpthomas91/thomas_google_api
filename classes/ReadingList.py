# This class will generate the user's current reading list. It will also add books to the local reading list database.

from classes.Book import Book
import sqlite3
from api import google_books_api
from .TerminalMessage import TerminalMessage
DATA_BASE = './data/reading_list.db'

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

        TerminalMessage.user_has_selected_msg(book)
        TerminalMessage.book_added_msg()

        self.books = Book.create_reading_list()

    