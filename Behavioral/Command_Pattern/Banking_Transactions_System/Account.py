class Account:

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.balance = 0
    
    def deposit(self, amount: float)->None:
        self.balance += amount
        print(f"Amount deposited in account of {self.name} sucessfully!!")
    
    def withdraw(self, amount: float)->None:
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount withdrawn from the account of {self.name}!!")
        else:
            raise ValueError("Insufficient Balance!")