from abc import ABC, abstractmethod

class VehicleType(ABC):

    @abstractmethod
    def deliver(self):
        pass