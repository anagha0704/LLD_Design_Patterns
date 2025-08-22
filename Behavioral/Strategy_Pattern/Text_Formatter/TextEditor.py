from Format import Format

class TextEditor:

    def __init__(self):
        self.strategy = None
    
    def set_strategy(self, strategy: Format)->None:
        self.strategy = strategy
    
    def format_it(self, txt: str)->str:
        return self.strategy.format(txt)