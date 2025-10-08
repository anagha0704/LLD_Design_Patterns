from abc import ABC, abstractmethod

class Target(ABC):

    @abstractmethod
    def get_temperature(self)->str:
        pass