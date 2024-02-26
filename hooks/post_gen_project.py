import sys
import subprocess

def run_xcodegen() -> None:
    print("Running XcodeGen...")
    subprocess.run(["xcodegen"], check=True)

if __name__ == "__main__":
    # Generate the Xcode project using XcodeGen
    run_xcodegen()

    # TODO: Run tests using Fastlane
    # TODO: Initialize git repo (see example: https://github.com/riteshhgupta/swift-cookiecutter/blob/master/cookiecutter/hooks/post_gen_project.sh)
    # TODO: Remove XcodeGen `project.yml` file

    print("Post-gen script complete")
