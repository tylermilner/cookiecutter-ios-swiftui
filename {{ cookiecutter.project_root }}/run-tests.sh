#!/bin/bash

SCHEME='{{ cookiecutter.__scheme }}'
DESTINATION='platform=iOS Simulator,OS=latest,name=iPhone 15'

xcodebuild test -scheme "$SCHEME" -destination "$DESTINATION"
