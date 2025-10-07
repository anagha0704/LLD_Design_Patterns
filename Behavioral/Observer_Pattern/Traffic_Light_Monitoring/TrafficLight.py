from typing import List
from Observer import Observer

class TrafficLight:

    def __init__(self):
        self.state = None
        self.observers = []

    def add_observers(self, o: Observer)->None:
        print("TrafficLight: Observer added!!")
        self.observers.append(o)

    def remove_observer(self, o: Observer)->None:
        self.observers.remove(o)
        print("TrafficLight: Observer removed!!")

    def change_state(self, state: str)->None:
        self.state = state
        print(f"TrafficLight: Light turned to {state}")
        for o in self.observers:
            print(o.update(state))