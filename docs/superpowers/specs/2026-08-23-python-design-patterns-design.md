# Python Design Patterns Coursework Portfolio Design

## Goal
Reconstruct and polish university design-pattern coursework into a recruiter-friendly Python repository with runnable examples, focused tests, and explicit provenance notes.

## Source Fidelity
- Factory and Adapter are treated as recovered coursework tasks.
- Factory preserves the online-order exercise with `IOrder`, `PhysicalProductOrder`, `DigitalProductOrder`, `ServiceOrder`, and `OrderFactory.create_order()`.
- Adapter preserves the external-payment exercise with `PaymentDetails`, `ExternalPaymentSystem.make_payment()`, and `PaymentAdapter.process_payment()`.
- Observer, Builder, Iterator, and Strategy are included as reconstructed educational additions because original assignment artifacts were not recoverable from the available files.
- The README must not claim reconstructed examples were untouched original submissions.

## Structure
Each pattern lives in its own package with one small domain example and tests:

- `factory/` — online-store order creation and total calculation.
- `adapter/` — adapt an incompatible external payment gateway to a local payment interface.
- `observer/` — order-status notifications to subscribers.
- `builder/` — incremental construction of a configurable report.
- `iterator/` — custom iteration over a course/module collection.
- `strategy/` — interchangeable discount calculation strategies.

## Quality Standard
- Python 3.11+.
- `pytest` tests for core behavior.
- No external runtime dependencies beyond pytest for testing.
- Clear type hints and small modules.
- Every example runnable from the command line.
- README explains intent, pattern roles, structure, testing, and reconstruction disclosure.
- GitHub Actions runs tests on Python 3.11.

## Non-Goals
- Framework-heavy implementations.
- Production e-commerce/payment integrations.
- Overengineered abstractions unrelated to demonstrating each pattern.

## Success Criteria
- Six pattern examples exist and are independently understandable.
- Factory and Adapter match the recovered coursework descriptions.
- All tests pass in CI.
- README is accurate about which material is recovered vs reconstructed.
