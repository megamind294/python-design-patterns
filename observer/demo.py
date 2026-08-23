from observer.order_status import OrderStatusSubject, RecordingObserver


if __name__ == "__main__":
    subject = OrderStatusSubject()
    observer = RecordingObserver()
    subject.subscribe(observer)
    subject.set_status("paid")
    subject.set_status("shipped")
    print(observer.events)
