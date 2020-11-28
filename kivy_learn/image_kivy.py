import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.config import Config


Config.set('graphics', 'resizable', True)

class MyApp(App):
    def build(self):
        img = Image(source='sports.png')
        #button = Button(img)

        #button.bind(on_press=self.on_press_img)

        return img

    def on_press_img(self, instance):
        print("You press the image")



if __name__ == "__main__":
    img_app = MyApp()
    img_app.run()