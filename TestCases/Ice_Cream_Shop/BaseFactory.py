from abc import ABC, abstractmethod

class BaseFactory(ABC):

    @abstractmethod
    def pick_base(self):
        pass