from DiscountStrategy import DiscountStrategy

class Item:

    def __init__(self, name: str, price: float, strategy: DiscountStrategy):
        self.name = name
        self.price = price
        self.discountStrategy = strategy