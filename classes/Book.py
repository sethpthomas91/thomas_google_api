# This class will be the framework for the book. It will be the main object passed into the database. We can make direct updates to books here in the future.

import sqlite3

class Book:

    def __init__(self, id, author, title, publishing_company):
        self.id = id
        self.author = author
        self.title = title
        self.publishing_company = publishing_company

    # modify data for book
    def update_author(self, new_author):
        self.author = new_author
    def update_author(self, new_title):
        self.title = new_title
    def update_author(self, new_publishing_company):
        self.publishing_company = new_publishing_company

    def __repr__(self):
        return f"""
Book ID: {self.id} 
    Title: {self.title}
    Author: {self.author} 
    Publisher: {self.publishing_company}"""

    # creates all books for display, read only
    @classmethod
    # uses SQLite database to generate the current reading list(all items)
    def create_reading_list(cls):
        reading_list = []
        # the database call is relative to where the runner.py is
        conn = sqlite3.connect('./data/reading_list.db')
        curs = conn.cursor()
        curs.execute("SELECT * FROM books")
        all_books_db = curs.fetchall()
        def db_to_list(obj):
            new_book = Book(obj[0],obj[1],obj[2],obj[3])
            return new_book
        reading_list = list(map(db_to_list, all_books_db))
        conn.commit()
        conn.close()
        return reading_list
