from abc import ABC, abstractmethod


class IOrder(ABC):
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.amount = float(amount)

    @abstractmethod
    def calculate_total(self) -> float:
        raise NotImplementedError


class PhysicalProductOrder(IOrder):
    def calculate_total(self) -> float:
        return round(self.amount * 1.10, 2)


class DigitalProductOrder(IOrder):
    def calculate_total(self) -> float:
        return round(self.amount, 2)


class ServiceOrder(IOrder):
    def calculate_total(self) -> float:
        return round(self.amount * 1.18, 2)


class OrderFactory:
    _types = {
        "physical": PhysicalProductOrder,
        "digital": DigitalProductOrder,
        "service": ServiceOrder,
    }

    @classmethod
    def create_order(cls, order_type: str, amount: float) -> IOrder:
        try:
            order_class = cls._types[order_type.strip().lower()]
        except KeyError as exc:
            raise ValueError(f"unsupported order type: {order_type}") from exc
        return order_class(amount)
