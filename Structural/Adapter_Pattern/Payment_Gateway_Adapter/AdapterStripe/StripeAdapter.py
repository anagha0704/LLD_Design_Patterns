from PaymentProcessor import PaymentProcessor
from Stripe import Stripe

class StripeAdapter(PaymentProcessor):

    def __init__(self, gateway: Stripe):
        self.gateway = gateway

    def pay(self, amount: str)->str:
        res = self.gateway.send_payment(amount)
        return f"Payment of {res} has been done"