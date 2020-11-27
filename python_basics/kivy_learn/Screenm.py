from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current
# This is how you can control the ScreenManager from kv.
# Each screen has by default a property manager that gives you insatnce of the screenmanager

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: "Go to settings"
            on_press: root.manager.current = "settings"
        Button:
            text: "Quit"

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()