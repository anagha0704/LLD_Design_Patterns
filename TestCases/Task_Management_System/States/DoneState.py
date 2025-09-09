from TaskState import TaskState
from TaskStatus import TaskStatus

class DoneState(TaskState):

    def start_progress(self, task: 'Task')->None:
        print("Cannot start a completed task. Reopen it first.")

    def complete_task(self, task: 'Task'):
        print("Task is already done.")
    
    def reopen_task(self, task: 'Task'):
        from States.ToDoState import ToDoState
        task.set_state(ToDoState())
    
    def get_status(self) -> TaskStatus:
        return TaskStatus.DONE