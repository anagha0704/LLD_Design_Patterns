from Decorators import Decorators
from IceCream import IceCream

class WhippedCream(Decorators):

    def __init__(self, base: IceCream):
        self.base = base
        self.cost = 0.2
    
    def describe(self) -> str:
        return self.base.describe() + ' and Whipped Cream'

    def price(self) -> float:
        return self.base.price() + self.cost