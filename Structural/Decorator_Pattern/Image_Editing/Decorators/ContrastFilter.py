from filter import filter

class ContrastFilter(filter):
  
    def apply_filter(self):
        return self.img.click() + " *Contrast Edited!*"