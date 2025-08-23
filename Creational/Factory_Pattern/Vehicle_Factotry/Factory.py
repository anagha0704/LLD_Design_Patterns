from abc import ABC, abstractmethod
from Vehicle import Vehicle

class Factory(ABC):

    @abstractmethod
    def request_vehicle(self)->Vehicle:
        pass