import kivy
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.stacklayout import StackLayout

class StackLayoutApp(App):
    def build(self):
        c = StackLayout()
        return c

if __name__ == "__main__":

    stApp = StackLayoutApp()
    stApp.run()