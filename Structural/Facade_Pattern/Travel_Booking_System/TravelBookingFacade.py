from Subsystems.CarBooking import CarBooking
from Subsystems.HotelBooking import HotelBooking
from Subsystems.FlightBooking import FlightBooking

class TravelBookingFacade:

    def __init__(self):
        self.booking_car = CarBooking()
        self.booking_hotel = HotelBooking()
        self.booking_flight = FlightBooking()

    def book_itenary(self, origin, destination, flight_class, hotel_name, room_type, nights, car_type, rental_days):
        flight_info = self.booking_flight.book(origin, destination, flight_class)
        hotel_info = self.booking_hotel.book(hotel_name, room_type, nights)
        car_info = self.booking_car.book(car_type, rental_days)

        print(flight_info)
        print(hotel_info)
        print(car_info)
        return f"flight: , {flight_info}, hotel: , {hotel_info}, car: , {car_info}"