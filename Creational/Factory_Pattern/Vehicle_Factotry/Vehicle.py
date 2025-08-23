from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def deliver(self)->None:
        pass