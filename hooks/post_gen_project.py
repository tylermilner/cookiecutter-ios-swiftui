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

    print("Post-gen script complete")
