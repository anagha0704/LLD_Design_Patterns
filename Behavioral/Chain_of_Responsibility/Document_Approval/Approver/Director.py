from Handler import Handler
from Document import Document

class Director(Handler):

    def approve(self, doc: Document):
        if doc.category == "Policy changes" or doc.category == "Large expenditures":
            print(f"Director: Document {doc.id} has been Approved")
        else:
            print(f"'{doc.category}' Category of Document is invalid")