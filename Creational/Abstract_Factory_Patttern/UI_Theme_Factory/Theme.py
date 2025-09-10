from abc import ABC, abstractmethod

class Theme(ABC):

    @abstractmethod
    def create_theme(self):
        pass