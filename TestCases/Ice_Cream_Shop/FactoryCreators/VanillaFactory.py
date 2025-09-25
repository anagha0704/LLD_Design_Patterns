from BaseFactory import BaseFactory
from FactoryProducts.Vanilla import Vanilla

class VanillaFactory(BaseFactory):

    def pick_base(self):
        return Vanilla()