from Item import Item

class Inventory:

    def __init__(self):
        self.stock = {} # "name":quantity
        self.items = {} # "name":Item
    
    def addItem(self, code: str, item: Item, quant: int):
        self.items[code] = item
        self.stock[code] = quant
    
    def reduceStock(self, code: str)->None:
        self.stock[code] = self.stock[code] - 1
    
    def getItem(self, code: str)->Item:
        return self.items[code]

    def isAvailable(self, code: str)->bool:
        if code in self.items:
            return True
        return False