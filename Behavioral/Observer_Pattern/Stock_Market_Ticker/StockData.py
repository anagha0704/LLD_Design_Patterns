from Observer import Observer

class StockData:

    def __init__(self):
        self.price = 0
        self.observers = []

    def subscribe(self, obs: Observer)->None:
        if obs not in self.observers:
            self.observers.append(obs)
        else:
            raise ValueError("StockData: You have already Subscribed!!")
        
    def unsubscribe(self, obs: Observer)->None:
        self.observers.remove(obs)
        print("StockData: Observer unsubscribed!!")

    def show_subscribers(self):
        print("StockData: Subscribed observers are: ")
        for ob in self.observers:
            print(ob.name)

    def notify(self, stock):
        print(f"StockData: Changes in price for {stock.name}")
        for obs in self.observers:
            obs.update(stock)