from ShoppingCart import ShoppingCart
from Strategies.CreditCardPayment import CreditCardPayment
from Strategies.CryptoPayment import CryptoPayment
from Strategies.PaypalPayment import PayPalPayment

class PaymentMethodDemo:

    def run():
        cart = ShoppingCart()

        creditcard = CreditCardPayment()
        paypal = PayPalPayment()
        crypto = CryptoPayment()

        cart.set_strategy(creditcard)
        cart.make_payment(1000)

        cart.set_strategy(paypal)
        cart.make_payment(1500.00)

        cart.set_strategy(crypto)
        cart.make_payment(2000)

if __name__ == "__main__":
    PaymentMethodDemo.run()