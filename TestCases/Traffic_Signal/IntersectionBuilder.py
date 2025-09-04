from typing import List
from TrafficObserver import TrafficObserver
from IntersectionController import IntersectionController
from Direction import Direction
from TrafficLight import TrafficLight

class IntersectionBuilder:

    def __init__(self, intersection_id:int):
        self._id = intersection_id
        self._green_duration = 5000
        self._yellow_duration = 2000
        self._observers: List[TrafficObserver] = []

    def with_duration(self, green: int, yellow: int)-> 'IntersectionBuilder':
        self._green_duration = green
        self._yellow_duration = yellow
        return self

    def add_observer(self, observer: TrafficObserver)->'IntersectionBuilder':
        self._observers.append(observer)
        return self

    def build(self)->IntersectionController:
        lights = {}
        for d in Direction:
            light = TrafficLight(self._id, d)

            for observer in self._observers:
                light.add_observer(observer)
            lights[d] = light
        return IntersectionController(self._id, lights, self._green_duration, self._yellow_duration)