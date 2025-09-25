from FactoryCreators.ChocolateFactory import ChocolateFactory
from FactoryCreators.StrawberryFactory import StrawberryFactory
from FactoryCreators.VanillaFactory import VanillaFactory
from IceCreamDecorators.ChocolateSyrup import ChocolateSyrup
from IceCreamDecorators.Nuts import Nuts
from IceCreamDecorators.Caramel import Caramel
from IceCreamDecorators.Sprinkles import Sprinkles
from IceCreamDecorators.WhippedCream import WhippedCream

class IceCreamShopDemo:

    def build_order(self, base_factory):
        base = base_factory.pick_base()
        return WhippedCream(Sprinkles(Caramel(Nuts(ChocolateSyrup(base)))))


    def run(self):
        for factory in [ChocolateFactory(), VanillaFactory(), StrawberryFactory()]:
            icecream = self.build_order(factory)
            print('Your order is:')
            print(icecream.describe())
            print('Your total is:')
            print(icecream.price())
            print()

if __name__ == "__main__":
    demo = IceCreamShopDemo()
    demo.run()