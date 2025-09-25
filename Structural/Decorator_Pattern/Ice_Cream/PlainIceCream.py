from IceCream import IceCream

class PlainIceCream(IceCream):

    def describe(self) -> str:
        return 'Plain Ice Cream'

    def price(self) -> float:
        return 2.0