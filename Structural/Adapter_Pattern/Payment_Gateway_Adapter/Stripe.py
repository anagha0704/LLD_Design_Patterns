class Stripe:

    def __init__(self):
        self.processor_name = "Stripe"

    def send_payment(self, total_amount: float)->float:
        return total_amount