from Format import Format

class LowerCase(Format):

    def format(self, txt: str)-> str:
        if len(txt) > 0:
            return txt.lower()
        else:
            raise ValueError("Empty String!!")