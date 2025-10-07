from Observer import Observer

class TrafficDataLogger(Observer):

    def update(self, state:str)->None:
        return f"Traffic Logger: Traffic Light changes to: {state}"