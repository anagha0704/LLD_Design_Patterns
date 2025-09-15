from abc import abstractmethod
from Image import Image

class filter(Image):

    def __init__(self, img: Image):
        self.img = img

    def click(self):
        return self.apply_filter()

    @abstractmethod
    def apply_filter(self):
        pass