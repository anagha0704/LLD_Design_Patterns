from Target import Target
from FahrenheitThermometer import FahrenheitThermometer

class FahrenheitToCelsiusAdapter(Target):

    def __init__(self, adaptee: FahrenheitThermometer):
        self.adaptee = adaptee

    def get_temperature(self)->str:
        temp = (self.adaptee.get_temperature_f()-32)/1.8
        return f"Fahrenheit Sensor Reading (converted): {temp}"