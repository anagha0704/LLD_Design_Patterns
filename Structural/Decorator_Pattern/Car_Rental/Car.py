from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def get_description(self)->str:
        pass

    @abstractmethod
    def get_price(self)->float:
        pass