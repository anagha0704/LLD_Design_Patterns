from PlanBuilder import PlanBuilder

class MealPlanGeneratorDemo:
    
    def run():
        healthy_builder = PlanBuilder()

        healthy_plan = (healthy_builder
                        .add_entree("Chicken")
                        .add_drinks("Juice")
                        .add_sides("Soup")
                        .build())
    
        print(f"For Healthy options follow:") 
        print(f"{healthy_plan}")

if __name__ == "__main__":
    MealPlanGeneratorDemo.run()