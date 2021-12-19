# unit testing
import unittest

# application imports
import api

import json



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
        output = 'https://www.googleapis.com/books/v1/volumes?q=Dune%20Frank%20Herbert'
        self.assertEqual(input, output)
    
    def test_for_wrong_url_constructor(self):
        """ This will test that the user input is filtered before entering the API call """
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

if __name__ == "__main__":
    unittest.main()
