from typing import List
from Content import Question
from Tag import Tag
from SearchStrategy import SearchStrategy

class TagSearch(SearchStrategy):

    def __init__(self, tag: Tag):
        self.tag = tag

    def filter(self, questions: List[Question])->List[Question]:
        return [q for q in questions
                if any(t.get_name().lower() == self.tag.get_name().lower() for t in q.get_tags())]