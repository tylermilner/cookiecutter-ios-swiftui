#!/bin/bash

xcodebuild test -project {{ cookiecutter.__project_name_no_spaces }}.xcodeproj -scheme {{ cookiecutter.__project_name_no_spaces }} -destination 'platform=iOS Simulator,name=iPhone 15 Pro,OS=latest'
