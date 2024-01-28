from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):

    def printing_msg(self):
        data = self.ids.textInput.text
        self.ids.label.text = data


class FirstApp(App):
    pass

FirstApp().run()