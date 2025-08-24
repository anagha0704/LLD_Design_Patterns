from abc import ABC, abstractmethod

class Builder(ABC):

    @abstractmethod
    def set_personal_info(self, name: str, email: str, phone_no: str)->"Builder":
        pass

    @abstractmethod
    def add_education(self, edu: str)->"Builder":
        pass
    
    @abstractmethod
    def add_work_experience(self, work: str)->"Builder":
        pass

    @abstractmethod
    def add_project(self, website: str)->"Builder":
        pass
    
    @abstractmethod
    def add_skill(self, skill: str)->"Builder":
        pass

    @abstractmethod
    def add_certification(self, cert: str)->"Builder":
        pass

    @abstractmethod
    def build(self):
        pass