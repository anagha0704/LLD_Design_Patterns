from abc import ABC, abstractmethod

class Builder(ABC):

    @abstractmethod
    def add_entree(self, entr: str):
        pass

    @abstractmethod
    def add_sides(self, side: str):
        pass

    @abstractmethod
    def add_drinks(self, drink: str):
        pass

    @abstractmethod
    def add_desserts(self, dessert: str):
        pass

    @abstractmethod
    def build(self):
        pass