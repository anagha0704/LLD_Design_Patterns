from TaskState import TaskState
from TaskStatus import TaskStatus

class InProgressState(TaskState):

    def start_progress(self, task: 'Task')->None:
        print("Task is already in Progress.")

    def complete_task(self, task: 'Task'):
        from States.DoneState import DoneState
        task.set_state(DoneState())
    
    def reopen_task(self, task: 'Task'):
        from States.ToDoState import ToDoState
        task.set_state(ToDoState())
    
    def get_status(self) -> TaskStatus:
        return TaskStatus.IN_PROGRESS