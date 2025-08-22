from Item import Item
from ShoppingCart import ShoppingCart
from Strategies.FixedAmount import FixedAmount
from Strategies.NoDiscount import NoDiscount
from Strategies.PercentageDiscount import PercentageDiscount

class Checkout_Demo:

    def run():
        item1 = Item("Clothes", 30.0, PercentageDiscount())
        item2 = Item("Electronic", 50.0, FixedAmount())
        item3 = Item("Medical", 10.0, NoDiscount())

        cart = ShoppingCart()

        cart.add_item(item1)
        cart.add_item(item2)
        cart.add_item(item3)

        total_payment = 0

        for product in cart.items:
            cart.setStrategy(product.discountStrategy)

            discounted_price = cart.calculate_discount(product.price)
            print(f"For {product.name} price is {product.price}. After discount it is: {discounted_price}")
            total_payment += discounted_price
        
        print(f"Your today's total payment due is: {total_payment}")

if __name__ == "__main__":
    Checkout_Demo.run()