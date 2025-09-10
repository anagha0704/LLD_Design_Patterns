from AbstractFactory import AbstractFactory
from Themes.DarkTheme import DarkTheme
from Styles.Button import Button
from Styles.Checkbox import Checkbox

class DarkFactory(AbstractFactory):

    def create_theme(self):
        theme = DarkTheme()
        return theme

    def create_button(self):
        button = Button()
        return button

    def create_checkbox(self):
        box = Checkbox()
        return box