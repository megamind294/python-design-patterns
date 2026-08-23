# Python Design Patterns

A compact Python portfolio of six classic design patterns with runnable examples and automated tests.

> **Coursework provenance:** Factory and Adapter are reconstructed from recovered university assignment descriptions. Observer, Builder, Iterator, and Strategy are polished educational additions created to complete the design-pattern portfolio because the original source material for those exercises was not recoverable. This repository does not present every file as an untouched original submission.

## Patterns

| Pattern | Example | Main idea |
|---|---|---|
| Factory | Online-store order types | Centralize object creation behind `OrderFactory.create_order()` |
| Adapter | External payment gateway | Translate a local payment interface to an incompatible external API |
| Observer | Order-status notifications | Notify subscribed observers when subject state changes |
| Builder | Structured report creation | Build a complex immutable result through chained steps |
| Iterator | Course modules | Encapsulate traversal while preserving collection internals |
| Strategy | Checkout discounts | Swap algorithms at runtime without changing the context |

## Project structure

```text
factory/     recovered coursework reconstruction
adapter/     recovered coursework reconstruction
observer/    reconstructed educational addition
builder/     reconstructed educational addition
iterator/    reconstructed educational addition
strategy/    reconstructed educational addition
tests/       pytest coverage for all patterns
```

## Run

Python 3.11+ is recommended.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest -q
```

Run any example directly from the repository root, for example:

```bash
python -m factory.demo
python -m adapter.demo
python -m observer.demo
python -m builder.demo
python -m iterator.demo
python -m strategy.demo
```

## Recovered coursework details

### Factory

The recovered task described an online-store ordering exercise with an `IOrder` abstraction, `PhysicalProductOrder`, `DigitalProductOrder`, `ServiceOrder`, and `OrderFactory.create_order()`. The rebuilt example keeps that structure and provides a small total-calculation behavior so each concrete order can be exercised and tested.

### Adapter

The recovered task described an incompatible external payment system with `PaymentDetails`, `ExternalPaymentSystem.make_payment(...)`, and a `PaymentAdapter.process_payment(...)` method returning a boolean result. The rebuilt example preserves that interface and demonstrates argument translation through a test double.

## Why this repository exists

This project is designed to make design-pattern coursework easy to review: every pattern is intentionally small, independently runnable, and covered by tests. The emphasis is on understanding responsibilities and interfaces rather than framework-specific code.

## Testing and CI

GitHub Actions runs the full pytest suite on Python 3.11 for every pull request and push to `main`.
