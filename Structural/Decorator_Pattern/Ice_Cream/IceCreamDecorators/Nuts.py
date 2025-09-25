from Decorators import Decorators
from IceCream import IceCream

class Nuts(Decorators):

    def __init__(self, base: IceCream):
        self.base = base
        self.cost = 1
    
    def describe(self) -> str:
        return self.base.describe() + ' and Nuts'

    def price(self) -> float:
        return self.base.price() + self.cost