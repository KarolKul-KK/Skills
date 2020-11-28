SidePanel_AppMenu = {'v one':['on_uno', None],
                    'v two':['on_due', None],
                    'v three':['on_tre', None],
                    }
id_AppMenu_METHOD = 0
id_AppMenu_Panel = 1

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.NavigationDrawer import NavigationLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar, ActionButton, ActionPrevious
from kivy.properties import ObjectProperty

RootApp = None

class SidePanel(BoxLayout):
    pass

class MenuItem(Button):
    def __init__(self, **kwargs):
        super(MenuItem, self).__init__( **kwargs)
        self.bind(on_press=self.menuitem_selected)

    def menuitem_selected(self, *args):
        print(self.text, SidePanel_AppMenu[self.text], SidePanel_AppMenu[self.text][id_AppMenu_METHOD])
        try:
            function_to_call = SidePanel_AppMenu[self.text][id_AppMenu_METHOD]
        except:
            print('error')
            return
        getattr(RootApp, function_to_call)()

class AppActionBar(ActionBar):
    pass

class ActionMenu(ActionPrevious):
    def menu(self):
        print('ActionMenu')
        RootApp.toogle_sidepanel()

class ActionQuit(ActionButton):
    def menu(self):
        print('App quit')
        RootApp.stop()

class MainPanel(BoxLayout):
    pass

class AppArea(FloatLayout):
    pass

class PageOne(FloatLayout):
    pass

class PageTwo(FloatLayout):
    pass

class PageThree(FloatLayout):
    pass

class AppButton(Button):
    n_button = ObjectProperty(None)
    def app_pushed(self):
        print(self.text, 'button', self.nbutton.state)

class NavDrawer(NavigationDrawer):
    def __ini__(self, **kwargs):
        super(NavDrawer, self).__init__( **kwargs)

    def close_sidepanel(self, animate=True):
        if self.state == 'open':
            if animate:
                self.anim_to_state('closed')
            else:
                self.state = 'closed'

class AndroidApp(App):
    def build(self):

        global RootApp
        RootApp = self

        # Navigation drawer
        self.NavDrawer = NavDrawer()

        side_panel = SidePanel()
        self.navigationdrawer.add_widget(side_panel)

        self.main_panel = MainPanel()

        self.navigationdrawer.anim_type = 'slide_above_anim'
        self.navigationdrawer.add_widget(self.main_panel)

        return self.navigationdrawer

    def toggle_sidepanel(self):
        self.navigationdrawer.toggle_state()

    def on_one(self):
        print('One... exec')
        self.switch_main_page('v one', PageOne)

    def on_two(self):
        print('Two... exec')
        self._switch_main_page('v two', PageTwo)

    def on_three(self):
        print('Three... exec')
        self._switch_main_page('v three', PageThree)

    def _switch_main_page(self, key, panel):
        self.navigationdrawer.close_sidepanel()
        if not SidePanel_AppMenu[key][id_AppMenu_PANEL]:
            SidePanel_AppMenu[key][id_AppMenu_PANEL]
        main_panel = SidePanel_AppMenu[key][id_AppMenu_PANEL]
        self.navigationdrawer.remove_widget(self.main_panel)
        self.navigationdrawer.add_widget(main_panel)
        self.main_panel = main_panel

if __name__ == '__main__':
    AndroidApp().run()