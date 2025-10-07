from Observer import Observer

class EmergencyResponseSystem(Observer):

    def update(self, state:str)->None:
        return f"Emergency Response System: Traffic Light changes to: {state}"