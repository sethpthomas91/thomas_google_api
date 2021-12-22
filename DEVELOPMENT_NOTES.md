Release notes:
This project meets the standards layed out by 8th Light's recruitment team. It includes the functions below:
1. Type in a query and display a list of 5 books matching that query.
2. Each item in the list should include the book's author, title, and publishing company.
3. A user should be able to select a book from the five displayed to save to a “Reading List”
4. View a “Reading List” with all the books the user has selected from their queries -- this is a local reading list and not tied to Google Books’s account features.

Future updates(by recommended priority):
1. This application lacks the ability to edit and delete books. This can be done by adding selection to the menu and building the feature in the ReadingList class. Information for adding this ability is in the SQLite documentation or at other tutorials. Information on SQLite queries can be found here: https://www.tutorialspoint.com/sqlite/sqlite_delete_query.htm 
3. Ability to utilize a user's google profile. It looks like the API documentaion has features where you can link them together. More information can be found here: https://developers.google.com/books/docs/v1/using#auth 
2. This application lacks the ability to have a user log in and out. This is currently designed for personal use. More research is needed to do this, but it looks like future developers could add a table to the SQLite database to handle users. The SQLite table for books would need a FOREIGN KEY that is associated with a user. I do not recommend this be implemented on this system or database as it seems there could be some security issues reading the database or changing the data. More research needs to be done in authentication methods.


Development history:
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
