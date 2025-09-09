from typing import List
from Task import Task
import threading

class TaskList:

    def __init__(self, id: str,  name: str):
        self._id = id
        self._name = name
        self._tasks: List[Task] = []
        self._lock = threading.Lock()

    def add_task(self, task: Task)->None:
        with self._lock:
            self._tasks.append(task)
        
    def get_task(self)->List[Task]:
        with self._lock:
            return self._tasks
        
    @property
    def name(self):
        return self._name
    
    def display(self):
        print(f"---Task List: {self._name}---")
        for  task in self._tasks:
            task.display()
        print("-----------")