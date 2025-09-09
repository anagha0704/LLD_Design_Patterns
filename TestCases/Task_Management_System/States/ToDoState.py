from TaskState import TaskState
from TaskStatus import TaskStatus

class ToDoState(TaskState):

    def start_progress(self, task: 'Task')->None:
        from InProgressState import InProgressState
        task.set_state(InProgressState())

    def complete_task(self, task: 'Task'):
        print("Cannot complete a task that is not in progress.")
    
    def reopen_task(self, task: 'Task'):
        print("Task is already in To-Do state.")
    
    def get_status(self) -> TaskStatus:
        return TaskStatus.TODO