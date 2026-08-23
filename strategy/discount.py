from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, subtotal: float) -> float:
        raise NotImplementedError


class NoDiscount(DiscountStrategy):
    def apply(self, subtotal: float) -> float:
        return subtotal


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        self.percent = percent

    def apply(self, subtotal: float) -> float:
        return subtotal * (1 - self.percent / 100)


class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.amount = amount

    def apply(self, subtotal: float) -> float:
        return max(0, subtotal - self.amount)


class Checkout:
    def __init__(self, subtotal: float, strategy: DiscountStrategy):
        self.subtotal = subtotal
        self.strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy) -> None:
        self.strategy = strategy

    def total(self) -> float:
        return round(self.strategy.apply(self.subtotal), 2)
