# A plain car costs $50/day.

# Adding GPS makes it $65/day.

# Adding GPS + Insurance makes it $95/day.

from PlainCar import PlainCar
from Decorators.ChildSafety import ChildSafety
from Decorators.GPSNavigation import GPSNavigation
from Decorators.InsuranceCoverage import InsuranceCoverage
from Decorators.RoadsideAssistance import RoadsideAssistance

class CarRentalDemo:

    def run():
        car = PlainCar("C1", "Customer has rented a Car", 50.0)

        gps = GPSNavigation(car, 15)

        insurance = InsuranceCoverage(gps, 30)

        road_side = RoadsideAssistance(insurance, 40)

        print(road_side.get_description())
        print(road_side.get_price())

if __name__ == "__main__":

    CarRentalDemo.run()