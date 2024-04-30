import sys
import subprocess


def is_xcodegen_installed() -> bool:
    print("Checking for XcodeGen...")
    try:
        subprocess.run(["xcodegen", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def is_git_installed() -> bool:
    print("Checking for Git...")
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    if not is_xcodegen_installed():
        print(
            "ERROR: XcodeGen is not installed. Please install it using `brew install xcodegen`."
        )
        sys.exit(1)

    if not is_git_installed():
        print(
            "ERROR: Git is not installed. Please install it using `brew install git`."
        )
        sys.exit(1)

    print("Pre-prompt script complete")
