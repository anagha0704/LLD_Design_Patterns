from Observer import Observer

class CentralTrafficController(Observer):

    def update(self, state:str)->None:
        return f"CentralTrafficController: Traffic Light changes to: {state}"