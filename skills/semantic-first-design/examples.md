# Worked semantic-first examples

These examples show the distinction to surface. They intentionally do not
replace the concrete rules owned by the specialised Python skills.

## 1. Absence is not failure

```python
# Ambiguous: None can mean no customer, transport failure, or malformed data.
def find_customer(customer_id: str) -> Customer | None:
    ...
```

If a missing customer is normal but lookup failure is not, preserve `None` for
the single normal absence meaning and expose failure explicitly:

```python
def find_customer(customer_id: CustomerId) -> Customer | None:
    # Raises the package's explicit lookup failure when the lookup cannot run.
    ...
```

The semantic distinction is normal absence versus failure. Use
`python-api-signature` for the signature and `python-error-handling` for the
failure contract.

## 2. A behavior choice is not always a boolean

```python
# Does False mean send immediately, suppress delivery, or use the default?
def save(report: Report, notify: bool = False) -> None:
    ...
```

When the domain has more than an obvious on/off meaning, surface the policy:

```python
def save(report: Report, *, delivery: DeliveryPolicy) -> None:
    ...
```

Do not introduce `DeliveryPolicy` if the operation is genuinely binary and the
boolean name makes both meanings immediately clear. Route the signature and
construct choice to `python-api-signature` and `python-model-selection`.

## 3. Success can provide a new guarantee

```python
def parse_config(raw: object) -> Config:
    # The annotation claims Config, but validation has not happened.
    ...
```

If callers must rely on validation, make the successful guarantee truthful:

```python
def validate_config(raw: object) -> ValidatedConfig:
    ...
```

The change is justified only when `ValidatedConfig` carries a distinct,
caller-relevant guarantee. Use `python-type-hints-strict` and
`python-model-selection` for the concrete type design.

## 4. Translate at the boundary

```python
# Leaks a vendor-specific weak response into domain code.
def load_invoice(invoice_id: str) -> dict[str, object] | None:
    return vendor_client.fetch(invoice_id)
```

An adapter should translate vendor identifiers, weak payloads, missing results,
and failures into the application's own stable contract before orchestration
uses them. The semantic distinction is external protocol versus application
meaning. Route architecture and errors to `python-library-architecture` and
`python-error-handling`.

## 5. Visible composition without a fake abstraction

```python
# The chosen sender is hidden in global discovery.
def send_receipt(receipt: Receipt) -> None:
    sender = registry.resolve("sender")
    sender.send(receipt)
```

When sender selection affects behavior, pass or compose it visibly at the
appropriate boundary. Do not compensate by adding a `Dependencies` container
unless those values form a real, cohesive concept. Route architecture choices
to `python-library-architecture`.

## 6. Reject abstraction without a variation axis

```python
class Formatter(Protocol):
    def format(self, value: str) -> str: ...

class DefaultFormatter:
    def format(self, value: str) -> str:
        return value.strip()
```

With one behavior, no independent variation, and no boundary, the interface
adds a second interpretation without removing ambiguity. Keep the named
function or concrete component until a real variation or boundary appears.
