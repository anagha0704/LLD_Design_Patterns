from CoffeeFactory import CoffeeFactory
from CoffeeTypes.Espresso import Espresso

class EspressoFactory(CoffeeFactory):

    def __init__(self):
        self.coffee = Espresso()

    def get_coffee(self)->str:
        print(self.coffee.prepare())