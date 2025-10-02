from TravelBookingFacade import TravelBookingFacade

class TravelBookingDemo:

    def run():
        system = TravelBookingFacade()
        print(system.book_itenary("New York", "Dallas", "Economy", "Hilton", "Regular", 2, "Sedan", 2))

if __name__ == "__main__":
    TravelBookingDemo.run()