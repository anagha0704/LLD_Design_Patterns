from Command import Command

class CopyText(Command):

    def __init__(self, editor: "TextEditor", start: int, end: int):
        self.editor = editor
        self.start = start
        self.end = end

    def execute(self):
        self.editor.copy(self.start, self.end)

    def undo(self):
        print("Copy cannot be undone")