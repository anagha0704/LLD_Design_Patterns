from Command import Command
from Account import Account

class WithdrawCommand(Command):

    def  __init__(self, account: Account, amount: float):
        self.account = account
        self.amount = amount

    def execute(self)->None:
        self.account.withdraw(self.amount)

    def rollback(self)->None:
        self.account.deposit(self.amount)