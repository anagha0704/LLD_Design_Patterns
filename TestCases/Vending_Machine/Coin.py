from enum import Enum

class Coin(Enum):

    PENNY = 1
    NICKEL = 5
    QUARTER = 25
    DIME = 10

    def get_value(self) -> int:
        return self.value