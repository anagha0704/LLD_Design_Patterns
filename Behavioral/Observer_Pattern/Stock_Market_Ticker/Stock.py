from StockData import StockData

class Stock:

    def __init__(self, name: str, price: float, stockdata: StockData):
        self.name = name
        self.price = price
        self.prev = None
        self.stockData = stockdata
    
    def price_change(self, price):
        if self.price != price:
            self.prev = self.price
            self.price = price
            self.stockData.notify(self)
        else:
            raise ValueError("Stock: Same price. No change!!")