class TrafficLight:

    def __init__(self):
        from TrafficLightStates.RedState import RedState
        self.curr_state = RedState()
    
    def display(self)->None:
        self.curr_state.display()
    
    def change(self)->None:
        self.curr_state = self.curr_state.change()