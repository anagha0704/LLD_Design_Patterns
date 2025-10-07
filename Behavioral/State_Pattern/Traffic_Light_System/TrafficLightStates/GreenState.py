from State import State

class GreenState(State):

    def display(self)->None:
        print("GREEN — Go!")

    def change(self)->State:
        from TrafficLightStates.YellowState import YellowState
        self.next = YellowState()
        return self.next