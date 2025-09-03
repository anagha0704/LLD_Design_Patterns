from enum import Enum

class EnumSignleton(Enum):

    INSTANCE = 1

    def some_method(self):
        return "I am some method on singleton"

if __name__ == "__main__":

    s1 = EnumSignleton.INSTANCE
    s2 = EnumSignleton.INSTANCE
    print(s1 is s2)