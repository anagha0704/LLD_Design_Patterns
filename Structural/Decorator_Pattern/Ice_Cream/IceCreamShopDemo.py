from PlainIceCream import PlainIceCream
from IceCreamDecorators.ChocolateSyrup import ChocolateSyrup
from IceCreamDecorators.Nuts import Nuts
from IceCreamDecorators.Caramel import Caramel
from IceCreamDecorators.Sprinkles import Sprinkles
from IceCreamDecorators.WhippedCream import WhippedCream

class IceCreamShopDemo:

    def run():
        base = PlainIceCream()

        choco = ChocolateSyrup(base)
        nuts = Nuts(choco)
        caramel = Caramel(nuts)
        sprinkle = Sprinkles(caramel)
        cream = WhippedCream(sprinkle)

        print('Your order is:')
        print(cream.describe())
        print('Your total is:')
        print(cream.price())

if __name__ == "__main__":
    IceCreamShopDemo.run()