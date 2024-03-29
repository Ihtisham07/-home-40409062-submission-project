import sqlite3

try:
    sqliteConnection = sqlite3.connect('users.csv')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    with open('query', 'r') as sqlite_file:
        sql_script = sqlite_file.read()

    cursor.executescript(sql_script)
    print("SQLite script executed successfully")
    cursor.close()

except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")
