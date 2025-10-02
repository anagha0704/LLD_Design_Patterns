from Handlers.Dollar10 import Dollar10
from Handlers.Dollar20 import Dollar20
from Handlers.Dollar50 import Dollar50
from Handlers.Dollar100 import Dollar100

class ATMCashWithdrawDemo:

    def run():
        dollar_100 = Dollar100()
        dollar_50 = Dollar50()
        dollar_20 = Dollar20()
        dollar_10 = Dollar10()

        dollar_100.set_next_handler(dollar_50)
        dollar_50.set_next_handler(dollar_20)
        dollar_20.set_next_handler(dollar_10)
        
        print("Enter the amount you would like to withdraw")
        amount = int(input())

        if amount % 10 != 0:
            raise ValueError("Machine can only dispense amount in multiples of 10!!")
        
        dollar_100.withdraw(amount)

        dollar_100.dispense()
        dollar_50.dispense()
        dollar_20.dispense()
        dollar_10.dispense()

if __name__ == "__main__":
    ATMCashWithdrawDemo.run()