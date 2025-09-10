from AbstractFactory import AbstractFactory
from Themes.LightTheme import LightTheme
from Styles.Button import Button
from Styles.Checkbox import Checkbox

class LightFactory(AbstractFactory):

    def create_theme(self):
        theme = LightTheme()
        return theme

    def create_button(self):
        button = Button()
        return button

    def create_checkbox(self):
        box = Checkbox()
        return box