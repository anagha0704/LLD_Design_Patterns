from DiscountStrategy import DiscountStrategy

class FixedAmount(DiscountStrategy):

    def __init__(self):
        self.disocunt = 20
    
    def apply_discount(self, price: float)->float:
        return (price - self.disocunt)