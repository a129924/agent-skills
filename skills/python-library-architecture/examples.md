# Examples

- Positive: Put shared pagination and credential contracts in `core`, keep `storage/` and `queues/` isolated, and expose one `Client` that composes them without either theme importing the other.
- Positive: Keep adapters near their owning theme, let themes depend on `core`, and keep orchestration at the facade/client layer.
- Negative: Let `billing/` import `users/models.py`, move HTTP bootstrap into `core`, or use `common/` as a dump zone for unrelated cross-theme code.
