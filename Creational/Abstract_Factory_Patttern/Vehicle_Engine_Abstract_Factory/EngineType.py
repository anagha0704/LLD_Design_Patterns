from abc import ABC, abstractmethod

class EngineType(ABC):

    @abstractmethod
    def start(self):
        pass