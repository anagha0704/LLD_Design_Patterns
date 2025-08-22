from Format import Format

class Capitalize(Format):

    def format(self, txt: str)-> str:
        if len(txt) > 0:
            return txt.capitalize()
        else:
            raise ValueError("Empty String!!")