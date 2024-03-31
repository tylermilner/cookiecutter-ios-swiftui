#!/bin/bash

# Shell script to generate a project with the cookiecutter default values
# Usage: ./generate-default-project.sh

# Generate a project with the cookiecutter default values
pipenv run cookiecutter . --no-input --overwrite-if-exists
