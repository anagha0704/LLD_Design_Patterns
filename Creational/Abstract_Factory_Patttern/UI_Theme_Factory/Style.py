from abc import ABC, abstractmethod

class Style(ABC):

    @abstractmethod
    def create_shape(self):
        pass