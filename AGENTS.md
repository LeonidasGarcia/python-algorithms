# AGENTS.md

## Import prefix
All algorithms are under `src.sorting`, not `sorting`. Tests and benchmarks use `from src.sorting import ...`.

## Commands
```bash
uv sync --extra dev  # install with test deps
uv run pytest       # run tests
uv run pytest -k bubble  # run one algorithm's tests
uv run python benchmarks/benchmark.py
```