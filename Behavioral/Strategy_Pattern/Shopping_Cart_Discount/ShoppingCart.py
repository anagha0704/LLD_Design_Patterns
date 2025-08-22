from DiscountStrategy import DiscountStrategy
from Item import Item

class ShoppingCart:
    
    def __init__(self):
        self.strategy = None
        self.items = []

    def setStrategy(self, strategy: DiscountStrategy)->None:
        self.strategy = strategy

    def calculate_discount(self, price: float)->float: 
        return self.strategy.apply_discount(price)
    
    def add_item(self, item: Item)->None:
        self.items.append(item)