from typing import List
from datetime import date
from Task import Task
from Priority import Priority
from TaskSortStrategy import TaskSortStrategy

class SortByDueDate(TaskSortStrategy):

    def sort(self, tasks: List[Task])->None:
        tasks.sort(key=lambda task: task.get_due_date() if task.get_due_date() else date.max)