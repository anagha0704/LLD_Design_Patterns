from Meal import Meal

class Builder:

    def __init__(self):
        self.meal = Meal()
        
    def withMainItem(self, item: str):
        self.meal.mainItem = item
        return self

    def withSideItem(self, item: str):
        self.meal.sideItem = item
        return self

    def withDrink(self, item: str):
        self.meal.drink = item
        return self
    
    def withDessert(self, item: str):
        self.meal.dessert = item
        return self

    def build(self):
        return self.meal