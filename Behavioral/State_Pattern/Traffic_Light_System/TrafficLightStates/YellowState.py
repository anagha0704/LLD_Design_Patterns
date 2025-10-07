from State import State

class YellowState(State):

    def display(self)->None:
        print("YELLOW — Slow!")

    def change(self)->State:
        from TrafficLightStates.RedState import RedState
        self.next = RedState()
        return self.next