import sqlite3

def login():
    while True:
        username = input("Please enter your name: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("sqldatabase.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM students WHERE name = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall

        if results:
            for i in results:
                print("Welcome ")
                break

        else:
            print("Username and password not recognised")
            again = input("Do you want try again?(Y/N): ")
            if again.lower() == "n":
                print("Good Bye")
                time.sleep(1)

login()
