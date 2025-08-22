from DiscountStrategy import DiscountStrategy

class NoDiscount(DiscountStrategy):

    def __init__(self):
        self.disocunt = 0
    
    def apply_discount(self, price: float)->float:
        return price