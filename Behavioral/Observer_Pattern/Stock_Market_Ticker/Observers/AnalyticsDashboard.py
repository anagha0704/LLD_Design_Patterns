from Observer import Observer
# shows percentage changes in stock prices.

class AnalyticsDashboard(Observer):

    def __init__(self):
        self.name = "Dashboard"
        self.percentage_change = 0

    def update(self, stock)->None:
        if stock.prev is not None:
            self.percentage_change = round((abs(stock.price - stock.prev)/stock.prev)*100, 2)
            self.reaction()
        else:
            print("AnalyticsDashboard: First update, no previous price to compare.")

    def reaction(self):
        print(f"AnalyticsDashboard: Percentage change in stock price is: {self.percentage_change}%")