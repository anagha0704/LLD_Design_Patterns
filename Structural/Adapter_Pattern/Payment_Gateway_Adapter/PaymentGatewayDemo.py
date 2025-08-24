from TargetProcessor import TargetProcessor
from PayPal import Paypal
from Stripe import Stripe
from AdapterPaypal.PaypalAdapter import PaypalAdapter
from AdapterStripe.StripeAdapter import StripeAdapter

class PaymentProcessGateway:

    def run():

        target = TargetProcessor()
        print(target.pay(800))

        paypal = Paypal()
        stripe = Stripe()

        adapter_p = PaypalAdapter(paypal)
        print(adapter_p.pay(550.00))

        adapter_s = StripeAdapter(stripe)
        print(adapter_s.pay(650.00))

if __name__ == "__main__":
    PaymentProcessGateway.run()