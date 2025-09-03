from Command import Command

class PasteText(Command):

    def __init__(self, editor: "TextEditor"):
        self.editor = editor
        self.pasted = ""

    def execute(self):
        self.pasted = self.editor.clipboard
        self.editor.paste()

    def undo(self):
        if self.pasted:
            self.editor.delete(len(self.pasted))
