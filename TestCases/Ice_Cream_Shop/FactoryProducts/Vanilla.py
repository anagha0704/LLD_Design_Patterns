from IceCream import IceCream

class Vanilla(IceCream):

    def describe(self) -> str:
        return 'Vanilla Ice Cream'

    def price(self) -> float:
        return 1.5