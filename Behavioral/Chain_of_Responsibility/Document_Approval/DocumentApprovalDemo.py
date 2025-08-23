from Handler import Handler
from Document import Document
from Approver.Department import Department
from Approver.TeamLead import TeamLead
from Approver.Director import Director

class DocumentApprovalDemo:

    def run():
        team_lead = TeamLead()
        dept = Department()
        director = Director()

        team_lead.next_handler(dept)
        dept.next_handler(director)

        doc1 = Document("d1", "Internal memos")
        doc2 = Document("d2", "Budget requests")
        doc3 = Document("d3", "Policy changes")
        doc4 = Document("d4", "New Budget")

        team_lead.approve(doc1)
        team_lead.approve(doc3)
        team_lead.approve(doc2)
        team_lead.approve(doc4)
        
if __name__ == "__main__":
    DocumentApprovalDemo.run()