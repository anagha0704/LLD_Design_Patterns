from BaseFactory import BaseFactory
from FactoryProducts.Chocolate import Chocolate

class ChocolateFactory(BaseFactory):

    def pick_base(self):
        return Chocolate()