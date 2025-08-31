.PHONY: typehint
typehint:
	mypy --ignore-missing-imports src/

.PHONY: test
test:
	pytest tests/

.PHONY: lint
lint:
	pylint src/

.PHONY: check
	check: lint typehint test