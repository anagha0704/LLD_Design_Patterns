from Handler import Handler
from Document import Document

class Department(Handler):

    def approve(self, doc: Document):
        if doc.category == "Budget requests":
            print(f"Department: Document {doc.id} has been Approved")
        else:
            self.next.approve(doc)