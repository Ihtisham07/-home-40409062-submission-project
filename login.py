import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS reglogin( username TEXT, password TEXT)')

def data_entry():
    c.execute('INSERT INTO reglogin VALUES(rock, ihtisham10)')
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
