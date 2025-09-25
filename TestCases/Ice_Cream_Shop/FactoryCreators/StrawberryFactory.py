from BaseFactory import BaseFactory
from FactoryProducts.Strawberry import Strawberry

class StrawberryFactory(BaseFactory):

    def pick_base(self):
        return Strawberry()