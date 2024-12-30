# cookiecutter-ios-swiftui

[![Tests](https://github.com/tylermilner/cookiecutter-ios-swiftui/actions/workflows/test.yml/badge.svg)](https://github.com/tylermilner/cookiecutter-ios-swiftui/actions/workflows/test.yml)
[![Deploy](https://github.com/tylermilner/cookiecutter-ios-swiftui/actions/workflows/deploy.yml/badge.svg)](https://github.com/tylermilner/cookiecutter-ios-swiftui/actions/workflows/deploy.yml)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for
jump-starting modern iOS apps using SwiftUI.

## ⚠️ Work in Progress ⚠️

This project is a work in progress and not yet feature complete. See below for
current progress:

- [x] Generate a bare-bones SwiftUI app
- [ ] Generate a bare-bones Fastlane setup
- [ ] Generate a bare-bones GitHub Actions CI/CD setup

## Getting Started

Although Cookiecutter runs on Linux, you'll want to have a Mac with Xcode
installed in order to properly generate a project using this template.

1. Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) (e.g.
   using [Homebrew](https://brew.sh)):

    ```Shell
    brew install cookiecutter
    ```

2. Install [XcodeGen](https://github.com/yonaskolb/XcodeGen):

    ```Shell
    brew install xcodegen
    ```

3. Run Cookiecutter against this repository:

    ```Shell
    cookiecutter gh:tylermilner/cookiecutter-ios-swiftui
    ```

4. Follow the prompts to generate your new iOS project.

## Generated Example Project

A generated version of this template that demonstrates the final project
structure can be found at [tylermilner/cookiecutter-ios-swiftui-output](https://github.com/tylermilner/cookiecutter-ios-swiftui-output).

### Resulting Directory Structure

The directory structure of your new project will look something like this (depending
on the settings that you choose):

```text
├── .github
│   └── workflows                                      <- GitHub Actions workflows for CI/CD
│       └── test.yml                                   <- GitHub Actions workflow for running tests
├── .gitignore                                         <- Standard iOS/Swift gitignore file
├── {{ cookiecutter.target_name }}                     <- The main app target directory
│   ├── Assets.xcassets                                <- Asset catalog
│   ├── ContentView.swift                              <- Main SwiftUI view
│   ├── {{ cookiecutter.target_name }}App.swift        <- Main app entry point
│   └── Preview Content
│       └── Preview Assets.xcassets                    <- Preview asset catalog
├── {{ cookiecutter.target_name }}.xcodeproj           <- Xcode project file
├── {{ cookiecutter.target_name }}Tests                <- Main app target tests directory
│   └── {{ cookiecutter.target_name }}Tests.swift      <- Main app target tests file
├── {{ cookiecutter.target_name }}UITests              <- Main app target UI tests directory
│   └── {{ cookiecutter.target_name }}UITests.swift    <- Main app target UI tests file
├── README.md                                          <- The top-level README for the project.
└── run-tests.sh                                       <- Convenience script for running tests locally
```

## Customizing the Template

See [CONTRIBUTING.md](CONTRIBUTING.md) for information about the project implementation
and how to setup your development environment to begin customizing the template.

## License

[MIT](LICENSE)
