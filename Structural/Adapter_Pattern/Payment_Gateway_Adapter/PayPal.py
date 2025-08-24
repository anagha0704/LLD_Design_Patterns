class Paypal:

    def __init__(self):
        self.processor_name = "Paypal"

    def make_payment(self, payment_amount: str)->str:
        return f"Payment of {payment_amount} is done!!"