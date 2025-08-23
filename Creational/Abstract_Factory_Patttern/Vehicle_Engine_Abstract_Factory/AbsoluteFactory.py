from abc import ABC, abstractmethod

class AbsoluteFactory(ABC):

    @abstractmethod
    def create_vehicle(self): 
        pass
    
    @abstractmethod
    def create_engine(self): 
        pass