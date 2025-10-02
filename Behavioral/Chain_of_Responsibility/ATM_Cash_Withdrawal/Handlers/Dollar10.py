from Handler import Handler

class Dollar10(Handler):

    def __init__(self):
        self.next_handler = None
        self.no_of_notes = 0
    
    def set_next_handler(self, handler: Handler)->Handler:
        self.next_handler = handler
        return self.next_handler

    def withdraw(self, amount:float)->float:
        self.no_of_notes = amount // 10
        dispensable_amount = 10*self.no_of_notes
        amount_remaining = amount - dispensable_amount
            
        if amount_remaining == 0:
            print("Successful Withdrawal!!")
        else:
            print("Some Error in the Machine...need to revert operations")

    def dispense(self)->int:
        if self.no_of_notes != 0:
            print(f"{self.no_of_notes} notes of 10 dollar dispensed")