# Python Design Patterns Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build six small, tested Python design-pattern examples, preserving recovered Factory/Adapter coursework and clearly labeling Observer/Builder/Iterator/Strategy as reconstructed educational additions.

**Architecture:** Each pattern is an independent Python package with a minimal domain model, a runnable `demo.py`, and pytest coverage. Shared framework code is deliberately avoided so each pattern remains understandable in isolation.

**Tech Stack:** Python 3.11+, pytest, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-23-python-design-patterns-design.md`

## Global Constraints

- Factory and Adapter must match the recovered coursework descriptions.
- Observer, Builder, Iterator, and Strategy must be disclosed as reconstructed educational additions.
- No runtime dependencies outside the Python standard library.
- Tests use pytest.
- Every pattern must be runnable independently.
- No secrets or personal academic identifiers.

---

### Task 1: Repository foundation + Factory pattern
**Files:** `.gitignore`, `requirements-dev.txt`, `factory/__init__.py`, `factory/orders.py`, `factory/demo.py`, `tests/test_factory.py`
**Interfaces:** `IOrder.calculate_total()`, `PhysicalProductOrder`, `DigitalProductOrder`, `ServiceOrder`, `OrderFactory.create_order(order_type, amount)`.
- [ ] Write tests that verify each order class and factory selection.
- [ ] Run `pytest tests/test_factory.py -v` and confirm RED before implementation.
- [ ] Implement the smallest classes/factory needed to pass.
- [ ] Run the test and confirm GREEN.
- [ ] Commit `feat: add factory pattern coursework example`.

### Task 2: Adapter pattern
**Files:** `adapter/__init__.py`, `adapter/payment.py`, `adapter/demo.py`, `tests/test_adapter.py`
**Interfaces:** `PaymentDetails(amount, currency, reference)`, `ExternalPaymentSystem.make_payment(total, currency_code, memo) -> bool`, `PaymentAdapter.process_payment(details) -> bool`.
- [ ] Write tests for argument translation and boolean result propagation.
- [ ] Confirm RED.
- [ ] Implement adapter and demo.
- [ ] Confirm GREEN.
- [ ] Commit `feat: add adapter pattern coursework example`.

### Task 3: Observer pattern reconstruction
**Files:** `observer/__init__.py`, `observer/order_status.py`, `observer/demo.py`, `tests/test_observer.py`
**Interfaces:** `OrderStatusSubject.subscribe(observer)`, `unsubscribe(observer)`, `set_status(status)`; observers implement `update(status)`.
- [ ] Test subscriber notifications and unsubscribe behavior.
- [ ] Confirm RED.
- [ ] Implement subject/observers.
- [ ] Confirm GREEN.
- [ ] Commit `feat: add observer pattern example`.

### Task 4: Builder pattern reconstruction
**Files:** `builder/__init__.py`, `builder/report.py`, `builder/demo.py`, `tests/test_builder.py`
**Interfaces:** `ReportBuilder.title()`, `add_section()`, `include_summary()`, `build() -> Report`.
- [ ] Test chained construction and immutable built output.
- [ ] Confirm RED.
- [ ] Implement builder.
- [ ] Confirm GREEN.
- [ ] Commit `feat: add builder pattern example`.

### Task 5: Iterator pattern reconstruction
**Files:** `iterator/__init__.py`, `iterator/course.py`, `iterator/demo.py`, `tests/test_iterator.py`
**Interfaces:** `CourseModules` implements `__iter__`; iterator yields modules in insertion order.
- [ ] Test custom iteration and repeated independent iteration.
- [ ] Confirm RED.
- [ ] Implement collection/iterator.
- [ ] Confirm GREEN.
- [ ] Commit `feat: add iterator pattern example`.

### Task 6: Strategy pattern reconstruction
**Files:** `strategy/__init__.py`, `strategy/discount.py`, `strategy/demo.py`, `tests/test_strategy.py`
**Interfaces:** `DiscountStrategy.apply(subtotal)`, `NoDiscount`, `PercentageDiscount`, `FixedDiscount`, `Checkout.set_strategy()` and `total()`.
- [ ] Test strategy switching and floor-at-zero behavior.
- [ ] Confirm RED.
- [ ] Implement strategies/context.
- [ ] Confirm GREEN.
- [ ] Commit `feat: add strategy pattern example`.

### Task 7: CI + recruiter documentation
**Files:** `.github/workflows/ci.yml`, `README.md`
- [ ] Add Python 3.11 CI running `pytest -q`.
- [ ] Write README with pattern table, run commands, folder structure, recovered/reconstructed provenance, and learning outcomes.
- [ ] Run full `pytest -q`.
- [ ] Commit `docs: polish design patterns portfolio project`.

## Self-Review
- Spec coverage: all six patterns, provenance, tests, runnable demos, CI, and README are mapped.
- Placeholder scan: no implementation placeholders remain.
- Type consistency: interfaces in tests and modules use the same names across tasks.
