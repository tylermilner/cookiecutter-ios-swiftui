#!/bin/bash

SCHEME='{{ cookiecutter.__scheme }}'
DESTINATION='platform=iOS Simulator,OS={{ cookiecutter.deployment_target }},name={{ cookiecutter.simulator_name }}'

xcodebuild test -scheme "$SCHEME" -destination "$DESTINATION"
