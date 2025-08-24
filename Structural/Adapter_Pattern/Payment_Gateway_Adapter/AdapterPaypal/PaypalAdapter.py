from PaymentProcessor import PaymentProcessor
from PayPal import Paypal

class PaypalAdapter(PaymentProcessor):

    def __init__(self, gateway: Paypal):
        self.gateway = gateway

    def pay(self, amount: str)->str:
        res = self.gateway.make_payment(amount)
        return f"Paypal Adapter: {res}"