import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config


Config.set('graphics', 'resizable', True)




class ButtonApp(App):

    def build(self):
        btn = Button(text="Push Me!",
                    color=(1, 0, .65, 1),
                    background_normal= 'program.png',
                    background_down= 'program.png',
                    size_hint=(.3, .3),
                    pos_hint={"x":0.35, "y":0.3}
                    )


        btn.bind(on_press=self.on_press_button)
        return btn

    def on_press_button(self, instance):
        print('You pressed the button!')
        


if __name__ == '__main__':

    root = ButtonApp()
    root.run()