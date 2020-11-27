import kivy
from kivy.app import App
kivy.require("2.0.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


Window.size = (400, 600)
Window.clearcolor = (1, 1, 1, 1)


class FloatingApp(App):

    def build(self):
        return FloatLayout()

flApp = FloatingApp()
flApp.run()
