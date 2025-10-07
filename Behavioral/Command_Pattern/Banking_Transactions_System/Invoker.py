from typing import List, Optional
from Command import Command

class Invoker:

    def __init__(self):
        self.curr_command = None
        self.history = []
    
    def set_command(self, command:Command)->None:
        self.curr_command = command
    
    def execute_command(self)->None:
        self.curr_command.execute()
        self.history.append(self.curr_command)
    
    def rollback_last_command(self)->None:
        if self.history:
            last_command = self.history.pop()
            last_command.rollback()
        else:
            raise ValueError("There is no previous transaction to undo!")

    def redo_command(self)->None:
        if self.history:
            self.curr_command = self.history[-1]
            self.curr_command.execute()
            self.history.append(self.curr_command)
        else:
            raise ValueError("There is no previous transaction to undo!")

    def show_history(self)->Optional[List]:
        return self.history