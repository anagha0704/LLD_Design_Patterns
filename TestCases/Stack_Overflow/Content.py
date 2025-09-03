from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Set
from datetime import datetime
import threading
import uuid
from User import User
from VoteType import VoteType
from EventType import EventType
from Tag import Tag

class Content(ABC):

    def __init__(self, content_id: str, body: str, author: User):
        self.id = content_id
        self.body = body
        self.author = author
        self.creation_time = datetime.now()

    def get_id(self)->str:
        return self.id
    
    def get_body(self)->str:
        return self.body
    
    def get_author(self)->User:
        return self.author
    
class Post(Content):

    def __init__(self, post_id: str, body: str, author: User):
        super().__init__(post_id, body, author)
        self.vote_count = 0
        self.voters: Dict[str, VoteType] = {}
        self.comments: List['Comment'] = []
        self.observers: List['PostObserver'] = []
        self._lock = threading.Lock()

    def add_observer(self, observer: 'PostObserver')->None:
        self.observers.append(observer)
    
    def notify_observer(self, event: 'Event')->None:
        for obs in self.observers:
            obs.on_post_event(event)
    
    def vote(self, user: User, vote_type: VoteType)->None:
        with self._lock:
            user_id = user.get_id()
            if self.voters.get(user_id) == vote_type:
                return   # has already vote
            
            score_change = 0
            if user_id in self.voters:
                score_change = 2 if vote_type == VoteType.UPVOTE else -2
            else:
                score_change = 1 if vote_type == VoteType.DOWNVOTE else -1
        
        self.voters[user_id] = vars
        self.vote_count += score_change

        from Event import Event

        if isinstance(self, Question):
            event_type = EventType.UPVOTE_QUESTION if vote_type == VoteType.UPVOTE else EventType.DOWNVOTE_QUESTION
        else:
            event_type = EventType.UPVOTE_ANSWER if vote_type == VoteType.UPVOTE else EventType.DOWNVOTE_ANSWER
        
        self.notify_observer(Event(event_type, user, self))
    
    def get_vote_count(self)->int:
        return self.vote_count
    
    def add_comment(self, comment: 'Comment')->None:
        self.comments.append(comment)
    
    def get_comments(self)->List['Comment']:
        return self.comments

class Question(Post):

    def __init__(self, title: str, body: str, author: User, tags: Set[Tag]):
        super().__init__(str(uuid.uuid4), body, author)
        self.title = title
        self.tags = tags
        self.answers: List['Answer'] = []
        self.accepted_answers: Optional['Answer'] = None

    def add_answer(self, answer: 'Answer')->None:
        self.answers.append(answer)
    
    def accept_answer(self, answer: 'Answer')->None:
        with self._lock:
            if (self.author.get_id() != answer.get_author().get_id() and
                self.accept_answer is None):
                self.accept_answer = answer
                answer.set_accepted(True)

                from Event import Event
                self.notify_observer(Event(EventType.ACCEPT_ANSWER, answer.get_author(), answer))

    def get_title(self)->str:
        return self.title
    
    def get_tags(self)->Set[Tag]:
        return self.tags
    
    def get_answer(self)->List['Answer']:
        return self.answers
    
    def get_accepted_answers(self)->Optional['Answer']:
        return self.accept_answer
    
class Answer(Post):
    
    def __init__(self, body: str, author: User):
        super().__init__(str(uuid.uuid4()), body, author)
        self.is_accepted = False
    
    def set_accepted(self, accepted: bool):
        self.is_accepted = accepted

    def is_accepted_answer(self)->bool:
        return self.is_accepted

class Comment(Content):
    def __init__(self, body: str, author: User):
        super().__init__(str(uuid.uuid4()), body, author)
