# cookiecutter-ios-swiftui

[![Tests](https://github.com/tylermilner/cookiecutter-ios-swiftui/actions/workflows/test.yml/badge.svg)](https://github.com/tylermilner/cookiecutter-ios-swiftui/actions/workflows/test.yml)
[![Deploy](https://github.com/tylermilner/cookiecutter-ios-swiftui/actions/workflows/deploy.yml/badge.svg)](https://github.com/tylermilner/cookiecutter-ios-swiftui/actions/workflows/deploy.yml)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for
jump-starting modern iOS apps using SwiftUI.

## Work in Progress

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

- [ ] Todo - document directory structure (see [this
  example](https://github.com/drivendata/cookiecutter-data-science#the-resulting-directory-structure))

## Customizing the Template

See [CONTRIBUTING.md](CONTRIBUTING.md) for information about the project implementation
and how to setup your development environment to begin customizing the template.

## License

[MIT](LICENSE)
