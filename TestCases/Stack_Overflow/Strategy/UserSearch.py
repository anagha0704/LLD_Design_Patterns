from typing import List
from Content import Question
from User import User
from SearchStrategy import SearchStrategy

class UserSearch(SearchStrategy):

    def __init__(self, user: User):
        self.user = user

    def filter(self, questions: List[Question])->List[Question]:
        return [q for q in questions
                if q.get_author().get_id() == self.user.get_id()]