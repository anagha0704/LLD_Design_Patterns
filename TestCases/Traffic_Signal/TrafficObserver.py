from abc import ABC, abstractmethod
from Direction import Direction
from Signal import Signal

class TrafficObserver(ABC):

    @abstractmethod
    def update(self, intersection_id: int, direction: Direction, color: Signal)->None:
        pass

class CentralMonitor(TrafficObserver):

    def update(self, intersection_id: int, direction: Direction, color: Signal)->None:
        print(f"[MONITOR] Intersection {intersection_id}: Light for {direction.value} direction chnaged to {color.value}.")