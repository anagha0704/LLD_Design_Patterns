from PaymentStrategy import PaymentStrategy

class PayPalPayment(PaymentStrategy):

    def pay(self, amount:float)->None:
        return f"Payment of {amount} is done using PayPal Payment Stategy!"