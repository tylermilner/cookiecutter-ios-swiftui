# Define default values
# Output directory for generated project
OUTPUT_DIR := .

# Command to run cookiecutter
COOKIECUTTER := pipenv run cookiecutter

# Default options passed to cookiecutter
COOKIECUTTER_OPTIONS := --overwrite-if-exists --no-input initialize_git_repo=False open_xcode_project=False run_tests=False

# The default directory of the generated project
# Should match default value for 'project_root' in cookiecutter.json
GENERATED_PROJECT_DIR := my-app

# Generate a new project using default values and overwrite if exists
.PHONY: generate
generate:
	@echo "Generating project with default values..."
	$(COOKIECUTTER) $(OUTPUT_DIR) $(COOKIECUTTER_OPTIONS)

# Generate a new project using user-provided values and overwrite if exists
.PHONY: generate-with-inputs
generate-with-inputs:
	@echo "Generating project with user-provided values..."
	$(COOKIECUTTER) $(OUTPUT_DIR) --overwrite-if-exists

# Clean up generated project
.PHONY: clean
clean:
	@if [ -d "$(GENERATED_PROJECT_DIR)" ]; then \
		echo "Cleaning up generated project..."; \
		rm -rf $(GENERATED_PROJECT_DIR); \
	else \
		echo "Clean not necessary. '$(GENERATED_PROJECT_DIR)' directory not found."; \
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
	@if [ -d "$(shell PIPENV_VERBOSITY=-1 pipenv --venv)" ]; then \
		echo "Removing virtual environment..."; \
		rm -rf $(shell PIPENV_VERBOSITY=-1 pipenv --venv); \
	else \
		echo "Uninstall project dependencies failed. Virtual environment not found."; \
	fi

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
