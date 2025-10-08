from abc import ABC, abstractmethod

class CoffeeFactory(ABC):

    @abstractmethod
    def get_coffee(self)->str:
        pass