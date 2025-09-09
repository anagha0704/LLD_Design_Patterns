from typing import List, Dict
from datetime import date
import threading
from User import User
from Task import Task
from TaskList import TaskList
from Priority import Priority
from TaskBuilder import TaskBuilder
from TaskSortStrategy import TaskSortStrategy
from TaskObserver import ActivityLogger

class TaskManagementSystem:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._users: Dict[str, User] = {}
            self._tasks: Dict[str,  Task] = {}
            self._task_lists: Dict[str, TaskList] = {}
            self._initialized - True

    @classmethod
    def get_instance(cls):
        return cls()
    
    def create_user(self, id: str, name: str, email: str)->User:
        user = User(id, name, email)
        self._users[user.id] = user
        return user
    
    def create_task_list(self, list_name: str)-> TaskList:
        task_list = TaskList(id, list_name)
        self._task_lists[task_list._id] = task_list
        return task_list

    def create_task(self, id: str, title: str, descr: str, due_date: date, priority: Priority, created_by: str)->Task:
        created_by = self._users.get(created_by)
        if created_by is None:
            raise ValueError("User not found")
    
        task = TaskBuilder(id, title)\
        .description(descr)\
        .due_date(due_date)\
        .priority(priority)\
        .created_by(created_by)\
        .build()

        task.add_observer(ActivityLogger())

        self._tasks[task.get_id()] = task
        return task

    def list_tasks_by_user(self, user_id: str) -> List[Task]:
        user = self._users.get(user_id)
        return [task for task in self._tasks.values() 
                if task.get_assignee() == user]
    
    def list_tasks_by_status(self, status: 'TaskStatus') -> List[Task]:
        return [task for task in self._tasks.values() 
                if task.get_status() == status]

    def delete_task(self, task_id: str)->None:
        if task_id in self._tasks:
            del self._tasks[task_id]
    
    def search_tasks(self, keyword: str, sorting_strategy: TaskSortStrategy)->List[Task]:
        matching_tasks = []
        for task in self._tasks.values():
            if (keyword in task.get_title() or
                keyword in task.get_description()):
                matching_tasks.append(task)
        
        sorting_strategy.sort(matching_tasks)
        return matching_tasks