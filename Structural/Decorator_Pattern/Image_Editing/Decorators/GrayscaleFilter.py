from filter import filter

class GrayscaleFilter(filter):

    def apply_filter(self):
        return self.img.click() + " *Contrast Edited!*"