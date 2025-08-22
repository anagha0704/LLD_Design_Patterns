from Observers.AnalyticsDashboard import AnalyticsDashboard
from Observers.MobileApp import MobileApp
from Observers.TradingBot import TradingBot
from StockData import StockData
from Stock import Stock

class StockMarketTickerDemo:
    def run():
        stock = StockData()
        
        s = Stock("TATA", 1.0, stock)
        bot = TradingBot()
        mobile = MobileApp()
        dashboard = AnalyticsDashboard()

        stock.subscribe(bot)
        stock.subscribe(mobile)
        stock.subscribe(dashboard)

        s.price_change(5.0)

        # stock.unsubscribe(mobile)
        stock.show_subscribers()

        s.price_change(20)

if __name__ == "__main__":
    StockMarketTickerDemo.run()