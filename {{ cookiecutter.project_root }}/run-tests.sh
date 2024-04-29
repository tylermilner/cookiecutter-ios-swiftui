#!/bin/bash

SCHEME='{{ cookiecutter.__project_name_no_spaces }}'
DESTINATION='platform=iOS Simulator,OS=latest,name=iPhone 15'

xcodebuild test -scheme "$SCHEME" -destination "$DESTINATION"
