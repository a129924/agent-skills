"""Regression tests for the bounded model-evaluation output contract."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest


EVALUATOR_PATH = Path("plan/skills-audit-and-progressive-disclosure/evaluate_models.py")
SPEC = spec_from_file_location("evaluate_models", EVALUATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
evaluate_models = module_from_spec(SPEC)
SPEC.loader.exec_module(evaluate_models)


def test_validate_output_path_accepts_only_dedicated_evidence_file() -> None:
    assert evaluate_models.validate_output_path(
        evaluate_models.TOPIC / "model-results.jsonl"
    ) == evaluate_models.TOPIC / "model-results.jsonl"

    with pytest.raises(ValueError, match="named model-results\\.jsonl"):
        evaluate_models.validate_output_path(evaluate_models.TOPIC / "validation.md")

    with pytest.raises(ValueError, match="file in this topic directory"):
        evaluate_models.validate_output_path(Path("/tmp/model-results.jsonl"))
