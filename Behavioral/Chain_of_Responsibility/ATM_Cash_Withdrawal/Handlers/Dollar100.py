from Handler import Handler

class Dollar100(Handler):

    def __init__(self):
        self.next_handler = None
        self.no_of_notes = 0
    
    def set_next_handler(self, handler: Handler)->Handler:
        self.next_handler = handler
        return self.next_handler

    def withdraw(self, amount:float)->None:
        
        self.no_of_notes = amount // 100
        dispensable_amount = 100*self.no_of_notes
        amount_remaining = amount - dispensable_amount
        
        self.next_handler.withdraw(amount_remaining)

    def dispense(self)->None:
        if self.no_of_notes != 0:
            print(f"{self.no_of_notes} notes of 100 dollar dispensed")