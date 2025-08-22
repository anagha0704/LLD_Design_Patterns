from abc import ABC, abstractmethod

class Format(ABC):

    def format(self, txt: str)->str:
        pass