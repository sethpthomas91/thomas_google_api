import requests

from ..classes.TerminalMessage import TerminalMessage
BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q='
BOOK_FILTER = '&printType=books'
RESULT_LIMIT = '&startIndex=0&maxResults=5'

# takes in user search terms and outputs a url with search terms
def url_constructor(search_terms):
    if " " in search_terms:
        search_terms = search_terms.replace(" ", "%20")
    return BASE_URL + search_terms + BOOK_FILTER + RESULT_LIMIT

# takes in a url and makes a GET request
def api_request(url=BASE_URL):
    try:
        response = requests.get(url)
        return response
    except:
        return TimeoutError

# should return a dictionary with only 5 objects if the API call went through
def api_json_return(response):
    search_dict = response.json()

    if search_dict['totalItems'] == 0:
        TerminalMessage.no_books_found_msg()
        return None

    filtered_book_list = []
    for book in search_dict['items']:
        filtered_book_list.append(book)
    return filtered_book_list

# takes in a book and filters out needed info
def book_filter(book):
    # handles errors if components don't exist
    if 'authors' in book['volumeInfo']:
        author = book['volumeInfo']['authors'][0]
    else :
        author = "No author on record"
    
    if 'title' in book['volumeInfo']:
        title = book['volumeInfo']['title']
    else: 
        title = "No title on record"
    
    if 'publisher' in book['volumeInfo']:
        publishing_company = book['volumeInfo']['publisher']
    else:
        publishing_company = "No publisher on record"

    book_dict = {
        'author' : author,
        'title' : title,
        'publishing_company' : publishing_company
    }
    return book_dict
    


