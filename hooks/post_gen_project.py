"""Post-gen script that runs after cookiecutter generates the project."""

import subprocess
from pathlib import Path


def run_xcodegen() -> None:
    """Run XcodeGen to generate an Xcode project."""
    print("Running XcodeGen...")
    subprocess.run(["xcodegen"], check=True)


def initialize_git_repo() -> None:
    """Initialize a git repository in the current directory."""
    print("Initializing git repository...")
    subprocess.run(["git", "-c", "init.defaultBranch=main", "init"], check=True)
    subprocess.run(["git", "add", "-A", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)


def remove_xcodegen_yml() -> None:
    """Remove the XcodeGen `project.yml` file from the current directory."""
    print("Removing XcodeGen `project.yml` file...")
    Path("project.yml").unlink()


def open_xcode_project() -> None:
    """Open the generated Xcode project."""
    print("Opening Xcode project...")
    xcode_project = "{{ cookiecutter.__project_name_no_spaces }}"
    subprocess.run(["open", f"{xcode_project}.xcodeproj"], check=True)


def run_bundler() -> None:
    """Run Bundler to install project dependencies."""
    print("Running Bundler...")
    subprocess.run(["bundle", "install"], check=True)


def run_tests() -> None:
    """Run project tests."""
    print("Running tests...")
    subprocess.run(["./run-tests.sh"], check=True)


if __name__ == "__main__":
    # Generate the Xcode project using XcodeGen
    run_xcodegen()

    # Remove XcodeGen `project.yml` file now that the Xcode project has been generated
    if {{cookiecutter.remove_xcodegen_yml}}:  # type: ignore[name-defined] # noqa: F821 (ignore "cookiecutter not defined" errors)
        remove_xcodegen_yml()

    # Initialize git repository
    if {{cookiecutter.initialize_git_repo}}:  # type: ignore[name-defined] # noqa: F821 (ignore "cookiecutter not defined" errors)
        initialize_git_repo()

    # Open the generated Xcode project
    if {{cookiecutter.open_xcode_project}}:  # type: ignore[name-defined] # noqa: F821 (ignore "cookiecutter not defined" errors)
        open_xcode_project()

    # Run the tests for the generated project
    if {{cookiecutter.run_tests}}:  # type: ignore[name-defined] # noqa: F821 (ignore "cookiecutter not defined" errors)
        run_bundler()
        run_tests()

    print("Post-gen script complete")
