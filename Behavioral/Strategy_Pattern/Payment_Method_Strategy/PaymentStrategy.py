from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    def pay(self, amount:float)->None:
        pass