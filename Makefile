.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@rye sync



.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@rye run pytest

.PHONY: check
check: ## check the code with flake8
	@echo "🚀 Checking code with ruff and pyright"
	@rye run ruff check .
	@rye run pyright