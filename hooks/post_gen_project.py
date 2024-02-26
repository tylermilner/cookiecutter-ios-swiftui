import os
import subprocess

def run_xcodegen() -> None:
    print("Running XcodeGen...")
    subprocess.run(["xcodegen"], check=True)

def remove_xcodegen_yml() -> None:
    print("Removing XcodeGen `project.yml` file...")
    os.remove("project.yml")

if __name__ == "__main__":
    # Generate the Xcode project using XcodeGen
    run_xcodegen()

    # TODO: Run tests using Fastlane
    # TODO: Initialize git repo (see example: https://github.com/riteshhgupta/swift-cookiecutter/blob/master/cookiecutter/hooks/post_gen_project.sh)

    # Remove XcodeGen `project.yml` file now that the Xcode project has been generated
    remove_xcodegen_yml()

    print("Post-gen script complete")
