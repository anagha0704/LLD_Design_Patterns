from PaymentProcessor import PaymentProcessor

class TargetProcessor(PaymentProcessor):

    def pay(self, amount)->str:
        return f"TargetProcessor: Payment of {amount} has been done!!"