import kivy
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutApp(App):

    def build(self):
        return BoxLayout()

boxApp = BoxLayoutApp()
boxApp.run()