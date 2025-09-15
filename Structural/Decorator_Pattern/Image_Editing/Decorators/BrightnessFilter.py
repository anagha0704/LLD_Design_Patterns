from filter import filter

class BrightnessFilter(filter):

    def apply_filter(self):
        return self.img.click() + " *Brightness Edited!*"