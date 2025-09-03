from abc import ABC, abstractmethod
from VendingMachine import VendingMachine

class VendingMachineState(ABC):

    def __init__(self, machine: VendingMachine):
        self.machine = machine

    @abstractmethod
    def select_item(self, code: str)->None:
        pass

    @abstractmethod
    def insert_money(self, coin: "Coin")->None:
        pass

    @abstractmethod
    def dispensing_item(self)->None:
        pass

    @abstractmethod
    def refund(self)->None:
        pass