from Editor import Editor
from TextEditor import TextEditor
from ConcreteCommands.CopyText import CopyText
from ConcreteCommands.DeleteText import DeleteText
from ConcreteCommands.PasteText import PasteText
from ConcreteCommands.WriteText import WriteText

class TextEditorDemo:

    def run():
        editor = TextEditor()
        invoker = Editor()

        # Write some text
        invoker.execute(WriteText(editor, "Hello "))
        invoker.execute(WriteText(editor, "World!"))

        # Delete last 6 characters ("World!")
        invoker.execute(DeleteText(editor, 6))

        # Undo delete (brings back "World!")
        invoker.undo()

        # Copy "Hello"
        invoker.execute(CopyText(editor, 0, 5))

        # Paste "Hello"
        invoker.execute(PasteText(editor))

        # Undo paste
        invoker.undo()

        # Redo paste
        invoker.redo()

if __name__ == "__main__":
    TextEditorDemo.run()