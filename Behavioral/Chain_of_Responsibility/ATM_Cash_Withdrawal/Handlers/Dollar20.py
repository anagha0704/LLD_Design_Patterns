from Handler import Handler

class Dollar20(Handler):

    def __init__(self):
        self.next_handler = None
        self.no_of_notes = 0
    
    def set_next_handler(self, handler: Handler)->Handler:
        self.next_handler = handler
        return self.next_handler

    def withdraw(self, amount:float)->float:
        
        self.no_of_notes = amount // 20
        dispensable_amount = 20*self.no_of_notes
        amount_remaining = amount - dispensable_amount

        self.next_handler.withdraw(amount_remaining)

    def dispense(self)->int:
        if self.no_of_notes != 0:
            print(f"{self.no_of_notes} notes of 20 dollar dispensed")