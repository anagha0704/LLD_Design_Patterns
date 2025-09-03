from typing import List
from Content import Question
from SearchStrategy import SearchStrategy

class KeywordSearch(SearchStrategy):

    def __init__(self, keyword: str):
        self.keyword = keyword.lower()

    def filter(self, questions: List[Question])->List[Question]:
        return [q for q in questions
                if self.keyword in q.get_title().lower() or self.keyword in q.get_body().lower()]