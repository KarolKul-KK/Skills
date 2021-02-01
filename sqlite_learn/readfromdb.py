import sqlite3


conn = sqlite3.connect('sqldatabase.db')
c = conn.cursor()


def read_from_db():
    c.execute("SELECT name, password FROM usernames")
    data = c.fetchall()
    print(data)
    #for row in c.fetchall():
     #   print(row[1])

read_from_db()