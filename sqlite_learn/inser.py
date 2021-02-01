import sqlite3


x = 'Liza'
y = '123'

with sqlite3.connect('sqldatabase.db') as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usernames(
userID INTEGER PRIMARY KEY,
name VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

cursor.execute(f"""
INSERT INTO usernames(name, password)
VALUES({x}, {y})
""")
db.commit()

cursor.execute("SELECT * FROM usernames")
print(cursor.fetchall())