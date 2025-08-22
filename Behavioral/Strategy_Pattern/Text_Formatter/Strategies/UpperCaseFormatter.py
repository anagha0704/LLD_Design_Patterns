from Format import Format

class UpperCase(Format):

    def format(self, txt: str)-> str:
        if len(txt) > 0:
            return txt.upper()
        else:
            raise ValueError("Empty String!!")