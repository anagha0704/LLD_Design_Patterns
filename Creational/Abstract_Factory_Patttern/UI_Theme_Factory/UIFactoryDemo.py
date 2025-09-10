from Factories.LightFactory import LightFactory
from Factories.DarkFactory import DarkFactory

class UIFactoryDemo:
    
    def run():

        # creating dark button
        factory1 = DarkFactory()
        theme1 = factory1.create_theme()
        button1 = factory1.create_button()
        box1 = factory1.create_checkbox()
        theme1.create_theme()
        button1.create_shape()
        box1.create_shape()

        # creating light checkbox
        factory2 = LightFactory()
        theme2 = factory2.create_theme()
        button2 = factory2.create_button()
        box2 = factory2.create_checkbox()
        theme2.create_theme()
        button2.create_shape()
        box2.create_shape()

if __name__ == "__main__":
    UIFactoryDemo.run()