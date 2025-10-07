from PaymentStrategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):

    def pay(self, amount:float)->None:
        return f"Payment of {amount} is done using Credit Card  Stategy!"