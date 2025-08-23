from Handler import Handler
from Document import Document

class TeamLead(Handler):

    def approve(self, doc: Document):
        if doc.category == "Internal memos":
            print(f"Team Lead: Document {doc.id} has been Approved")
        else:
            self.next.approve(doc)