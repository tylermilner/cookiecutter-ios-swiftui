#!/bin/bash

# Shell script to generate a project with the cookiecutter default values for quick debugging during development.
# Technically strays from the Cookiecutter project defaults slightly:
#   - No git repository will be created.
#   - Xcode will not be opened (use 'open-xcode' to override).
# Usage: ./generate-default-project.sh [open-xcode]
# open-xcode: Optional. If present, Xcode will be opened after generating the template.

# Get the command line argument
open_xcode=$1

# Set the open_xcode_project value based on the open_xcode argument
if [ "$open_xcode" = "open-xcode" ]; then
    open_xcode_project=True
else
    open_xcode_project=False
fi

# Generate a project with the cookiecutter default values
pipenv run cookiecutter . --no-input --overwrite-if-exists initialize_git_repo=False open_xcode_project=$open_xcode_project
