from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self)->None:
        pass

    @abstractmethod
    def rollback(self)->None:
        pass