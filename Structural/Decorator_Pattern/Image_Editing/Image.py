from abc import ABC, abstractmethod

class Image(ABC):

    @abstractmethod
    def click(self)->str:
        pass