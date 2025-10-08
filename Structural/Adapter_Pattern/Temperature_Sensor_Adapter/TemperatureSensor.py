from Target import Target

class TemperatureSensor(Target):

    def __init__(self, temp: float):
        self.temp = temp

    def get_temperature(self)->str:
        return f"Celsius Sensor Reading: {self.temp}"