from kivy.app import App
from kivy.core.text import LabelBase


class ChatApp(App):
    pass


if __name__ == '__main__':
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    ChatApp().run()