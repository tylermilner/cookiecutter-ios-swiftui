# Contributing

[fork]: https://github.com/tylermilner/cookiecutter-ios-swiftui/fork
[pr]: https://github.com/tylermilner/cookiecutter-ios-swiftui/compare
[code-of-conduct]: CODE_OF_CONDUCT.md

Hi there! We're thrilled that you'd like to contribute to this project. Your
help is essential for keeping it great.

Contributions to this project are
[released](https://help.github.com/articles/github-terms-of-service/#6-contributions-under-repository-license)
to the public under the [project's open source license](LICENSE).

Please note that this project is released with a [Contributor Code of
Conduct][code-of-conduct]. By participating in this project you agree to abide
by its terms.

## About This Project

### Cookiecutter

This project is a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
template for quickly spinning up iOS apps.

Cookiecutter is a templating tool written in Python that uses a special `{{
variable_name }}` syntax to automatically replace variables in template files
when run. In this template, the main files involved are:

- `cookiecutter.json` - A configuration file that contains the variables that
  the user is prompted to input when generating the template, along with their
  default values.
- `{{ cookiecutter.project_root }}` - A directory containing the source files
  for the iOS project template.
- `hooks` - A directory containing the pre- and post-run hooks that are executed
  before and after the template is generated.

For more information, see the [Cookiecutter
documentation](https://cookiecutter.readthedocs.io/en/stable/overview.html).

### XcodeGen

In addition to Cookiecutter, [XcodeGen](https://github.com/yonaskolb/XcodeGen)
is used to generate the final Xcode project.

This differs from some other iOS Cookiecutter templates where the Xcode project
file is manually marked up with Cookiecutter `{{ variable_name }}` replacements.
Having these raw Cookiecutter variables inside of the `xcodeproj` prevents Xcode
from opening the file directly, which means you're on the hook to make all of
the edits to the `xcodeproj` file manually as you continue to build out your
template by adding files, adjusting build settings, etc.

By using XcodeGen, Cookiecutter first runs its replacements inside of the
`project.yml` file, which is then used to generate a fresh Xcode project as part
of a post-run step. From there, the `project.yml` file can be discarded or kept,
depending on if there is a desire to continue using XcodeGen on an ongoing basis
in the generated project.

## Making Code Changes

In order to customize or make changes to the project template, you'll first need
to set up your development environment and then install the project's
dependencies.

### Quick Start

Assuming you have Homebrew and `pyenv` installed, you can quickly get started using
`make` and the targets defined in the `Makefile`. If you don't have Homebrew and
`pyenv` installed, see the [Manual Steps](#manual-steps) section below.

1. Setup the Python environment:

    ```Shell
    make setup
    ```

2. Install the project's dependencies:

    ```Shell
    make install
    ```

3. Make changes to the template files in the `{{ cookiecutter.project_root }}` directory,
then regenerate the project:

    ```Shell
    make generate
    ```

    or

    ```Shell
    make generate-with-inputs
    ```

4. Add or update the tests, then run them:

    ```Shell
    make test
    ```

5. Run the linters and formatters:

    ```Shell
    make lint
    ```

### Manual Steps

#### Development Environment Setup

##### Homebrew

This guide assumes that you already have [Homebrew](https://brew.sh) installed.
If you aren't using Homebrew, you will need adjust the setup steps accordingly.

##### Python

If you already have Python and `pipenv` installed, skip ahead to [Installing
Project Dependencies](#installing-project-dependencies). Otherwise, follow the
instructions below to get your Python environment set up.

###### pyenv

In order to avoid using the system Python, use Homebrew to install
[pyenv](https://github.com/pyenv/pyenv) for Python version management:

```Shell
brew install pyenv
```

Complete the `pyenv` [post-install
steps](https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv)
according to your Shell type (example below for `zsh`):

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

Then, use `pyenv` to install the version of Python in use by the project (i.e.
`.python-version` file):

```Shell
pyenv install
```

###### Pipenv

Once Python is installed, install [pipenv](https://pipenv.pypa.io/en/latest/):

```Shell
pip install pipenv
```

#### Installing Project Dependencies

The project has both Python (e.g. Cookiecutter) and non-Python (e.g. XcodeGen)
project dependencies that will need to be installed.

##### Python Project Dependencies

Install the project's Python-based development dependencies using `pipenv`:

```Shell
pipenv install --dev
```

##### Non-Python Project Dependencies

The only non-Python project dependency is
[XcodeGen](https://github.com/yonaskolb/XcodeGen) so that a final Xcode project
can be generated. Install it using Homebrew:

```Shell
brew install xcodegen
```

#### Making Changes to the iOS Template

Make updates to the template files in the `{{ cookiecutter.project_root }}`
directory as necessary.

After making changes, regenerate the project locally by running Cookiecutter
against the repository directory, applying the `--overwrite-if-exists` flag to
automatically overwrite the previous output and optionally the `--no-input` flag
to skip needing to provide user input:

```Shell
pipenv run cookiecutter . --overwrite-if-exists --no-input
```

Note that the `pipenv run` command is used to ensure that the project's
`cookiecutter` dependency from inside the Python virtual environment is used.
See below for more information about Python virtual environments using `pipenv`.

##### Python Virtual Environments

From here on, you'll want to prefix any commands that require the project's
dependencies with `pipenv run` so that the project's dependencies in the virtual
environment are used (e.g. invoking `cookiecutter` to generate the template or
`pytest` to run the tests).

Alternatively, you can also manually enter the virtual environment before
invoking project dependencies:

```Shell
pipenv shell
```

Once the virtual environment is active, you will see that your terminal output
is prefixed with the name of the virtual environment (e.g.
`(cookiecutter-ios-swiftui)`). From here, you can run project dependencies like
`cookiecutter` directly, without needing to prefix the command with `pipenv
run`.

As an aside, since you've likely already installed Cookiecutter globally on your
system using Homebrew, you technically don't _need_ to enter the virtual
environment to run the `cookiecutter` command to generate the template. However,
as a best practice, it's still recommended to make sure to run the
`cookiecutter` command from within the virtual environment, either prefixing the
command with `pipenv run` or manually entering the virtual environment with
`pipenv shell`.

In order to return to your shell's main environment, exit the virtual
environment:

```Shell
exit
```

If you ever need to remove the virtual environment so that it can be recreated
using the `pip install --dev` command, you can do so using the following
command:

```Shell
pipenv --rm
```

#### Running Tests

This project uses [pytest](https://github.com/pytest-dev/pytest) to unit test
the template generation process. Run the tests by entering the virtual
environment and running `pytest`, or by using `pipenv run`:

```Shell
pipenv run pytest
```

For convenience, you can also run the tests by executing the `run-tests.sh`
script:

```Shell
./run-tests.sh
```

#### Linting

This project uses [ruff](https://github.com/astral-sh/ruff) for linting and
formatting. Run the linter by entering the virtual environment and running `ruff
--fix` and `ruff format`, or by using `pipenv run`:

```Shell
pipenv run ruff --fix
pipenv run ruff format
```

For convenience, you can also run the linter by executing the `lint.sh` script:

```Shell
./lint.sh
```

##### Additional Linters

There are some additional linters that are run via the [super-linter action](https://github.com/super-linter/super-linter)
in the CI [Lint workflow](.github/workflows/linter.yml), which can be helpful
to run locally.

###### markdownlint

Running [markdownlint](https://github.com/DavidAnson/markdownlint) locally:

1. Install markdownlint (e.g. using Homebrew):

    ```Shell
    brew install markdownlint-cli
    ```

2. Run markdownlint against the Markdown files in the repository:

    ```Shell
    markdownlint --config .github/linters/.markdown-lint.yml --fix .
    ```

###### yamllint

Running [yamllint](https://github.com/adrienverge/yamllint) locally:

1. Install yamllint (e.g. using Homebrew):

    ```Shell
    brew install yamllint
    ```

2. Run yamllint against the YAML files in the repository:

    ```Shell
    yamllint --config-file .github/linters/.yaml-lint.yml .
    ```

##### Pre-Commit Hooks

A `.pre-commit-config.yaml` has been setup to run the linters as [pre-commit](https://pre-commit.com)
hooks. To install the pre-commit hooks, run the following command:

```Shell
pipenv run pre-commit install
```

Run the pre-commit hooks manually to verify everything is working:

```Shell
pipenv run pre-commit run --all-files
```

###### Adding Additional Pre-Commit Hooks

Add additional pre-commit hooks to `.pre-commit-config.yaml` and then run
`pre-commit install` to install them:

```Shell
pipenv run pre-commit install
```

Once installed, verify the new hooks are working as expected by running them
against all files:

```Shell
pipenv run pre-commit run --all-files
```

###### Updating Pre-Commit Hooks

Since the pre-commit hooks are provided by external repositories, they don't
automatically update with other development dependencies like `ruff` or `mypy`.
To quickly update the pre-commit hooks to their latest versions, run the
following command:

```Shell
pipenv run pre-commit autoupdate
```

### Debugging

When running tests, use the `-s` or `--capture=no` flag to disable output
capture and see the output of the tests, which will make any `print()`
statements in your tests visible:

```Shell
pipenv run pytest -s
```

## Submitting a pull request

1. [Fork][fork] and clone the repository
2. Configure and install the dependencies: `pipenv install --dev`
3. Make sure the tests pass on your machine: `./run-tests.sh`
4. Create a new branch: `git checkout -b my-branch-name`
5. Make your change, add tests, and make sure the tests still pass
6. Do one final check to ensure all tests, linter, and compilation steps pass:
   `./run-tests.sh && ./lint.sh`
7. Push to your fork and [submit a pull request][pr]
8. Pat your self on the back and wait for your pull request to be reviewed and
   merged.

Here are a few things you can do that will increase the likelihood of your pull
request being accepted:

- Follow the style guide style by running the linter `./lint.sh`.
- Write tests.
- Keep your change as focused as possible. If there are multiple changes you
  would like to make that are not dependent upon each other, consider submitting
  them as separate pull requests.
- Write a [good commit
  message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

## Creating a Release

When it comes time to create a new release, repository maintainers should follow
the steps below to create and publish a new release.

### Versioning

For versioning, we are following the [recommended versioning
documentation](https://github.com/actions/toolkit/blob/master/docs/action-versioning.md)
available in GitHub's [actions/toolkit](https://github.com/actions/toolkit)
repository.

### Automated Release

- [ ] **TODO**: Add automated release instructions

### Manual Release

Perform the following steps to create a manual release:

1. Make sure all desired changes have been pushed to the `main` branch.
2. Create a `release/*` branch off of `main` (e.g. `release/v1.0.1`).
3. Update the `version` in `TBD` to the desired version.
4. Run `pipenv install --dev` to make sure the `Pipfile.lock` file is
   up-to-date.
5. Run `./run-tests.sh && ./lint.sh` one last time to make sure all tests,
   linters, etc. pass.
6. Create a pull request from the `release/*` branch to `main`.
7. Once the pull request is merged, create a new release targeted on `main` in
   the GitHub UI. Make sure to set it to create the corresponding tag on publish
   (e.g. `v1.0.1`) and keep the "Publish this Action to the GitHub Marketplace"
   option checked.
8. Once the release has been published on GitHub, switch back to the `main`
   branch and pull down any changes.
9. Update the major version tag to point the latest release, which should look
   something like the following (replacing "v1" if publishing a different major
   version tag):

```Shell
git tag -fa v1 -m "Update v1 tag"
git push origin v1 --force
```

## Resources

- [How to Contribute to Open
  Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com)
- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/en/latest/)
