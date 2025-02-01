.PHONY: fmt init test typecheck new

init:
	uv sync

fmt:
	uv run ruff check --fix
	uv run ruff format

test:
	uv run pytest

typecheck:
	uv run mypy

new:
	./new.sh

