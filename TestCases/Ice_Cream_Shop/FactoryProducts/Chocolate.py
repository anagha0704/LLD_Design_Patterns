from IceCream import IceCream

class Chocolate(IceCream):

    def describe(self) -> str:
        return 'Chocolate Ice Cream'

    def price(self) -> float:
        return 2.0