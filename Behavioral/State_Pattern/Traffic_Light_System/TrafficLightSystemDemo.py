from TrafficLight import TrafficLight

class TrafficLightSystemDemo:

    def run():
        light = TrafficLight()

        light.display() # Red
        light.change() 
        light.display() # Green
        light.change()
        light.display() # Yellow
        light.change()
        light.display() # Red

if __name__ == "__main__":
    TrafficLightSystemDemo.run()