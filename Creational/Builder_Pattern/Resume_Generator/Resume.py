class Resume:
    
    def __init__(self):
        self.personl_info = None
        self.education = []
        self.work_experience = []
        self.projects = []
        self.skills = []
        self.certifications = []

    def __str__(self):
        res = "***Resume****\n"
        if self.personl_info:
            res += f"Personal Info: {self.personl_info}\n"
        if self.education:
            res += "Education:\n" + "\n".join(f" - {edu}" for edu in self.education) + "\n"
        if self.work_experience:
            res += "Work Experience:\n" + "\n".join(f" - {exp}" for exp in self.work_experience) + "\n"
        if self.projects:
            res += "Projects:\n" + "\n".join(f" - {proj}" for proj in self.projects) + "\n"
        if self.skills:
            res += "Skills:\n" + ", ".join(self.skills) + "\n"
        if self.certifications:
            res += "Certifications:\n" + "\n".join(f" - {cert}" for cert in self.certifications) + "\n"
        return res