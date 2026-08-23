from factory.orders import DigitalProductOrder, OrderFactory, PhysicalProductOrder, ServiceOrder


def test_factory_builds_each_order_type():
    assert isinstance(OrderFactory.create_order('physical', 120), PhysicalProductOrder)
    assert isinstance(OrderFactory.create_order('digital', 80), DigitalProductOrder)
    assert isinstance(OrderFactory.create_order('service', 200), ServiceOrder)


def test_orders_calculate_expected_totals():
    assert PhysicalProductOrder(100).calculate_total() == 110
    assert DigitalProductOrder(100).calculate_total() == 100
    assert ServiceOrder(100).calculate_total() == 118
