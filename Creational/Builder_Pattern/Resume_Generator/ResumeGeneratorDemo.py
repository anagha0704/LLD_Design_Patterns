from ResumeBuilder import ResumeBuilder

class ResumeGeneratorDemo:

    def run():
        builder1 = ResumeBuilder()
        
        # fresher
        fresher_resume = (builder1
                        .set_personal_info("Alice Johnson", "alice@example.com", "123-456-7890")
                        .add_education("B.Sc Computer Science, XYZ University")
                        .add_project("Personal Portfolio Website")
                        .add_skill("Python")
                        .add_skill("SQL")
                        .build()
                        )
        
        print("Fresher Resume:\n", fresher_resume)

        # experienced
        builder2 = ResumeBuilder()

        experienced_resume = (builder2
                            .set_personal_info("Bob Smith", "bob@example.com", "987-654-3210")
                            .add_education("M.Sc Data Science, ABC University")
                            .add_work_experience("Software Engineer at TechCorp (3 years)")
                            .add_work_experience("Data Analyst at DataWorks (2 years)")
                            .add_project("Customer Churn Prediction ML Model")
                            .add_skill("Java")
                            .add_skill("Machine Learning")
                            .add_certification("AWS Certified Solutions Architect")
                            .build())
    
        print("Experienced Resume:\n", experienced_resume)

if __name__ == "__main__":
    ResumeGeneratorDemo.run()