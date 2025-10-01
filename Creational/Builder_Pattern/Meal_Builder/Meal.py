class Meal:

    def __init__(self):
        self.mainItem = ""
        self.sideItem = ""
        self.drink = "" 
        self.dessert = ""
    
    def __str__(self):
        return f"{self.mainItem} + {self.sideItem} + {self.dessert} + {self.drink}"