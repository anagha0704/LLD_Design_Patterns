from Decorators import Decorators
from IceCream import IceCream

class Caramel(Decorators):

    def __init__(self, base: IceCream):
        self.base = base
        self.cost = 0.6
    
    def describe(self) -> str:
        return self.base.describe() + ' and Caramel'

    def price(self) -> float:
        return self.base.price() + self.cost