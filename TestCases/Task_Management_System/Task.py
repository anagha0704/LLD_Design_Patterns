from typing import List, Optional
from datetime import date
import threading
from TaskBuilder import TaskBuilder
from Comment import Comment
from ActivityLog import ActivityLog
from States.ToDoState import ToDoState
from User import User
from Priority import Priority
from TaskStatus import TaskStatus
from TaskState import TaskState
from TaskObserver import TaskObserver
from States.ToDoState import ToDoState

class Task:

    def __init__(self, builder: TaskBuilder):
        self._id = builder._id
        self._title = builder._title
        self._description = builder._description
        self._due_date = builder._due_date
        self._priority = builder._priority
        self._created_by = builder._created_by
        self._assignee = builder._assignee
        self._tags = builder._tags
        self._comments: List[Comment] = []
        self._subtasks: List['Task'] = []
        self._observers: List[TaskObserver] = []
        self._activity_logs: List[ActivityLog] = []
        self._current_state = ToDoState()
        self._lock = threading.Lock()
        self.add_log(f"Task created with title: {self._title}")

    def set_assignee(self, user: User)->None:
        with self._lock:
            self._assignee = user
            self.add_log(f"Assigned to {user.name}")
            self.notify_observer("assignee")

    def update_priority(self, priority: Priority)->None:
        with self._lock:
            self._priority = priority
            self.notify_observer("priority")

    def add_comment(self, comment: Comment)->None:
        self._comments.append(comment)
        self.add_log(f"Comment added by {comment.author.name}")
        self.notify_observer("comment")

    def add_subtask(self, subtask: 'Task')->None: 
        with self._lock:
            self._subtasks.append(subtask)
            self.add_log(f"Subtask added: {subtask.get_title()}")
            self.notify_observer("subtask_added")

    # state pattern
    def set_state(self, state: TaskState):
        self._current_state = state
        self.add_log(f"Status changes to: {state.get_status().value}")
        self.notify_observer("status")

    def start_progress(self)->None:
        self._current_state.complete_task(self)

    def complete_task(self):
        self._current_state.complete_task(self)
    
    def reopen_task(self):
        self._current_state.reopen_task(self)
    
    # observer pattern
    def add_observer(self, observer: TaskObserver)->None:
        self._observers.append(observer)

    def remove_observer(self, observer: TaskObserver)->None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observer(self, change_type: str)->None:
        for observer in self._observers:
            observer.update(self, change_type)

    def add_log(self, log_description: str)->None:
        self._activity_logs.append(ActivityLog(log_description))
    
    def is_composite(self)->bool:
        return len(self._subtasks) > 0
    
    def display(self, indent: str = "")->None:
        print(f"{indent}- {self._title} [{self.get_status().value}, {self._priority.value}, Due: {self._due_date}]")
        if self.is_composite():
            for subtask in self._subtasks:
                subtask.display(indent + " ")
        
    # Getters and setter
    def get_id(self)->str:
        return self._id
    
    def  get_title(self)->str:
        return self._title
    
    def get_description(self)->str:
        return self._description
    
    def get_priority(self)->Priority:
        return self._priority

    def get_due_date(self)->date:
        return self._due_date
    
    def get_assignee(self)->Optional[User]:
        return self._assignee

    def get_status(self)->TaskStatus:
        return self._current_state.get_status()

    def set_title(self, title: str)->None:
        self._title = title
    
    def set_description(self, descr: str)->None:
        self._description = descr