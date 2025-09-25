from abc import ABC, abstractmethod

class IceCream(ABC):

    @abstractmethod
    def describe(self)->str:
        pass

    @abstractmethod
    def price(self)->float:
        pass