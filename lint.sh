#!/bin/bash

# Run mypy
pipenv run mypy .

# Run formatter
pipenv run ruff format

# Run linter
pipenv run ruff check --fix
