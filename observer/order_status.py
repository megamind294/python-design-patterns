from typing import Protocol


class Observer(Protocol):
    def update(self, status: str) -> None: ...


class OrderStatusSubject:
    def __init__(self):
        self._observers: list[Observer] = []
        self.status = "created"

    def subscribe(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def set_status(self, status: str) -> None:
        self.status = status
        for observer in tuple(self._observers):
            observer.update(status)


class RecordingObserver:
    def __init__(self):
        self.events: list[str] = []

    def update(self, status: str) -> None:
        self.events.append(status)
