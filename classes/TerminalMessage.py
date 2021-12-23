# this class will handle all displays to the user

class TerminalMessage:
    
    def welcome_msg():
        return print(""" 
Welcome user!

This is an application where you can search for books through your terminal. 
It relies on the google books database, so we hope you can find something you want to read.

You will mainly be using numbers to navigate the menu. 

Please feel free to add any books you come across to your reading list!
""")

    def initial_menu():
        return """
Please select a number that corresponds to what you want to do:
1. Search for books
2. View your current reading list
3. Exit the application
"""

    def exit_msg():
        return print(""" 
Have a nice day and happy reading!
""")

    def start_display_msg():
        return print(""" 
---------------------------
CURRENT READING LIST BELOW:
""")

    def end_display_msg():
        return print("""
END READING LIST
---------------------------
""") 

    def start_search_books_msg():
        return print(""" 
---------------------------
STARTING SEARCH FOR NEW BOOKS:
 """)

    def end_search_books_msg():
        return print(""" 
ENDING SEARCH FOR NEW BOOKS.
---------------------------              
""")

    def search_book_prompt():
        return """ 
What would you like to search for?
"""

    def user_selection_prompt():
        return"""

Which of these books would you like to add to your reading list?

If you don't see anything you like,
select 6 to go back to the main menu.
"""

    def user_has_selected_msg(book_selection):
        return print(f""" 
You have selected to add:
{book_selection}
""")

    def book_added_msg():
        return print(""" 
Book added to reading list.
""")

    def not_a_number_msg():
        return """ 
Please enter a valid number.
"""

    def abort_msg():
        return""" 
Returning to main menu.
"""

    def no_books_found_msg():
        return print(""" 
Sorry, but there were no books found.
Please try another search.
""")