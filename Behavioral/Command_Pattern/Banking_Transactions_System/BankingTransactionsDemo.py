from Invoker import Invoker
from Account import Account
from BankingCommands.DepositCommand import DepositCommand
from BankingCommands.WithdrawCommand import WithdrawCommand
from BankingCommands.TransferCommand import TransferCommand

class BankingTransactionsDemo:

    def run():

        # Deposit $500 into Account A.
        # Withdraw $200 from Account A.
        # Transfer $100 from Account A to Account B.

        A = Account("A123", "ABC")
        B = Account("B123", "BCD")

        manager = Invoker()

        deposite = DepositCommand(A,500)
        withdraw = WithdrawCommand(A,200)
        transfer = TransferCommand(A,B,100)

        manager.set_command(deposite)
        manager.execute_command()

        manager.set_command(withdraw)
        manager.execute_command()

        manager.set_command(transfer)
        manager.execute_command()

        manager.rollback_last_command()
        manager.redo_command()

if __name__ == "__main__":
    BankingTransactionsDemo.run()