from Observer import Observer

class MobileApp(Observer):

    def __init__(self):
        self.name = "Mobile App"
        self.curr_price = 0.0

    def update(self, stock)->None:
        self.curr_price = stock.price
        self.reaction()

    def reaction(self)->None:
        print(f"MobileAPP: New stock price is: {self.curr_price}.")