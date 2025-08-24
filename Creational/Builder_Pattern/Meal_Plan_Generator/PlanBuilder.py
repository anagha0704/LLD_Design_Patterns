from Builder import Builder
from MealPlan import MealPlan

class PlanBuilder(Builder):

    def __init__(self):
        self.plan = MealPlan()

    def add_entree(self, entr: str)->Builder:
        self.plan.entree.append(entr)
        return self

    def add_sides(self, side: str)->Builder:
        self.plan.sides.append(side)
        return self

    def add_drinks(self, drink: str)->Builder:
        self.plan.drinks.append(drink)
        return self

    def add_desserts(self, dessert: str)->Builder:
        self.plan.desserts.append(dessert)
        return self

    def build(self)->MealPlan:
        return self.plan