# thomas_google_api
This repository is for 8th Lights technical assessment. 

User notes:
1. In order to run this application you will need to create the database. Please follow the instructions below. Have the user run a file that contains the following instructions:
# conn = sqlite3.connect('./data/reading_list.db')
# curs = conn.cursor()
# curs.execute("""CREATE TABLE books (
#     id integer primary key,
#     author text,
#     title text,
#     publisher text
#     ) """)
# conn.commit()
# conn.close()


Project minimum viable product.
1. Type in a query and display a list of 5 books matching that query.
2. Each item in the list should include the book's author, title, and publishing company.
3. A user should be able to select a book from the five displayed to save to a “Reading List”
4. View a “Reading List” with all the books the user has selected from their queries -- this is a local reading list and not tied to Google Books’s account features.

Release 0 API Calls
Functionality:
1. Application files should make calls to google books API.

Testing:
1. Validate API call
2. Validate response data

Release 1 Backend Support
Functionality:
1. Ability to store data  
  a. Build Classes
    - Terminal Interface
    - Reading List
    - 
  b. Saving Data
    -SQL Lite vs csv file
    https://docs.python.org/3/library/sqlite3.html

Testing:
1. Ensure DB does not accept invalid data
2. Validate Class interactions

Release 2 Frontend User Terminal
Functionality
1. User is able to search for books using the API call functionality
2. User is able to display books to the terminal

Testing:
1. Terminal handles invalid inputs
