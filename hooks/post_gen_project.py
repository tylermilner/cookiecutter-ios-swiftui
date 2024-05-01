import os
import subprocess


def run_xcodegen() -> None:
    print("Running XcodeGen...")
    subprocess.run(["xcodegen"], check=True)


def initialize_git_repo() -> None:
    print("Initializing git repository...")
    subprocess.run(["git", "-c", "init.defaultBranch=main", "init"], check=True)
    subprocess.run(["git", "add", "-A", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)


def remove_xcodegen_yml() -> None:
    print("Removing XcodeGen `project.yml` file...")
    os.remove("project.yml")


def open_xcode_project() -> None:
    print("Opening Xcode project...")
    xcode_project = "{{ cookiecutter.__project_name_no_spaces }}"
    subprocess.run(["open", f"{xcode_project}.xcodeproj"], check=True)


if __name__ == "__main__":
    # Generate the Xcode project using XcodeGen
    run_xcodegen()

    # TODO: Run tests using Fastlane

    # Remove XcodeGen `project.yml` file now that the Xcode project has been generated
    if {{cookiecutter.remove_xcodegen_yml}}:  # noqa: F821 (ignore undefined name 'cookiecutter')
        remove_xcodegen_yml()

    # Initialize git repository
    if {{cookiecutter.initialize_git_repo}}:  # noqa: F821 (ignore undefined name 'cookiecutter')
        initialize_git_repo()

    # Open the generated Xcode project
    if {{cookiecutter.open_xcode_project}}:  # noqa: F821 (ignore undefined name 'cookiecutter')
        open_xcode_project()

    print("Post-gen script complete")
