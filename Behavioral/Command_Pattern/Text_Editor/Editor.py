from Command import Command

class Editor:

    def __init__(self):
        self.history = []
        self.redo_stack = []

    def execute(self, command: Command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()

    def undo(self):
        if not self.history:
            print("Nothing to undo.")
            return
        command = self.history.pop()
        command.undo()
        self.redo_stack.append(command)
    
    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        last_command = self.redo_stack.pop()
        last_command.execute()
        self.history.append(last_command)