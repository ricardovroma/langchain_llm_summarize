linting:
	poetry run ruff check

linting/fix:
	poetry run ruff check --fix

cov:
	poetry run pytest --cov-fail-under=100 --cov=. --cov-report=html --cov-report=xml:coverage.xml tests --ignore=tests/int tests

run:
	poetry run python src/main.py

check: linting cov