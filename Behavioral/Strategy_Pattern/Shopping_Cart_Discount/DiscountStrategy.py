from abc import ABC, abstractmethod

class DiscountStrategy(ABC):

    def apply_discount(self, price)->float:
        pass
    