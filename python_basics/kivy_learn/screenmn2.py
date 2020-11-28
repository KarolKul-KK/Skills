from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManage(ScreenManager):
    pass

presentation = Builder.load_file('cr.kv')

class ScrApp(App):

    def build(self):
        return presentation

if __name__ == "__main__":
    ScrApp().run()