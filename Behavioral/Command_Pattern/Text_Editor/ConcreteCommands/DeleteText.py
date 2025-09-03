from Command import Command

class DeleteText(Command):

    def __init__(self, editor: "TextEditor", count):
        self.editor = editor
        self.count = count
        self.deleted = ""

    def execute(self):
        self.deleted = self.editor.delete(self.count)

    def undo(self):
        self.editor.write(self.deleted)