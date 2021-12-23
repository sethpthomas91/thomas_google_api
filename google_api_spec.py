# unit testing
import unittest
from unittest.mock import patch

# application imports
import api
import classes

# misc imports
import sqlite3
import json
from classes.GoogleList import GoogleList

from classes.ReadingList import ReadingList
from classes.TerminalInterface import TerminalInterface
from classes.TerminalMessage import TerminalMessage

# global variables
TEST_URL = 'https://www.googleapis.com/books/v1/volumes?q=flowers%20for%20algernon'

# API testing
class TestCasesAPICalls(unittest.TestCase):
    """ This will test functionality of the Google API Call """
    def test_for_API_call(self):
        """ This will test that the API call is returning a 200 code """
        input = api.api_request(TEST_URL).status_code
        output = 200
        self.assertEqual(input, output)
    
    def test_for_wrong_API_call(self):
        """ This will test that the API call is returning a 400 code if it has the wrong url """
        BAD_URL = 'https://www.googleapis.com/'
        input = api.api_request(BAD_URL).status_code
        output = 404
        self.assertEqual(input, output)
    
    def test_for_url_constructor(self):
        """ This will test that the user input is filtered before entering the API call """
        input = api.url_constructor("Dune Frank Herbert")
        output = 'https://www.googleapis.com/books/v1/volumes?q=Dune%20Frank%20Herbert&printType=books&startIndex=0&maxResults=5'
        self.assertEqual(input, output)
    
    def test_for_wrong_url_constructor(self):
        """ This will test that the user input is filtered before entering the API call, false positive test. """
        input = api.url_constructor("Dune Frank Herbert")
        output = 'https://www.googleapis.com/books/v1/volumes?q=Dune Frank Herbert'
        self.assertNotEqual(input, output)

    def test_book_filter(self):
        """ Will test that a passed in book dictionary will be filtered down to a smaller book object """
        with open('./tests/test_book.json', 'r') as test_data:
            test_book = json.loads(test_data.read()) 
        input = api.book_filter(test_book)
        output = {
        'author' : "Frank Herbert",
        'title' : "Dune",
        'publishing_company' : "Penguin"
    }
        self.assertEqual(input, output)

    def test_book_class_title(self):
        """ Will test a book class being created """
        book_1 = classes.Book('1','Douglas Adams','Hitchhikers Guide to the Galaxy','Megadodo')
        input = book_1.author
        output = 'Douglas Adams'
        self.assertEqual(input, output)
    
    def test_book_class_wrong_output(self):
        """ Will test a book class being created, tests for false positive """
        book_1 = classes.Book('1','Douglas Adams','Hitchhikers Guide to the Galaxy','Megadodo')
        input = book_1.title
        output = 'Megadodo'
        self.assertNotEqual(input, output)

    def test_reading_list_class(self):
        """ Will test a reading list being created """
        reading_list = ReadingList()
        book_1 = classes.Book('1','Test Author 1','Test Title 1','Test Publisher 1')
        book_2 = classes.Book('2','Test Author 2','Test Title 2','Test Publisher 2')
        book_3 = classes.Book('3','Test Author 3','Test Title 3','Test Publisher 3')
        reading_list.books = [book_1, book_2, book_3]
        input = reading_list.books[1]
        output = book_2
        self.assertEqual(input, output)

    def test_reading_list_class_false_pos(self):
        """ Will test a reading list being created, tests for a false positive """
        reading_list = ReadingList()
        book_1 = classes.Book('1','Test Author 1','Test Title 1','Test Publisher 1')
        book_2 = classes.Book('2','Test Author 2','Test Title 2','Test Publisher 2')
        book_3 = classes.Book('3','Test Author 3','Test Title 3','Test Publisher 3')
        reading_list.books = [book_1, book_2, book_3]
        input = reading_list.books[0]
        output = book_3
        self.assertNotEqual(input, output)
    
    def test_book_creation(self):
        """ Tests for creating an instance of a book """
        book_1 = classes.Book('1','Test Author 1','Test Title 1','Test Publisher 1')
        input = book_1
        output = classes.Book
        self.assertIsInstance(input, output)

    def test_reading_list_creation(self):
        """ Tests for creating an instance of a reading list """
        reading_list = classes.ReadingList()
        input = reading_list
        output = classes.ReadingList
        self.assertIsInstance(input, output)

    def test_google_list_creation(self):
        """ Test for creating an instance of a google list """
        google_list = GoogleList()
        input = google_list
        output = classes.GoogleList
        self.assertIsInstance(input, output)

    def test_google_list_selected_book(self):
        """ Test for proper return of a user selected book """
        google_list = GoogleList()
        book_1 = classes.Book('1','Test Author 1','Test Title 1','Test Publisher 1')
        book_2 = classes.Book('2','Test Author 2','Test Title 2','Test Publisher 2')
        book_3 = classes.Book('3','Test Author 3','Test Title 3','Test Publisher 3')
        google_list.search_list = [book_1, book_2, book_3]
        input = google_list.get_selected_book(1)
        output = book_1
        self.assertEqual(input, output)

    def test_google_list_selected_book_false_pos(self):
        """ Test for proper return of a user selected book, testing for false positive """
        google_list = GoogleList()
        book_1 = classes.Book('1','Test Author 1','Test Title 1','Test Publisher 1')
        book_2 = classes.Book('2','Test Author 2','Test Title 2','Test Publisher 2')
        book_3 = classes.Book('3','Test Author 3','Test Title 3','Test Publisher 3')
        google_list.search_list = [book_1, book_2, book_3]
        input = google_list.get_selected_book(2)
        output = book_3
        self.assertNotEqual(input, output)
    
    @patch('classes.TerminalInterface.get_search_input', return_value='this is a search')
    def test_input_returns_string(self, input):
        self.assertEqual(classes.TerminalInterface.get_search_input(), 'this is a search')


if __name__ == "__main__":
    unittest.main()
