from strategy.discount import Checkout, FixedDiscount, NoDiscount, PercentageDiscount


def test_checkout_can_switch_discount_strategies():
    checkout = Checkout(200, NoDiscount())
    assert checkout.total() == 200

    checkout.set_strategy(PercentageDiscount(10))
    assert checkout.total() == 180

    checkout.set_strategy(FixedDiscount(250))
    assert checkout.total() == 0
