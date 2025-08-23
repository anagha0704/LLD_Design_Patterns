from Car import Car
from Feature import Feature

class InsuranceCoverage(Feature):

    def __init__(self, feature: Feature, price: float, ):
        super().__init__(feature)
        self.price = price
        self.desc = ' + Insurance Coveraage'

    def get_description(self)->str:
        return super().get_description() + self.desc
    
    def get_price(self)->float:
        return super().get_price() + self.price