from typing import List
from Direction import Direction
from Signal import Signal
from TrafficObserver import TrafficObserver
from SignalState import SignalState
from SignalStates.RedState import RedState

class TrafficLight:

    def __init__(self, intersection_id: int, direction: Direction):
        self._intersection_id = intersection_id
        self._direction = direction
        self._curr_color = None
        self._curr_state = RedState()
        self._next_state = None
        self._observers: List[TrafficObserver] = []
        self._curr_state.handle(self)

    def start_green(self)->None:
        self._curr_state = self._next_state
        self._curr_state.handle(self)
    
    def transition(self)->None:
        self._curr_state = self._next_state
        self._curr_state.handle(self)
    
    def set_color(self, color: Signal)->None:
        if self._curr_color != color:
            self._curr_color = color
            self._notify_observers()
    
    def set_next_state(self, state: SignalState)->None:
        self._next_state = state

    def get_current_color(self)->Signal:
        return self._curr_color

    def get_direction(self)->Direction:
        return self._direction

    def add_observer(self, observer: TrafficObserver)->None:
        self._observers.append(observer)
    
    def remove_observer(self, observer: TrafficObserver)->None:
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._intersection_id, self._direction, self._curr_color)