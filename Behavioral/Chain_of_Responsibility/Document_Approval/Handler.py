from abc import ABC, abstractmethod
from Document import Document

class Handler(ABC):

    def __init__(self):
        self.next = None

    def next_handler(self, handler: "Handler"):
        self.next = handler

    @abstractmethod
    def approve(self, doc: Document):
        pass