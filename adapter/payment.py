from dataclasses import dataclass


@dataclass(frozen=True)
class PaymentDetails:
    amount: float
    currency: str
    reference: str


class ExternalPaymentSystem:
    def make_payment(self, total: float, currency_code: str, memo: str) -> bool:
        return total > 0 and bool(currency_code.strip()) and bool(memo.strip())


class PaymentAdapter:
    def __init__(self, gateway: ExternalPaymentSystem):
        self.gateway = gateway

    def process_payment(self, details: PaymentDetails) -> bool:
        return self.gateway.make_payment(details.amount, details.currency, details.reference)
