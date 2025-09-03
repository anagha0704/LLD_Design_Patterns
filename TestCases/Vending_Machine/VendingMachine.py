from Inventory import Inventory
from Item import Item

class VendingMachine:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VendingMachine, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            from States.IdleState import IdleState
            self.curr_state = IdleState(self)
            self.inventory = Inventory()
            self.balance = 0
            self.selectedItemCode = None
    
    def addItem(self, code: str, name: str, price: float, quantity: int)->Item:
        item = Item(code, name, price)
        self.inventory.addItem(code, item, quantity)
        return item

    def select_item(self, code: str)->None:
        if self.inventory.isAvailable(code):
            self.selectedItemCode = code
            self.curr_state.select_item(code)
        else:
            raise Exception("Vending Machine: Sorry, Item not available in inventory!!")

    def insert_money(self, coin: "Coin")->None:
        self.curr_state.insert_money(coin)

    def dispense(self)->None:
        self.curr_state.dispensing_item()

    def dispensing_item(self)->None:
        item = self.inventory.getItem(self.selectedItemCode)
        if self.balance >= item.get_price():
            self.inventory.reduceStock(item.code)
            self.balance -= item.get_price()
            print(f"Vending Machine: Dispensed: {item.get_name()}")
            if self.balance > 0:
                print(f"vending Machine: Returning change: {self.balance}")
            self.reset()
            from States.IdleState import IdleState
            self.set_state(IdleState(self))
        else:
            raise Exception("Vending Machine: Sorry, Selected Item price is higher than your inserted money!!")

    def refund(self)->None:
        print(f"Vending Machine: Refunding: {self.balance}")
        self.balance = 0
    
    def get_selected_item(self)->"Item":
        return self.inventory.getItem(self.selectedItemCode)

    def reset(self)->None:
        self.selectedItemCode = None
        self.balance = 0

    def set_state(self, state)->None:
        self.curr_state = state
    
    def addBalance(self, balance: float)->None:
        self.balance += balance
    
    def setSelectedItemCode(self, code: str)->None:
        self.selectedItemCode = code

    def get_balance(self) -> float:
        return self.balance