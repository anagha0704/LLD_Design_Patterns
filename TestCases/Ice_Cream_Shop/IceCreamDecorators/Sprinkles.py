from Decorators import Decorators
from IceCream import IceCream

class Sprinkles(Decorators):

    def __init__(self, base: IceCream):
        super().__init__(base)
        self.cost = 0.5
    
    def describe(self) -> str:
        return self.base.describe() + ' and Sprinkles'

    def price(self) -> float:
        return self.base.price() + self.cost