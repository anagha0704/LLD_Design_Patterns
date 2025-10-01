from Builder import Builder

class MealBuilder:

    def run():

        builder = Builder()

        meal = (builder.withMainItem("Burger").withSideItem("Fries").withDessert("Pie").withDrink("Coke").build())
        print("your order is:", meal)

if __name__ == "__main__":
    MealBuilder.run()