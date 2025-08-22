from TextEditor import TextEditor
from Strategies.CapitalizeFormatter import Capitalize
from Strategies.LowerCaseFormatter import LowerCase
from Strategies.UpperCaseFormatter import UpperCase

class FormattingDemo:

    def run():
        editor = TextEditor()

        strategies = [Capitalize(), LowerCase(), UpperCase()]
        txt = "heLlo"

        for char in strategies:
            editor.set_strategy(char)
            print(f"Given string '{txt}' has been formatted: {editor.format_it(txt)}")

if __name__ == "__main__":
    FormattingDemo.run()