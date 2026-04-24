---
name: python-docstrings
description: Write clear, contract-first docstrings using Google Style format with explicit intent and boundaries
---

# Python Docstrings

## Purpose

Guide developers to write clear, contract-first docstrings in Google Style format that emphasize **explicit over implicit**. Docstrings should capture callable intent, boundary semantics, and error contracts so code is self-documenting without invented rationale.

## Trigger / When to use

**Use this skill when**:
- Writing or reviewing public API docstrings (classes, public methods, module-level functions, dataclass fields)
- Deciding when a private helper method needs more than a one-liner
- Choosing between traditional `Raises:` vs business-return patterns (e.g., `Result[T, E]`)
- Documenting semantic intent without guessing at hidden business rationale
- Capturing error semantics and field-level contracts in structured data

**Do NOT use this skill for**:
- Choosing type hint shapes (e.g., `Optional` vs `Union`) — delegate to `python-type-hints-strict`
- Deciding whether to use a dataclass, ABC, or enum — delegate to `python-model-selection`
- Naming conventions — delegate to `python-naming`
- Framework-specific auto-docs (FastAPI, Pydantic, SQLAlchemy) — out of scope
- Inline comments on algorithms or control flow — delegate to code clarity improvements

## Inputs

- Public or private method/class/function signature with type hints
- Explicit code-adjacent context: parameter names, return types, error types, module/class role, surrounding API boundary
- Business contract signals: what callers need to know about preconditions, postconditions, error paths, or domain semantics

## Process

**Step-by-step docstring workflow**:

1. **Identify scope**: Is this a public API (class, public method, public function, dataclass field) or private helper?
   - **Public**: Always write full docstring (one-liner + description + Args/Returns/Raises/Examples)
   - **Private**: Write one-liner; add full docstring only if explicit contract signals exist (state mutation, error translation, structured/domain return, reused preconditions)

2. **Extract explicit signals**:
   - Symbol name and module/class role
   - Parameter names and type annotations
   - Return type (including `None`)
   - Named error types (exception classes, `Result`, `Union[Success, Failure]`)
   - Constraints visible in code (e.g., guards, validators)

3. **Derive semantic intent**:
   - If signals reveal a clear boundary or domain role (e.g., "authenticate a user against JWT"), document that **why** and **when** briefly
   - If signals do **not** reveal trustworthy "why", skip invented rationale and write contract-only docstring instead
   - When in doubt, prefer **"what contract / when to call"** over speculative "why"

4. **Identify error paths**:
   - Traditional: document exception types in `Raises:` and when they occur
   - Modern: if returning `Result[T, E]` or `Union[Success, Failure]`, document both Ok and Err paths in `Returns:` section
   - For dataclass fields: document domain constraints only if they are already explicit in public API or validation

5. **Fill Google Style sections**:
   - **One-liner**: callable purpose in present tense (e.g., "Authenticate a user using JWT.")
   - **Extended description**: intent, boundary context, preconditions (if not obvious from signature)
   - **Args**: parameter purpose, type (optional; trust signature), constraints
   - **Returns**: return value meaning, optional/error semantics
   - **Raises** or error case in `Returns:`: when and why exceptions/errors occur
   - **Examples**: 1–2 typical use cases (optional for simple callables)
   - **Yields** (if generator): similar to Returns

## Examples

### Positive Example 1: Public Function with Semantic Intent Derived from Explicit Boundary Context

```python
def authenticate_user(token: str, secret_key: str) -> User:
    """Authenticate a user using a JWT token.
    
    Verifies the JWT signature against the provided secret key and extracts the 
    embedded user identity. This is the primary authentication entry point for 
    REST API requests.
    
    Args:
        token: A JWT-formatted bearer token from the request Authorization header.
        secret_key: The HMAC secret key used to verify the token signature.
    
    Returns:
        A User object with populated id, email, and roles extracted from the token claims.
    
    Raises:
        JWTError: If the token signature is invalid or the token is expired.
        ValueError: If the token is malformed or missing required claims.
    
    Example:
        user = authenticate_user(token="eyJ0...", secret_key="secret123")
    """
```

**Why this is correct**: The docstring captures the **why** (primary authentication entry point) and **when** (REST API requests) from explicit code-adjacent context (function name, parameter names, return type, exception types). No invented rationale.

---

### Positive Example 2: Public Function Where Intent Is Not Explicit, So Contract-Only Docstring

```python
def _normalize_email(email: str) -> str:
    """Return a lowercase, trimmed email address.
    
    Args:
        email: An email string, potentially with leading/trailing whitespace or mixed case.
    
    Returns:
        The email in lowercase and trimmed.
    """
```

**Why this is correct**: The function name and type signature already convey purpose. The docstring **does not invent** a business "why" (e.g., "to match user records in our database"). Instead, it states the contract clearly: what goes in, what comes out. This stays portable and generic.

---

### Positive Example 3: Private Helper with No Independent Contract (One-Liner Only)

```python
class UserRepository:
    def _build_query_filter(self, role: str) -> dict:
        """Build a database query filter dict for the given role."""
        return {"role": role, "is_active": True}
```

**Why this is correct**: This is a local implementation detail with no independent caller-facing contract outside the method. The one-liner is sufficient. No full docstring needed.

---

### Negative Example: Invented Rationale and Type Contradiction

```python
def process_order(order_id: int) -> Order:
    """Process an order to generate revenue for the platform.
    
    This method is important for business because orders drive our company's 
    growth metrics. We call it from the payment service whenever a user completes 
    checkout.
    
    Args:
        order_id: The order ID. It's a number.
    
    Returns:
        order: An Order object. This is the main data structure we use.
    
    Raises:
        OrderNotFound: If the order does not exist (probably because the user 
                       deleted it or it was corrupted by some race condition).
    """
```

**Why this is wrong**:
1. **Invented rationale**: "to generate revenue for the platform" is not discoverable from code or visible API boundary
2. **Over-explaining obvious**: "It's a number" and "This is the main data structure" add noise
3. **Vague error semantics**: Raises description speculates ("probably because...") instead of stating contract clearly
4. **Redundant Returns**: Restates type information already in signature

---

## Outputs

A complete Google Style docstring following the contract-first philosophy:
- Clear one-liner summarizing intent
- Extended description only when intent is explicit from code-adjacent context
- Args / Returns / Raises sections that state the contract clearly
- No invented business rationale not discoverable from code or surrounding API
- Portable; no project-specific architecture assumptions

## Boundaries

**OUT of scope** (delegate to other skills):
- Type hint shape decisions (`Optional` vs `Union`, `int` vs `float`) → `python-type-hints-strict`
- Model and class design choices (dataclass vs ABC, @validator, JSONSchema) → `python-model-selection`
- Naming conventions for identifiers and variables → `python-naming`
- Framework-specific docstring patterns (FastAPI auto-docs, Pydantic, SQLAlchemy) → framework skills
- Linting and auto-formatting → linter configuration
- Async/await specific patterns → future skill (explicitly deferred)
- Deprecation warnings and version history → future skill (explicitly deferred)

**IN scope** (this skill owns):
- Google Style format and structure (one-liner, description, Args/Returns/Raises/Examples/Yields)
- Public API contract documentation (classes, public methods, public functions, dataclass fields)
- Private method docstring rule (one-liner vs full, based on independent contract signals)
- Semantic intent capture (derivation method from explicit signals; contract-only fallback)
- Error semantics (both traditional `Raises:` and business-return patterns like `Result[T, E]`)
- Dataclass field-level semantic documentation
- Type hint alignment (docstrings must not contradict signatures)

## Local references

- **reference.md**: Navigation overview; lists split reference files and their roles
- **references/google-style-template.md**: Google Style structure reference and format guidelines
- **references/semantic-intent.md**: How to derive semantic intent from explicit signals; fallback rules; anti-pattern examples
- **references/error-semantics.md**: Traditional `Raises:` vs business-return patterns (Result[T,E]); error documentation without choosing design pattern
- **references/dataclass-patterns.md**: Field-level documentation; semantic role capture; contract-vs-validation boundary
