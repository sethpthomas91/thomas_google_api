# This will be the main calling function to run the application
from classes.TerminalInterface import TerminalInterface
import sqlite3

try:
    TerminalInterface().run()
    
except:
    conn = sqlite3.connect('./data/reading_list.db')
    curs = conn.cursor()
    curs.execute("""CREATE TABLE books (
        book_id INTEGER PRIMARY KEY,
        author text,
        title text,
        publisher text
        ) """)
    conn.commit()
    conn.close()

    TerminalInterface().run()





# This will create the local database, must be run as the first step, but never again
