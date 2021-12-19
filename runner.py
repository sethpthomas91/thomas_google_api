# This will be the main calling function to run the application
from classes.TerminalInterface import TerminalInterface
TerminalInterface().run()


import sqlite3

# This will create the local database, must be run as the first step, but never again
# conn = sqlite3.connect('./data/reading_list.db')
# curs = conn.cursor()
# curs.execute("""CREATE TABLE books (
#     book_id INTEGER PRIMARY KEY,
#     author text,
#     title text,
#     publisher text
#     ) """)
# conn.commit()
# conn.close()

# saving data to the database
# conn = sqlite3.connect('./data/reading_list.db')
# curs = conn.cursor()
# curs.execute("INSERT INTO books VALUES ('Frank Herbert', 'Dune', 'Penguin')")
# curs.execute("INSERT INTO books VALUES ('Frank Herbert', 'Children of Dune', 'Penguin')")
# conn.commit()
# conn.close()

# querying the database
# conn = sqlite3.connect('./data/reading_list.db')
# curs = conn.cursor()
# curs.execute("SELECT * FROM books")
# curs.execute("SELECT * FROM books WHERE title='Dune'")
# print(curs.fetchall())
# conn.commit()
# conn.close()

# proper way to enter information to protect from SQL injection attacks
# book_1 = classes.Book('Douglas Adams','Hitchhikers Guide to the Galaxy','Megadodo')
# book_2 = classes.Book('Douglas Adams','The Restaurant at the End of the Universe', 'Megadodo')
# conn = sqlite3.connect('./data/reading_list.db')
# curs = conn.cursor()
# curs.execute("INSERT INTO books VALUES (NULL,?,?,?)",(book_1.author, book_1.title, book_1.publishing_company))
# curs.execute("INSERT INTO books VALUES (NULL,?,?,?)",(book_2.author, book_2.title, book_2.publishing_company))
# conn.commit()
# conn.close()

# grabbing all of the books
# conn = sqlite3.connect('./data/reading_list.db')
# curs = conn.cursor()
# curs.execute("SELECT * FROM books")
# print(curs.fetchall())
# conn.commit()
# conn.close()