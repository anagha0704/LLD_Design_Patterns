from filter import filter

class WatermarkFilter(filter):

    def apply_filter(self):
        return self.img.click() + " *Watermark Edited!*"