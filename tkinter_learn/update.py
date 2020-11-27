from tkinter import *
from PIL import ImageTk, ImageTk
import sqlite3


root = Tk()
root.title('Code at home')
root.geometry("400x500")

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
#Create update function to save our new edited data
def update():
    conn = sqlite3.connect('addres_book.db')
    #create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""", 
        {'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'address': adr_editor.get(),
        'city': city_editor.get(),
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': record_id
        })

    #Commit changes
    conn.commit()
    #Close connection
    conn.close()
    
    editor.destroy()

    #clear the text boxes
    f_name_editor.delete(0, END)
    l_name_editor.delete(0, END)
    adr_editor.delete(0, END)
    city_editor.delete(0, END)
    state_editor.delete(0, END)
    zipcode_editor.delete(0, END)




#Create edit function to update records
def edit():
    global editor
    editor = Tk()
    editor.title('Update a Record')
    editor.geometry("400x400")
    conn = sqlite3.connect('addres_book.db')
    #create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    #Query the database
    # oid is a numbet of id or something like that if first record oid = 1
    c.execute("SELECT * FROM addresses where oid = " + record_id)
    records = c.fetchall()
    # print(records)
    #Loop thru results
    
    #create Global variables for text box names
    global f_name_editor
    global l_name_editor
    global adr_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    #create Text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    adr_editor = Entry(editor, width=30)
    adr_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    #create Text box Labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    adr_label_editor = Label(editor, text="Address")
    adr_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    #Put data to boxes when we choose id and click edit
    for record in records:
        f_name_editor.insert(0 ,record[0])
        l_name_editor.insert(0 ,record[1])
        adr_editor.insert(0 ,record[2])
        city_editor.insert(0 ,record[3])
        state_editor.insert(0 ,record[4])
        zipcode_editor.insert(0 ,record[5])

    #Create a save button To save edited record
    save_button = Button(editor, text="Save Records", command=update)
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    


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
    query_label.grid(row=13, column=0, columnspan=2)
    
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

delete_box_label = Label(root, text="Select ID" )
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

# Create an update button
edit_button = Button(root, text="Edit Records", command=edit)
edit_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


#comit changes
conn.commit()

#close connection
conn.close()



root.mainloop()