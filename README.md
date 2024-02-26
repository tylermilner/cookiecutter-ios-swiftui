# cookiecutter-ios-swiftui

Cookiecutter template for jump-starting modern iOS apps using SwiftUI.

## Getting Started

Install Cookiecutter (e.g. using [Homebrew](https://brew.sh)):

```Shell
brew install cookiecutter
```

Run Cookiecutter against this repo:

```Shell
cookiecutter gh:tylermilner/cookiecutter-ios-swiftui
```

## About This Project

### Cookiecutter

This project is a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template for quickly spinning up iOS apps.

Cookiecutter is a templating tool written in Python that uses a special `{{ variable_name }}` syntax to automatically replace variables in template files when run. The main template code for the iOS project is located in the `{{ cookiecutter.project_root }}` directory.

### XcodeGen

In addition to Cookiecutter, [XcodeGen](https://github.com/yonaskolb/XcodeGen) is used to generate the final Xcode project.

This differs from some other iOS Cookiecutter templates where the Xcode project file is manually marked up with Cookiecutter `{{ variable_name }}` replacements. Having these raw Cookiecutter variables inside of the `xcodeproj` prevents Xcode from opening the file directly, which means you're on the hook to make all of the edits to the `xcodeproj` file manually as you continue to build out your template by adding files, adjusting build settings, etc.

By using XcodeGen, Cookiecutter first runs its replacements inside of the `project.yml` file, which is then used to generate a fresh Xcode project as part of a post-run step. From there, the `project.yml` file can be discarded or kept, depending on if there is a desire to continue using XcodeGen on an ongoing basis in the generated project.

### Generated Example Project

A generated version of this template that demonstrates the final project structure can be found at:

- [ ] TODO - Add link to generated output version of the template

#### Resulting Directory Structure

- [ ] TODO - document directory structure (see [this example](https://github.com/drivendata/cookiecutter-data-science#the-resulting-directory-structure))

## Contributing

In order to customize or make changes to the project template, you'll first need to set up your development environment and then install the project's dependencies.

### Development Environment Setup

If you already have Python and `pipenv` installed, skip ahead to [Installing Project Dependencies](#installing-project-dependencies). Otherwise, follow the instructions below to get your Python environment set up.

#### Homebrew

This guide assumes that you already have [Homebrew](https://brew.sh) installed. If you aren't using Homebrew, you will need adjust the setup steps accordingly.

#### Python

In order to avoid using the system Python, use Homebrew to install [pyenv](https://github.com/pyenv/pyenv) for Python version management:

```Shell
brew install pyenv
```

Complete the `pyenv` [post-install steps](https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv) according to your Shell type (example below for `zsh`):

```Shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

Restart your shell for the `PATH` changes to take effect:

```Shell
exec "$SHELL"
```

If you haven't already, navigate to the project directory:

```Shell
cd cookiecutter-ios-swiftui
```

Then, use `pyenv` to install the version of Python in use by the project (i.e. `.python-version` file):

```Shell
pyenv install
```

#### Pipenv

Once Python is installed, install [pipenv](https://pipenv.pypa.io/en/latest/):

```Shell
pip install pipenv
```

### Installing Project Dependencies

The project has both Python (e.g. Cookiecutter) and non-Python (e.g. XcodeGen) project dependencies that will need to be installed.

#### Python Project Dependencies

Install the project's Python-based development dependencies using `pipenv`:

```Shell
pipenv install --dev
```

#### Non-Python Project Dependencies

The only non-Python project dependency is [XcodeGen](https://github.com/yonaskolb/XcodeGen) so that a final Xcode project can be generated. Install it using Homebrew:

```Shell
brew install xcodegen
```

### Making Changes

Make updates to the template files in the `{{ cookiecutter.project_root }}` directory as necessary.

After making changes, regenerate the project locally by running Cookiecutter against the repo directory, applying the `--overwrite-if-exists` flag to automatically overwrite the previous output and optionally the `--no-input` flag to skip needing to provide user input:

```Shell
pipenv run cookiecutter . --overwrite-if-exists --no-input
```

Note that the `pipenv run` command is used to ensure that the project's `cookiecutter` dependency from inside the Python virtual environment is used. See below for more information about Python virtual environments using `pipenv`.

#### Python Virtual Environments

From here on, you'll want to prefix any commands that require the project's dependencies with `pipenv run` so that the project's dependencies in the virtual environment are used (e.g. invoking `cookiecutter` to generate the template or `pytest` to run the tests).

Alternatively, you can also manually enter the virtual environment before invoking project dependencies:

```Shell
pipenv shell
```

Once the virtual environment is active, you will see that your terminal output is prefixed with the name of the virtual environment (e.g. `(cookiecutter-ios-swiftui)`). From here, you can run project dependencies like `cookiecutter` directly, without needing to prefix the command with `pipenv run`.

As an aside, since you've likely already installed Cookiecutter globally on your system using Homebrew, you technically don't _need_ to enter the virtual environment to run the `cookiecutter` command to generate the template. However, as a best practice, it's still recommended to make sure to run the `cookiecutter` command from within the virtual environment, either prefixing the command with `pipenv run` or manually entering the virtual environment with `pipenv shell`.

In order to return to your shell's main environment, exit the virtual environment:

```Shell
exit
```

If you ever need to remove the virtual environment so that it can be recreated using the `pip install --dev` command, you can do so using the following command:

```Shell
pipenv --rm
```

### Running Tests

_TBD_

```Shell
pipenv run pytest
```

## Todo

This is currently a work in progress. Misc todos are listed below:

- [ ] TODO - validate bundle id format (see [this SO post](https://stackoverflow.com/a/55623269/4343618) for possible regex)
- [ ] TODO - add SwiftGen as a dependency
- [ ] TODO - use Python for hooks instead of shell scripts
