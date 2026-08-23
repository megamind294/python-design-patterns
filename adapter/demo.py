from adapter.payment import ExternalPaymentSystem, PaymentAdapter, PaymentDetails


if __name__ == "__main__":
    adapter = PaymentAdapter(ExternalPaymentSystem())
    ok = adapter.process_payment(PaymentDetails(49.5, "PLN", "ORDER-42"))
    print(f"payment accepted: {ok}")
