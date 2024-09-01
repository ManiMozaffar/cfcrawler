.PHONY: install
install: ## Install the uv environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using uv"
	@uv sync

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@uv run pytest

.PHONY: check
check: ## check the code with flake8
	@echo "🚀 Checking code with ruff and pyright"
	@uv run ruff check .
	@uv run pyright