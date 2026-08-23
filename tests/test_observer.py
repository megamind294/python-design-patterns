from observer.order_status import OrderStatusSubject, RecordingObserver


def test_observers_receive_status_changes_and_can_unsubscribe():
    subject = OrderStatusSubject()
    first = RecordingObserver()
    second = RecordingObserver()
    subject.subscribe(first)
    subject.subscribe(second)

    subject.set_status('paid')
    subject.unsubscribe(second)
    subject.set_status('shipped')

    assert first.events == ['paid', 'shipped']
    assert second.events == ['paid']
