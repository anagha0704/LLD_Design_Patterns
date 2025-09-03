from abc import ABC, abstractmethod
from typing import List
from Content import Question

class SearchStrategy(ABC):

    @abstractmethod
    def filter(self,  questions: List[Question])->List[Question]:
        pass
