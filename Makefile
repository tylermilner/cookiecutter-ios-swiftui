# Default values
OUTPUT_DIR := .
COOKIECUTTER := pipenv run cookiecutter

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

# Setup Python environment (assumes Homebrew and pyenv is installed)
.PHONY: setup
setup:
	@echo "Installing Python version..."
	pyenv install
	@echo "Installing pipenv..."
	pip install pipenv

# Install project dependencies
.PHONY: install
install:
	@echo "Installing project dependencies..."
	pipenv install --dev
	@echo "Installing pre-commit hooks..."
	pipenv run pre-commit install
	@echo "Installing XcodeGen..."
	brew install xcodegen

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
