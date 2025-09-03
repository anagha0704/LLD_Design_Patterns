from VendingMachineState import VendingMachineState

class DispensingState(VendingMachineState):

    def select_item(self, code: str):
        print(f"Dispensing State: Item has been selected and money is received. Item can be Dispensed")

    def insert_money(self, coin: "Coin"):
        print(f"Dispensing State: Waiting for Dispensing. Cannot onsert money now!!")

    def dispensing_item(self):
        # Already triggered by HasMoneyState
        print("Dispensing in progress...")
    
    def refund(self):
        print("Dispensing in progress. Refund not allowed.")