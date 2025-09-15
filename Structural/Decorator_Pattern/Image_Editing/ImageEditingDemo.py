from BaseImage import BaseImage
from Decorators.BrightnessFilter import BrightnessFilter
from Decorators.ContrastFilter import ContrastFilter
from Decorators.GrayscaleFilter import GrayscaleFilter
from Decorators.WatermarkDecorator import WatermarkFilter

class ImageEditingDemo:

    def run():
        img = BaseImage("my_photo.png")
        
        bf = BrightnessFilter(img)

        cf = ContrastFilter(bf)

        gf = GrayscaleFilter(cf)

        wf = WatermarkFilter(gf)
        
        print(wf.apply_filter())

if __name__ == "__main__":
    ImageEditingDemo.run()