from Image import Image

class BaseImage(Image):

    def __init__(self, filename: str):
        self.filename = filename

    def click(self)->str:
        return f"{self.filename} Image clicked!"