class MealPlan:

    def __init__(self):
        self.entree = []
        self.sides = []
        self.drinks = []
        self.desserts = []
    
    def __str__(self):
        res = ""
        if self.entree:
            res += "Entree: " + f"{self.entree}"
        if self.sides:
            res += "\nSides: " + f"{self.sides}"
        if self.drinks:
            res += "\nDrinks: " + f"{self.drinks}"
        if self.desserts:
            res += "\nDesserts: " + f"{self.desserts}"
        return res