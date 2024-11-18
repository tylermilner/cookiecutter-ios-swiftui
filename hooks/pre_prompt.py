"""Pre-prompt script that runs before cookiecutter gets inputs from the user."""

import subprocess
import sys


def is_xcodegen_installed() -> bool:
    """Check if XcodeGen is installed."""
    print("Checking for XcodeGen...")
    try:
        subprocess.run(["xcodegen", "--version"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        return False
    else:
        return True


def is_git_installed() -> bool:
    """Check if Git is installed."""
    print("Checking for Git...")
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        return False
    else:
        return True


def is_bundler_installed() -> bool:
    """Check if Bundler is installed."""
    print("Checking for Bundler...")
    try:
        subprocess.run(["bundle", "--version"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        return False
    else:
        return True


if __name__ == "__main__":
    if not is_xcodegen_installed():
        print(
            "ERROR: XcodeGen is not installed. Please install it using `brew "
            "install xcodegen`.",
        )
        sys.exit(1)

    if not is_git_installed():
        print(
            "ERROR: Git is not installed. Please install it using `brew install git`.",
        )
        sys.exit(1)

    if not is_bundler_installed():
        print(
            "ERROR: Bundler is not installed. Please install it using `gem install "
            "bundler`.",
        )
        sys.exit(1)

    print("Pre-prompt script complete")
