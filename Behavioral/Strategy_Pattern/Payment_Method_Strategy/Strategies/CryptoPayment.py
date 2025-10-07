from PaymentStrategy import PaymentStrategy

class CryptoPayment(PaymentStrategy):

    def pay(self, amount:float)->None:
        return f"Payment of {amount} is done using Crypto Payment Stategy!"