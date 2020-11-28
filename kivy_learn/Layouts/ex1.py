import kivy
from kivy.app import App
kivy.require("2.0.0")
from kivy.uix.widget import Widget



class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()

customWidget = CustomWidgetApp()
customWidget.run()
