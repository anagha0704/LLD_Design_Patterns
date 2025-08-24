from Builder import Builder
from Resume import Resume

class ResumeBuilder(Builder):

    def __init__(self):
        self.resume = Resume()

    def set_personal_info(self, name: str, email: str, phone_no: str)->Builder:
        self.resume.personl_info = f"{name}, {email}, {phone_no}"
        return self

    def add_education(self, edu: str)->Builder:
        self.resume.education.append(edu)
        return self
    
    def add_work_experience(self, exp: str)->Builder:
        self.resume.work_experience.append(exp)
        return self

    def add_project(self, project: str)->Builder:
        self.resume.projects.append(project)
        return self
    
    def add_skill(self, skill: str)->Builder:
        self.resume.skills.append(skill)
        return self
    
    def add_certification(self, cert: str):
        self.resume.certifications.append(cert)
        return self

    def build(self):
        return self.resume