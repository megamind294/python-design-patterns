from strategy.discount import Checkout, NoDiscount, PercentageDiscount


if __name__ == "__main__":
    checkout = Checkout(200, NoDiscount())
    print("regular:", checkout.total())
    checkout.set_strategy(PercentageDiscount(15))
    print("discounted:", checkout.total())
