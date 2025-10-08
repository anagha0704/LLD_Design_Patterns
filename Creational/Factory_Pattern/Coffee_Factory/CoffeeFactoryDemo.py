from Factories.CappuccinoFactory import CappuccinoFactory
from Factories.EspressoFactory import EspressoFactory
from Factories.LatteFactory import LatteFactory

class CoffeeFactoryDemo:
    
    def run():
        print("Enter coffee type")
        type = input()
        
        if type == "latte":
           factory = LatteFactory()
        elif type == "espresso":
           factory = EspressoFactory()
        elif type == "cappuccino":
           factory = CappuccinoFactory()
        else:
            raise ValueError("Invalid coffee type")

        factory.get_coffee()

if __name__ == "__main__":
    CoffeeFactoryDemo.run()