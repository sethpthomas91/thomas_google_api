import requests
BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q='

# takes in user search terms and outputs a url with search terms
def url_constructor(search_terms):
    if " " in search_terms:
        search_terms = search_terms.replace(" ", "%20")
    return BASE_URL + search_terms

# takes in a url and makes a GET request
def api_request(url=BASE_URL):
    response = requests.get(url)
    return response

# should return a dictionary with only 5 objects if the API call went through
def api_json_return(response):
    search_dict = response.json()
    filtered_book_list = [
        search_dict['items'][0],
        search_dict['items'][1],
        search_dict['items'][2],
        search_dict['items'][3],
        search_dict['items'][4]
    ]
    return filtered_book_list

# takes in a book and filters out needed info
def book_filter(book):
    book_dict = {
        'author' : book['volumeInfo']['authors'][0],
        'title' : book['volumeInfo']['title'],
        'publishing_company' : book['volumeInfo']['publisher']
    }
    return book_dict
    


