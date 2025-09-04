from SignalState import SignalState
from Signal import Signal

class RedState(SignalState):

    def handle(self,  context: 'TrafficLight')->None:
        context.set_color(Signal.RED)
        context.set_next_state(RedState())