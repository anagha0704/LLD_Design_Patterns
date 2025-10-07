from Command import Command
from Account import Account

class TransferCommand(Command):

    def __init__(self, sender: Account, receiver: Account, amount: float):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def execute(self)->None:
        self.sender.withdraw(self.amount)
        self.receiver.deposit(self.amount)

    def rollback(self)->None:
        self.receiver.withdraw(self.amount)
        self.sender.deposit(self.amount)