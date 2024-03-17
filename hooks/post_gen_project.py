import os
import subprocess

def run_xcodegen() -> None:
    print("Running XcodeGen...")
    subprocess.run(["xcodegen"], check=True)

def remove_xcodegen_yml() -> None:
    print("Removing XcodeGen `project.yml` file...")
    os.remove("project.yml")

def open_xcode_project() -> None:
    print("Opening Xcode project...")
    xcode_project = "{{ cookiecutter.__project_name_no_spaces }}"
    subprocess.run(["open", f"{xcode_project}.xcodeproj"])

if __name__ == "__main__":
    # Generate the Xcode project using XcodeGen
    run_xcodegen()

    # TODO: Run tests using Fastlane
    # TODO: Initialize git repo (see example: https://github.com/riteshhgupta/swift-cookiecutter/blob/master/cookiecutter/hooks/post_gen_project.sh)

    # Remove XcodeGen `project.yml` file now that the Xcode project has been generated
    if {{ cookiecutter.remove_xcodegen_yml }} == True:
        remove_xcodegen_yml()

    # Open the generated Xcode project
    if {{ cookiecutter.open_xcode_project }} == True:
        open_xcode_project()

    print("Post-gen script complete")
