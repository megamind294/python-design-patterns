from factory.orders import OrderFactory


if __name__ == "__main__":
    for kind in ("physical", "digital", "service"):
        order = OrderFactory.create_order(kind, 100)
        print(f"{kind}: {order.calculate_total():.2f}")
