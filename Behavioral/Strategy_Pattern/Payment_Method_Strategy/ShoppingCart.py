from PaymentStrategy import PaymentStrategy

class ShoppingCart:

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: PaymentStrategy)->None:
        self.strategy = strategy
    
    def get_strategy(self)->PaymentStrategy:
        return self.strategy
    
    def make_payment(self, amount:float)->None:
        strategy = self.get_strategy()
        print(strategy.pay(amount))