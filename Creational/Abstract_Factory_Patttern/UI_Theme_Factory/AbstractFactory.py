from abc import ABC, abstractmethod

class AbstractFactory:

    @abstractmethod
    def create_theme(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass