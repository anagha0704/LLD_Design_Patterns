from Handler import Handler

class Dollar50(Handler):

    def __init__(self):
        self.next_handler = None
        self.no_of_notes = 0
    
    def set_next_handler(self, handler: Handler)->Handler:
        self.next_handler = handler
        return self.next_handler

    def withdraw(self, amount:float)->float:
        
        self.no_of_notes = amount // 50
        dispensable_amount = 50*self.no_of_notes
        amount_remaining = amount - dispensable_amount

        self.next_handler.withdraw(amount_remaining)

    def dispense(self)->int:
        if self.no_of_notes != 0:
            print(f"{self.no_of_notes} notes of 50 dollar dispensed")