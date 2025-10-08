from CoffeeFactory import CoffeeFactory
from CoffeeTypes.Cappuccino import Cappuccino

class CappuccinoFactory(CoffeeFactory):

    def __init__(self):
        self.coffee = Cappuccino()

    def get_coffee(self)->str:
        print(self.coffee.prepare())