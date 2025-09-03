from Command import Command

class WriteText(Command):

    def __init__(self, editor: "TextEditor", txt: str):
        self.editor = editor
        self.txt = txt

    def execute(self):
        self.editor.write(self.txt)

    def undo(self):
        self.editor.delted(len(self.txt))