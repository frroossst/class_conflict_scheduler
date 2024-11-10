version=Python 3.10.12
license=MIT


.PHONY: *

help: ## print this message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@egrep "^(.+)\:\ ##\ (.+)" ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

check: ## run type checks and ruff checks
	mypy .
	ruff check

test: ## run tests
	python3 tests.py

clean: ## clean up
	rm -rf __pycache__ .mypy_cache
