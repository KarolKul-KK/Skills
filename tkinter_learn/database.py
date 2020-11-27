from tkinter import *
from PIL import ImageTk, ImageTk
import sqlite3


root = Tk()
root.title('Code at home')
root.geometry("400x400")

#database

conn = sqlite3.connect('addres_book.db')

#create cursor
c = conn.cursor()
'''
#create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
'''
#Create function to delete a record
def delete():
    conn = sqlite3.connect('addres_book.db')
    #create cursor
    c = conn.cursor()

    #Delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    conn.commit()

    conn.close()




#create submit function for database
def submit():
    conn = sqlite3.connect('addres_book.db')
    #create cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :adr, :city, :state, :zipcode )",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'adr': adr.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })

    conn.commit()

    conn.close()



    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    adr.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#create query function
def query():
    conn = sqlite3.connect('addres_book.db')
    #create cursor
    c = conn.cursor()
    #Query the database
    # oid is a numbet of id or something like that if first record oid = 1
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    #Loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    
    conn.commit()

    conn.close()



#create Text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
adr = Entry(root, width=30)
adr.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

#create Text box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
adr_label = Label(root, text="Address")
adr_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Delete ID" )
delete_box_label.grid(row=9, column=0, pady=5)

#create submit button
submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

#create a Query Button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create Delete button
delete_button = Button(root, text="Delete Records", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)




#comit changes
conn.commit()

#close connection
conn.close()



root.mainloop()