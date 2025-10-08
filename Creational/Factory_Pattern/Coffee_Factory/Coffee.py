from abc import ABC, abstractmethod

class Coffee(ABC):

    @abstractmethod
    def prepare(self)->str:
        pass