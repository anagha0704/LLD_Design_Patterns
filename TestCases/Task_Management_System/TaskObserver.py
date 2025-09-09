from abc import ABC, abstractmethod

class TaskObserver(ABC):

    @abstractmethod
    def update(self, task: 'Task', change_type: str)->None:
        pass

class ActivityLogger(TaskObserver):

    def update(self, task: 'Task', change_type: str)->None:
        print(f"LOGGER: Task '{task.get_title()}' was updated. Change: {change_type}")