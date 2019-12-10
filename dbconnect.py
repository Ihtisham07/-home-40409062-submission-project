import sqlite3
    

conn = sqlite3.connect(users1.db)
print "Database Opened Successfully";

conn.execute('CREATE TABLE users (uid TEXT, username TEXT, password TEXT, email TEXT, settings TEXT)')
print "Table created Successfully";
conn.close()

c = conn.cursor()
