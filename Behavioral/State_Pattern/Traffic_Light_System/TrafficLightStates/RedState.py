from State import State

class RedState(State):

    def display(self)->None:
        print("RED — Stop!")

    def change(self)->State:
        from TrafficLightStates.GreenState import GreenState
        self.next = GreenState()
        return self.next