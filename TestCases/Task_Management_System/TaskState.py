from abc import ABC, abstractmethod
from TaskStatus import TaskStatus

class TaskState(ABC):

    @abstractmethod
    def start_progress(self, task: 'Task')->None:
        pass

    @abstractmethod
    def complete_task(self, task: 'Task'):
        pass
    
    @abstractmethod
    def reopen_task(self, task: 'Task'):
        pass
    
    @abstractmethod
    def get_status(self) -> TaskStatus:
        pass