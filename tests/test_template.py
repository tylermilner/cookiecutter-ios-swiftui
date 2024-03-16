import os
import pytest

# - Test Fixtures
# The `cookies` fixture is provided by the `pytest-cookies` plugin to give an easy way to generate the project
# The `baked_cookies` fixture below is a custom fixture that uses the `cookies` fixture to automatically generate the project with defaults appropriate for testing

@pytest.fixture
def baked_cookies(cookies):
    result = cookies.bake(extra_context={"open_xcode_project": False})
    assert result.exit_code == 0
    assert result.exception is None
    return result

# - Test Cases

def test_project_generation_file_structure(baked_cookies):
    project_path = baked_cookies.project_path

    # Check that the project directory was created
    assert os.path.isdir(project_path)
    assert os.path.basename(project_path) == "my-app"

    # Check that all expected files exist
    expected_file_paths = [
        ".gitignore",
        "MyApp/Assets.xcassets/AccentColor.colorset/Contents.json",
        "MyApp/Assets.xcassets/AppIcon.appiconset/Contents.json",
        "MyApp/Assets.xcassets/Contents.json",
        "MyApp/ContentView.swift",
        "MyApp/MyAppApp.swift",
        "MyApp/Preview Content/Preview Assets.xcassets/Contents.json",
        "MyApp.xcodeproj/project.pbxproj",
        "MyApp.xcodeproj/project.xcworkspace/contents.xcworkspacedata",
        "MyAppTests/MyAppTests.swift",
        "MyAppUITests/MyAppUITests.swift",
        "MyAppUITests/MyAppUITestsLaunchTests.swift",
        "README.md"
    ]

    for file_path in expected_file_paths:
        full_file_path = os.path.join(project_path, file_path)
        assert os.path.isfile(full_file_path), f"File not found: {full_file_path}"

    
    # Check that no unexpected files exist
    unexpected_files = []
    ignored_files = [
        ".DS_Store",
        "MyApp/.DS_Store",
        "MyApp/Assets.xcassets/.DS_Store",
        "MyApp/Preview Content/.DS_Store",
    ]

    for root, dirs, files, in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(file_path, project_path)

            if relative_file_path not in expected_file_paths and relative_file_path not in ignored_files:
                unexpected_files.append(relative_file_path)

    assert not unexpected_files, f"Unexpected files found: {unexpected_files}"
