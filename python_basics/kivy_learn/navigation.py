from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import MDNavigationDrawer
#from navigationdrawer import MDNavigationDrawer


main_widget = Builder.load_file('nav.kv')

class Navigator(MDNavigationDrawer):
    image_source = StringProperty('images/me.png')

class NavigateApp(MDApp):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        self.nav_drawer = Navigator()
        return main_widget

NavigateApp().run()