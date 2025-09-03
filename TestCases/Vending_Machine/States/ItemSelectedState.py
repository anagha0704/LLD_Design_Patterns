from VendingMachineState import VendingMachineState

class ItemSelectedState(VendingMachineState):

    def select_item(self, code: str)->None:
        print(f"Item Selected State: Item has been already selected! Insert money..")

    def insert_money(self, coin: "Coin")->None:
        self.machine.addBalance(coin.get_value())
        print(f"Item Selected State: Coin inserted: {coin.get_value()}¢ ({coin.name})")
        
        selected_item = self.machine.get_selected_item()
        if selected_item and self.machine.get_balance() >= selected_item.get_price():
            print("Item Selected State: Sufficient money received.")
            # Import here to avoid circular dependency
            from States.HasMoneyState import HasMoneyState
            self.machine.set_state(HasMoneyState(self.machine))

    def dispensing_item(self)->None:
        print("Item Selected State: Insert money to Dispense Item!")

    def refund(self)->None:
        print("Item Selected State: Insert money before asking for refund!")