from kivy.app import App
from kivy.core.text import LabelBase


# Needs JDK and Android emulator

class MetroApp(App):
    pass


if __name__ == '__main__':
    LabelBase.register(name='Modern Pictograms', fn_regular='modernpics.ttf')
    MetroApp().run()