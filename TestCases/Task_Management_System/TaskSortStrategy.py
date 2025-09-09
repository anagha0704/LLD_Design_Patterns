from typing import List
from Task import Task
from abc import ABC, abstractmethod

class TaskSortStrategy(ABC):

    @abstractmethod
    def sort(self, tasks: List[Task])->None:
        pass
