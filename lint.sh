#!/bin/bash

# Run formatter
pipenv run ruff format

# Run linter
pipenv run ruff check --fix
