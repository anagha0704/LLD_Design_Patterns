from VendingMachineState import VendingMachineState

class HasMoneyState(VendingMachineState):

    def select_item(self, code: str)->None:
        print(f"Has Money State: Item has been selected and money is received. Item can be Dispensed")

    def insert_money(self, coin: "Coin")->None:
        print(f"Has Money State: Already Inserted!!")

    def dispensing_item(self)->None:
        from States.DispensingState import DispensingState
        self.machine.set_state(DispensingState(self.machine))
        self.machine.dispensing_item()
    
    def refund(self):
        self.machine.refund()
        self.machine.reset()
        # Import here to avoid circular dependency
        from States.IdleState import IdleState
        self.machine.set_state(IdleState(self.machine))