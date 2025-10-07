from Command import Command
from Account import Account

class DepositCommand(Command):

    def __init__(self, receiver: Account, amount: float):
        self.receiver = receiver
        self.amount = amount

    def execute(self)->None:
        self.receiver.deposit(self.amount)

    def rollback(self)->None:
        self.receiver.withdraw(self.amount)