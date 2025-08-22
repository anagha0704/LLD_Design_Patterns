from DiscountStrategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):

    def __init__(self):
        self.disocunt = 10.0
    
    def apply_discount(self, price: float)->float:
        p = (price*self.disocunt)/100
        return (price - p)