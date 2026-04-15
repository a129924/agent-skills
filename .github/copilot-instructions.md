# agent-skills — Copilot Instructions

Concise, project-specific context for productive AI-assisted development.

---

## 🎯 Purpose & Architecture

**agent-skills** converts legacy Python data pipeline processes into reusable, Domain-Driven Design (DDD) based **Agent Skills** — modular, composable units of work that can be orchestrated by AI agents or humans in Plan-Driven Development workflows.

**Core Concept**: Each skill is a **Bounded Context** containing domain models, business logic, and infrastructure, enabling parallel skill development and cross-skill composition.

---

## ⚡ Quick Start

### Prerequisites
- Python 3.10+
- `uv` package manager (https://github.com/astral-sh/uv)

### Setup & Testing
```bash
# Create virtual environment
uv venv

# Sync dependencies
uv sync

# Run tests (all)
uv run pytest tests/ -v

# Run single test file/function
uv run pytest tests/skills/observation/test_create_observation.py -v
uv run pytest tests/skills/observation/test_create_observation.py::test_create_valid_observation -v

# Type checking
uv run pyright src/

# Linting & formatting
uv run ruff check src/ --fix
uv run ruff format src/
```

---

## 📁 Project Structure

```
agent-skills/
├── src/agent_skills/                    # Main codebase (DDD four-layer per skill)
│   ├── {skill_name}/                    # Each skill is a Bounded Context
│   │   ├── domain/                      # Business logic, entities, contracts
│   │   ├── application/                 # Use cases, services, DTOs
│   │   ├── infrastructure/              # Repositories, adapters, external APIs
│   │   └── __init__.py
│   ├── shared/                          # Cross-skill utilities (values, errors)
│   └── __init__.py
│
├── tests/
│   ├── skills/                          # Per-skill tests
│   │   └── {skill_name}/
│   │       ├── test_domain/
│   │       ├── test_application/
│   │       └── test_infrastructure/
│   └── conftest.py
│
├── pyproject.toml                       # uv project config + dependencies
├── .github/
│   ├── copilot-instructions.md          # This file
│   └── workflows/                       # CI/CD (optional)
└── README.md
```

### Three-Layer Path Convention

```
src/agent_skills/{skill_name}/{layer}/{feature}/{package}/{module}.py
```

**Examples**:
- `src/agent_skills/observation/domain/models/observation.py`
- `src/agent_skills/observation/application/use_cases/create_observation.py`
- `src/agent_skills/observation/infrastructure/repositories/postgres_observation_repository.py`
- `src/agent_skills/patient/domain/services/patient_service.py`

---

## 📝 Coding Conventions (Must Follow)

### Naming Rules
- **Variables, functions, modules, directories**: `snake_case` (lowercase with underscores)
- **Classes**: `PascalCase`
- **Constants**: `UPPER_CASE`
- **No Chinese, special characters in code** (reserved for docs/comments)

### Type Hints (Mandatory)
- All function signatures **must** include explicit type hints on parameters and return values
- Use **PEP 604 syntax** (Python 3.10+): `str | int`, `User | None` (not `Union`, `Optional`)
- Use `list[str]`, `dict[str, int]` (not `List`, `Dict`)

**Example**:
```python
from typing import TypeAlias
from uuid import UUID

UserId: TypeAlias = UUID

def get_user_by_id(user_id: UserId) -> User | None:
    """Retrieve user by ID."""
    pass
```

### Domain Layer (Contracts)

**Contracts** define business logic without technical implementation details:

- **Sync contracts**: Pure business naming (no `Async` prefix)
  ```python
  class ObservationRepository(ABC):
      @abstractmethod
      def find_by_id(self, obs_id: str) -> Observation | None:
          """Find observation by ID."""
          pass
  ```

- **Async contracts**: Mark with `Async` prefix to disambiguate
  ```python
  class AsyncNotificationService(ABC):
      @abstractmethod
      async def send_async(self, notification: Notification) -> None:
          pass
  ```

- **Prohibited**: Technical terms (PostgreSQL, HTTP, Cache) in domain names

### Infrastructure Layer (Implementations)

Infrastructure classes use **[Technology] + [Contract Name]** pattern:

```python
# ✅ Correct
class PostgresObservationRepository(ObservationRepository):
    pass

class HttpxNotificationGateway(NotificationGateway):
    pass

class InMemoryObservationRepository(ObservationRepository):  # For testing
    pass

# ❌ Incorrect (domain terms in infra)
class ObservationRepository:  # Should be PostgresObservationRepository
    pass
```

### Method Naming by Layer

Naming style varies by architectural layer to reflect abstraction level:

| Layer | Verbs | Examples |
|-------|-------|----------|
| **Infrastructure** | `fetch_`, `_execute_`, `_parse_`, `_map_` | `fetch_by_sql()`, `_parse_json_response()` |
| **Domain** | `find_`, `get_`, `save_`, `delete_`, `create_` | `find_by_id()`, `find_all_active()`, `save()` |
| **Application** | `execute()`, `validate_`, `apply_`, `_build_` | `execute()`, `validate_input()`, `_build_response()` |
| **Presentation** | RESTful verbs (lowercase) | `create_`, `get_`, `list_`, `update_`, `delete_` |

**Golden Rule**: Infrastructure layer uses technical jargon; Domain layer uses business language.

### Class Visibility & Structure

```python
class MyService:
    # 1. Public methods (no prefix)
    def create_user(self, name: str) -> User:
        self._validate_name(name)
        return User(name=name)

    # 2. Private methods (single underscore prefix)
    def _validate_name(self, name: str) -> None:
        if not name or len(name) < 2:
            raise ValueError("Name must be at least 2 characters")

    # 3. Magic methods (e.g., __init__, __str__)
    def __repr__(self) -> str:
        return f"MyService(...)"
```

### ABC & Protocol Rules

- **ABC (Abstract Base Class)**: When defining interface with shared logic or clear hierarchy (e.g., Repository, Service)
- **Protocol**: When defining pure structural contracts without inheritance
- **Priority**: Prefer ABC
- **Required**: Use `@override` decorator on implementations

**Example**:
```python
from abc import ABC, abstractmethod
from typing_extensions import override

class ObservationRepository(ABC):
    @abstractmethod
    def find_by_id(self, obs_id: str) -> Observation | None:
        pass

class PostgresObservationRepository(ObservationRepository):
    @override
    def find_by_id(self, obs_id: str) -> Observation | None:
        # Implementation
        return None
```

### Pydantic & Mapping

- **External data** (API requests, third-party responses): Use Pydantic `BaseModel` for validation
- **Internal domain models**: Use `@dataclass` or `@dataclass(frozen=True)`
- **Mapping required**: Always use explicit Mapper to convert Pydantic DTO → internal dataclass

**Example**:
```python
from pydantic import BaseModel
from dataclasses import dataclass

# External DTO
class CreateObservationRequest(BaseModel):
    patient_id: str
    observation_type: str
    content: str

# Internal model
@dataclass(frozen=True)
class Observation:
    patient_id: str
    observation_type: ObservationType
    content: str

# Mapper
class ObservationMapper:
    @staticmethod
    def from_request(req: CreateObservationRequest) -> Observation:
        return Observation(
            patient_id=req.patient_id,
            observation_type=ObservationType(req.observation_type),
            content=req.content,
        )
```

---

## 🤖 Agent Skills Framework

Each **skill** is a self-contained Bounded Context implementing a reusable data transformation or business process:

### Skill Anatomy

```
{skill_name}/
├── domain/
│   ├── models/              # Entities, value objects
│   ├── services/            # Domain services with business rules
│   ├── errors.py            # Domain-specific exceptions (inherit BaseError)
│   └── __init__.py
│
├── application/
│   ├── use_cases/           # Orchestration of domain logic
│   │   └── {action}_use_case.py
│   ├── dto/                 # Data Transfer Objects (Pydantic)
│   └── __init__.py
│
├── infrastructure/
│   ├── repositories/        # Data access implementations
│   ├── adapters/            # External API clients
│   └── __init__.py
│
└── __init__.py
```

### Creating a New Skill

1. **Define domain contracts** (domain/models, domain/services, domain/errors)
   - Write business rules without implementation details
   - Use ABC for repositories & services
   
2. **Implement use cases** (application/use_cases)
   - Orchestrate domain logic
   - Validate input, coordinate with repositories
   - Return DTOs (Pydantic) for external consumption

3. **Implement infrastructure** (infrastructure/repositories, infrastructure/adapters)
   - Inherit from domain contracts
   - Use [Technology] + [Contract] naming
   
4. **Write tests** covering domain logic, use case flows, and integration points

---

## 🧪 Testing Strategy

### Test Organization
```
tests/skills/{skill_name}/
├── test_domain/
│   └── test_models.py, test_services.py, test_errors.py
├── test_application/
│   └── test_create_{action}_use_case.py
└── test_infrastructure/
    └── test_postgres_{skill_name}_repository.py
```

### Minimum Requirements
- **Coverage target**: 80% for domain + application layers
- **Per use case**: ✅ success path, ❌ main failure scenarios
- **Run before commit**: `uv run pytest tests/ -v`

---

## 📋 Plan-Driven Development Workflow

Each skill development follows a structured plan → implementation → review cycle:

### 1. Create Plan
File: `plan/{skill_name}/{skill_name}.plan.md`

```markdown
# {Skill Name} Plan

## Goals
[What business value does this skill provide?]

## Design Direction
[Architecture approach: sync/async, data flow, key patterns]

## Contracts & Interfaces
- Domain models: ...
- Repository interface: ...
- Use case DTO: ...
- Errors: ...

## Outputs
- src/agent_skills/{skill_name}/domain/...
- src/agent_skills/{skill_name}/application/...
- tests/skills/{skill_name}/...

## Acceptance Criteria
- [ ] Use case executes successfully
- [ ] 80% test coverage
- [ ] Type checking passes (pyright)
- [ ] Linting passes (ruff)
```

### 2. Plan Discussion → tasks.md
- Agent confirms understanding, asks clarifications if needed
- Agent produces `plan/{skill_name}/tasks.md` with step-by-step breakdown

### 3. Implementation
- Agent implements per DDD structure & conventions
- Runs tests, type checker, linter before signaling completion

### 4. Code Review & Iteration
- Human reviews design & implementation
- Same session: agent refines based on feedback
- Repeat until ready to commit

### 5. Completion
```bash
# Archive tasks.md after acceptance
mv plan/{skill_name}/tasks.md plan/{skill_name}/{skill_name}-$(date +%Y-%m-%d).tasks.md

# Commit with conventional commit format
git commit -m "feat({skill_name}): description of what was implemented"
```

---

## 🔧 Git Workflow

### Branch Naming
```
ai/feature/{skill_name}    # New skill
ai/fix/{skill_name}        # Bug fix in existing skill
ai/refactor/{skill_name}   # Refactoring existing skill
```

### Commit Message Format (Conventional Commits)
```
type(scope): subject

scope = {skill_name} (e.g., observation, patient, notification)
type = feat|fix|refactor|docs|test|chore

Examples:
- feat(observation): implement create observation use case
- fix(patient): handle null patient ID edge case
- refactor(notification): simplify async sender logic
```

---

## 📚 Key Files to Know

- **pyproject.toml**: Project metadata, dependencies (uv manages these)
- **.github/copilot-instructions.md**: This file — quick reference for Copilot
- **src/agent_skills/shared/**: Common errors, value objects, utilities shared across skills
- **tests/conftest.py**: Pytest fixtures and test configuration

---

## ⚠️ Common Mistakes to Avoid

1. ❌ **Mixing technical terms in domain layer**
   - ❌ `PostgresProductRepository` (in domain/)
   - ✅ `ProductRepository` (in domain/); `PostgresProductRepository` (in infrastructure/)

2. ❌ **Missing type hints**
   - ❌ `def create(x): return x`
   - ✅ `def create(x: Item) -> Item:`

3. ❌ **Old-style unions**
   - ❌ `Optional[User]`, `Union[str, int]`
   - ✅ `User | None`, `str | int`

4. ❌ **No `__init__.py` in packages**
   - Every directory under src/ with subfolders must have `__init__.py`

5. ❌ **Private methods without underscore**
   - ❌ `def helper(): ...`
   - ✅ `def _helper(): ...`

6. ❌ **Dataclass without type hints**
   - ❌ `@dataclass class User: name = ...`
   - ✅ `@dataclass class User: name: str`

---

## 🔗 References

- **Legacy Rules**: /Users/andrew/code/ai-agent-rules/ai-agent-rules/
  - `ai-rules/01_project_structure.md` — DDD architecture deep-dive
  - `ai-rules/02_coding_standards.md` — Naming & style detailed rules
  - `ai-rules/03_agents_spec.md` — 7-phase collaboration workflow
  - `ai-rules/04_spec_format.md` — Plan markdown format
  
- **Python Docs**:
  - PEP 604 (Type Unions): https://www.python.org/dev/peps/pep-0604/
  - ABC & typing_extensions: https://docs.python.org/3/library/abc.html
  - Pydantic: https://docs.pydantic.dev/

---

## 🔌 MCP Servers (Optional)

For enhanced AI assistant capabilities, consider configuring MCP servers:

- **Database Access**: PostgreSQL/SQLite MCP server for schema inspection and query testing
- **CLI Tools**: Bash MCP server for running tests, linting, and deployment scripts during development
- **Advanced Scenarios**: File system or Python REPL servers for dynamic exploration

Consult your AI assistant's documentation on how to configure MCP servers for this project.

---

## ❓ Quick Troubleshooting

**Q: How do I run a single test?**
```bash
uv run pytest tests/skills/observation/test_create_observation.py::test_create_valid_observation -v
```

**Q: Type checking fails but code seems correct?**
```bash
# Ensure you're using PEP 604 syntax (| not Union)
uv run pyright src/ --outputjson
```

**Q: Should I use dataclass or Pydantic?**
- **Pydantic**: External data (API requests, config files) → validation
- **dataclass**: Internal domain models, DTOs between layers

**Q: How do I add a cross-skill utility?**
- Add to `src/agent_skills/shared/` with clear naming
- Import in other skills: `from agent_skills.shared import MyUtil`

---

**Ready to start?** Create your first skill plan in `plan/{skill_name}/{skill_name}.plan.md` and initiate a chat session! 🚀
