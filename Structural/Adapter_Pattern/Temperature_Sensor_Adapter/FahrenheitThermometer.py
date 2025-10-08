class FahrenheitThermometer:

    def __init__(self, temp: float):
        self.temp_f = temp

    def get_temperature_f(self)->str:
        return self.temp_f