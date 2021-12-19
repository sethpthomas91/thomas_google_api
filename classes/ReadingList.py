from classes.Book import Book

class ReadingList:

    def __init__(self):
        self.books = Book.create_reading_list()

    # handles logic for menu choice 1
    def search_for_books(self):
        pass

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