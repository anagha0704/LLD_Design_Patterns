from typing import Set
from datetime import date
from Priority import Priority
from User import User
from Tag import Tag

class TaskBuilder:

    def __init__(self, id :str,title: str):
        self._id = id
        self._title = title
        self._description = ""
        self._due_date = None
        self._priority = None
        self._created_by = None
        self._assignee = None
        self._tags = set()

    def description(self, descr: str)->'TaskBuilder':
        self._description = descr
        return self
    
    def due_date(self, due_date: date)->'TaskBuilder':
        self._due_date = due_date
        return self
    
    def priority(self, priority: Priority)->'TaskBuilder':
        self._priority = priority
        return self
    
    def assignee(self, assignee: User) -> 'TaskBuilder':
            self._assignee = assignee
            return self
        
    def created_by(self, created_by: User) -> 'TaskBuilder':
        self._created_by = created_by
        return self
    
    def tags(self, tags: Set[Tag]) -> 'TaskBuilder':
        self._tags = tags
        return self
    
    def build(self) -> 'Task':
        from Task import Task
        return Task(self)