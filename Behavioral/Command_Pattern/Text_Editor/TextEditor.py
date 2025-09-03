class TextEditor:

    def __init__(self):
        self.content = "" 
        self.clipboard = ""

    def write(self, txt):
        self.content += txt
        print(f"Text Editor: Current text-> '{self.content}'")
    
    def delete(self, count):
        delted = self.content[-count:] if count <= len(self.content) else self.content
        self.content = self.content[:-count]
        print(f"Text Editor: {delted}, current text -> '{self.content}")
        return delted

    def copy(self, start, end):
        self.clipboard = self.content[start:end+1]
        print(f"Text Editor: Copied '{self.clipboard}'")

    def paste(self):
        self.content += self.clipboard
        print(f"Text Editor: '{self.clipboard}', Current content: {self.content}")