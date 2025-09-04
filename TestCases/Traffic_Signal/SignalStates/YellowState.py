from SignalState import SignalState
from Signal import Signal
from SignalStates.RedState import RedState

class YellowState(SignalState):

    def handle(self,  context: 'TrafficLight')->None:
        context.set_color(Signal.YELLOW)
        context.set_next_state(RedState())