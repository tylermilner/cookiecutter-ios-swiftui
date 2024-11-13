# Default values
OUTPUT_DIR := .
COOKIECUTTER := pipenv run cookiecutter
# Should match 'project_root' in cookiecutter.json
DEFAULT_PROJECT_FOLDER := my-app

# Generate a new project using default values and overwrite if exists
.PHONY: generate
generate:
	@echo "Generating project with default values..."
	$(COOKIECUTTER) $(OUTPUT_DIR) --overwrite-if-exists --no-input initialize_git_repo=False open_xcode_project=False

# Generate a new project using user-provided values and overwrite if exists
.PHONY: generate-with-inputs
generate-with-inputs:
	@echo "Generating project with user-provided values..."
	$(COOKIECUTTER) $(OUTPUT_DIR) --overwrite-if-exists

# Clean up generated project
.PHONY: clean
clean:
	@if [ -d "$(DEFAULT_PROJECT_FOLDER)" ]; then \
		echo "Cleaning up generated project..."; \
		rm -rf $(DEFAULT_PROJECT_FOLDER); \
	else \
		echo "Clean failed. '$(DEFAULT_PROJECT_FOLDER)' directory not found."; \
	fi

# Setup development environment (assumes Homebrew and pyenv is installed)
.PHONY: setup
setup:
	@echo "Installing Python version..."
	pyenv install
	@echo "Installing pipenv..."
	pip install pipenv
	@echo "Installing XcodeGen..."
	brew install xcodegen

# Install project dependencies
.PHONY: install
install:
	@echo "Installing project dependencies..."
	pipenv install --dev
	@echo "Installing pre-commit hooks..."
	pipenv run pre-commit install

# Uninstall project dependencies
.PHONY: uninstall
uninstall:
	@echo "Uninstalling pre-commit hooks..."
	pipenv run pre-commit uninstall
	@echo "Clearing pre-commit cache..."
	pipenv run pre-commit clean
	@echo "Uninstalling project dependencies..."
	pipenv --rm

# Run linters and formatters
.PHONY: lint
lint:
	@echo "Running linters and formatters using pre-commit..."
	pipenv run pre-commit run --all-files

# Run tests
.PHONY: test
test:
	@echo "Running tests..."
	pipenv run pytest
