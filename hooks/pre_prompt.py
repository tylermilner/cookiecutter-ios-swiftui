import sys
import subprocess

def is_xcodegen_installed() -> bool:
    print("Checking for XcodeGen...")
    try:
        subprocess.run(["xcodegen", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    if not is_xcodegen_installed():
        print("ERROR: XcodeGen is not installed. Please install it using `brew install xcodegen`.")
        sys.exit(1)

    print("Pre-prompt script complete")
