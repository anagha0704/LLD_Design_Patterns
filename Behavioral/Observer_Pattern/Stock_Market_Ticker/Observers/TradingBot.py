from Observer import Observer
# reacts to price changes (e.g., prints “BUY” if price falls below threshold, “SELL” if it rises above).

class TradingBot(Observer):

    def __init__(self):
        self.name = "Trading Bot"
        self.threshold = 1.5
        self.suggest = ""

    def update(self, stock)->None:
        if stock.price < self.threshold:
            self.suggest = "BUY"
        elif stock.price > self.threshold:
            self.suggest = "SELL"
        else:
            raise ValueError("TradingBot: New price is same as threshold. You are good!")
        self.reaction()

    def reaction(self):
        print(f"TradingBot: As per the new prices, you should: {self.suggest}")