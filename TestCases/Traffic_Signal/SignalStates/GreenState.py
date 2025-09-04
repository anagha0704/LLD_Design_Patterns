from SignalState import SignalState
from Signal import Signal

class GreenState(SignalState):

    def handle(self,  context: 'TrafficLight')->None:
        context.set_color(Signal.GREEN)
        from SignalStates.YellowState import YellowState
        context.set_next_state(YellowState())