from CoffeeFactory import CoffeeFactory
from CoffeeTypes.Latte import Latte

class LatteFactory(CoffeeFactory):

    def __init__(self):
        self.coffee = Latte()

    def get_coffee(self)->str:
        print(self.coffee.prepare())