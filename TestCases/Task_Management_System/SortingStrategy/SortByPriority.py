from typing import List
from Task import Task
from Priority import Priority
from TaskSortStrategy import TaskSortStrategy

class SortByPriority(TaskSortStrategy):

    def sort(self, tasks: List[Task])->None:
        # higher priority first
        priority_order = {Priority.CRITICAL: 4, Priority.HIGH: 3, 
                         Priority.MEDIUM: 2, Priority.LOW: 1}
        
        tasks.sort(key=lambda task: priority_order.get(task.get_priority(), 0), reverse=True)