from typing import Dict
import threading
from Direction import Direction
from Signal import Signal
from TrafficLight import TrafficLight
from IntersectionState import IntersectionState
from States.NorthSouthGreenState import NorthSouthGreenState

class IntersectionController:

    def __init__(self, intercetion_id: int, traffic_lights: Dict[Direction, TrafficLight], 
                 green_duration: int, yellow_duration: int):
        self._id = intercetion_id
        self._traffic_lights = traffic_lights
        self._green_duration = green_duration
        self._yellow_duration = yellow_duration
        self._curr_state = NorthSouthGreenState()
        self._running = True
    
    def get_id(self)->int:
        return self._id
    
    def get_green_duration(self)->int:
        return self._green_duration
    
    def get_yellow_duration(self)->int:
        return self._yellow_duration
    
    def get_light(self, direction: Direction)->int:
        return self._traffic_lights[direction]
    
    def set_state(self, state: IntersectionState):
        self._curr_state = state

    def start(self)->None:
        thread = threading.Thread(target=self.run())
        thread.start()
    
    def stop(self)->None:
        self._running = False

    def run(self)->None:
        while self._running:
            try:
                self._curr_state.handle(self)
            except Exception as e:
                print(f"Intersection {self._id} encountered an error: {e}")
                self._running = False
    