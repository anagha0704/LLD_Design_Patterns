from VendingMachineState import VendingMachineState

class IdleState(VendingMachineState):

    def select_item(self, code: str)->None:
        from States.ItemSelectedState import ItemSelectedState
        self.machine.set_state(ItemSelectedState(self.machine))
        print(f"Item selected: {code}")

    def insert_money(self, coin: "Coin")->None:
        print(f"Idle State: Select Item before inserting money!")

    def dispensing_item(self)->None:
        print("Idle State: Select Item to dispense!")

    def refund(self)->None:
        print("Idle State: Select Item and insert money before asking for refund!")