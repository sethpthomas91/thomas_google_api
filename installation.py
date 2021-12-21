import sqlite3

def create_table():
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

create_table()