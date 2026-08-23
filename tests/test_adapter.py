from adapter.payment import ExternalPaymentSystem, PaymentAdapter, PaymentDetails


class RecordingGateway(ExternalPaymentSystem):
    def __init__(self):
        self.received = None

    def make_payment(self, total: float, currency_code: str, memo: str) -> bool:
        self.received = (total, currency_code, memo)
        return True


def test_adapter_translates_payment_details():
    gateway = RecordingGateway()
    adapter = PaymentAdapter(gateway)
    details = PaymentDetails(amount=49.5, currency='PLN', reference='ORDER-42')

    assert adapter.process_payment(details) is True
    assert gateway.received == (49.5, 'PLN', 'ORDER-42')
