from kivy.app import App
from kivy.lang import Builder

kv_str = Builder.load_string('''
ActionBar:
    pos_hint: {'top':1}
    ActionView:
        use_separator: True
        ActionPrevious:
            title: "Example App"
            with_previous: False
        ActionButton:
            text: 'File'
        ActionButton:
            text: 'Edit'
        ActionGroup:
            text: 'Tools'
            mode: 'spinner'
            ActionButton:
                text: 'tool1'
            ActionButton:
                text: 'tool2'
            ActionButton:
                text: 'tool3'
            ActionButton:
                text: 'tool4'
''')

class ExampleApp(App):
    def build(self):
        return kv_str

if __name__ == '__main__':
    ExampleApp().run()