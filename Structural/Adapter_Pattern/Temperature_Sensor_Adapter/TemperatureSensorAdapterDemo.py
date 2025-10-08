from TemperatureSensor import TemperatureSensor
from FahrenheitThermometer import FahrenheitThermometer
from FahrenheitToCelsiusAdapter import FahrenheitToCelsiusAdapter

class TemperatureSensorAdapterDemo:
    
    def run():
        celcius = TemperatureSensor(25.0)
        fahrenheit = FahrenheitThermometer(77.0)
        adapter = FahrenheitToCelsiusAdapter(fahrenheit)

        print(celcius.get_temperature())
        print(adapter.get_temperature())

if __name__ == "__main__":
    TemperatureSensorAdapterDemo.run()