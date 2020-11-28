import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.accordion import Accordion

from tkinter.filedialog import askopenfilename
from tkinter import Tk

class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)


class ScreenTwo(BoxLayout, Screen, Accordion):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        self.create_table()
        self.get_table_column_headings()
        self.get_users()

    def populate_fields(self, instance): #new
        columns = self.data_items[instance.index]['range']
        self.user_no_text_input.text = self.data_items[columns[0]]['text']
        self.user_name_text_input.text = self.data_items[columns[1]]['text']

    def get_table_column_headings(self):
        connection = sqlite3.connect("demo.db")
        with connection:
            cursor = connection.cursor()
            cursor.execute("PRAGMA table_info(Users)")
            col_headings = cursor.fetchall()
            self.total_col_headings = len(col_headings)

    def filechooser(self):
        Tk().withdraw()
        self.image_path = askopenfilename(initiadir = "/", title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.image.source = self.image_path

    def create_table(self):
        connection = sqlite3.connect("demo.db")
        cursor = connection.cursor()
        sql = """CREATE TABLE IF NOT EXISTS Users(
            UserID integer PRIMARY KEY,
            UserName text NOT NULL)"""
        cursor.execute(sql)
        connection.close()

    def get_users(self):
        connection = sqlite3.connect("demo.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Users ORDER BY UserID ASC")
        rows = cursor.fetchall()

        # create list with db column, db primary key, and db column range
        data = []
        low = 0
        high = self.total_col_headings - 1
        # Using database column range for populating the TextInput widgets with values from the row clicked/pressed
        self.data_items = []
        for row in rows:
            for col in row:
                data.append([col, row[0], [low, high]])
            low += self.total_col_headings
            high += self.total_col_headings
        
        # Create data_items
        self.data_items = [{'text': str(x[0]), 'Index': str(x[1]), 'range': x[2]} for x in data]

    def save(self):
        connection = sqlite3.connect("demo.db")
        cursor = connection.cursor()

        UserID = self.user_no_text_input.text
        UserName = self.user_name_text_input.text

        EmpPhoto = open(self.image_path, "rb").read()

        try:
            save_sql = "INSER INTO Users (UserID, UserName) VALUES(?,?)"
            connection.execute(save_sql, (UserID, UserName))
            connection.commit()
            connection.close()
        except sqlite3.IntegrityError as e:
            print("Error: ", e)

        self.get_users() #New


class ScreenOne(Screen):
    pass


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    "Add selection and focus behaviour to the view"

class SelectableButton(RecycleDataViewBehavior, Button):


    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    
    def refresh_view_attrs(self, rv, index, data):
        "Catch and handle the view changes"
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        "Add selection on touch down"
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def aplly_selection(self, rv, index, is_selected):
        "Respond to the selection of items in the view."
        self.selected = is_selected

class OneApp(App):
    def build(self):
        return Manager()

if __name__ == "__main__":
    OneApp().run()
