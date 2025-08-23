from Car import Car

class PlainCar(Car):

    def __init__(self,  id: str, desc: str, price: float):
        self.id = id
        self.desc = desc
        self.price = price

    def get_description(self)->str:
        return self.desc

    def get_price(self)->float:
        return self.price