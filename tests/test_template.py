import os
import pytest
import re
import yaml

# - Test Fixtures
# The `cookies` fixture provided by the `pytest-cookies` plugin automatically generates/cleans up a project directory for each test case
# The `baked_cookies` fixture below is a custom fixture that uses the `cookies` fixture to automatically generate the project with defaults appropriate for testing

@pytest.fixture
def baked_cookies(cookies):
    result = cookies.bake(extra_context={"open_xcode_project": False, "remove_xcodegen_yml": False})
    assert result.exit_code == 0
    assert result.exception is None
    return result

# - Test Cases

# Test that the project generation completes successfully with the expected files on disk
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
        "project.yml",
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

# Test that project_name is replaced correctly in all necessary files
def test_project_name_replaced(baked_cookies):
    project_path = baked_cookies.project_path

    # Verify project.yml contents
    with open(os.path.join(project_path, "project.yml")) as file:
        project_yml = yaml.safe_load(file)
        assert project_yml["name"] == "MyApp"

    # Verify README contents
    with open(os.path.join(project_path, "README.md")) as file:
        readme = file.read()
        assert "# My App" in readme

# Helper function to check Swift source files for header comment with target name
def check_swift_source_files_for_target_name_header_comment(project_path, target_name):
        for root, dirs, files in os.walk(os.path.join(project_path, target_name)):
            for file in files:
                if file.endswith(".swift"):
                    with open(os.path.join(root, file), 'r') as swift_file:
                        lines = [next(swift_file) for x in range(3)]  
                        assert re.match(f"//  {target_name}", lines[2].strip()), f"File {file} does not match pattern in line 3"

# Test that target_name is replaced correctly in all necessary files
def test_target_name_replaced(baked_cookies):
    app_target_name = "MyApp"
    app_tests_target_name = "MyAppTests"
    app_uitests_target_name = "MyAppUITests"
    project_path = baked_cookies.project_path
    
    # Verify project.yml contents
    with open(os.path.join(project_path, "project.yml")) as file:
        project_yml = yaml.safe_load(file)

        assert app_target_name in project_yml["targets"]
        app_target = project_yml["targets"][app_target_name]
        assert app_target_name in app_target["sources"]
        assert f"{app_target_name}/Preview Content" in app_target["settings"]["base"]["DEVELOPMENT_ASSET_PATHS"]

        assert app_tests_target_name in project_yml["targets"]
        app_tests_target = project_yml["targets"][app_tests_target_name]
        assert app_tests_target_name in app_tests_target["sources"]
        assert app_target_name in app_tests_target["dependencies"][0]["target"]
        assert app_tests_target_name in app_tests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]

        assert app_uitests_target_name in project_yml["targets"]
        app_uitests_target = project_yml["targets"][app_uitests_target_name]
        assert app_uitests_target_name in app_uitests_target["sources"]
        assert app_target_name in app_uitests_target["dependencies"][0]["target"]
        assert app_uitests_target_name in app_uitests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]

    # Verify target name header comment in Swift source files for each target
    targets = [app_target_name, app_tests_target_name, app_uitests_target_name]
    for target in targets:
        check_swift_source_files_for_target_name_header_comment(project_path, target)

    # Verify remaining header comments for main app source file
    with open(os.path.join(project_path, app_target_name, f"{app_target_name}App.swift")) as file:
        app_swift = file.read()
        assert f"//  {app_target_name}App.swift" in app_swift
        assert f"struct {app_target_name}App: App" in app_swift
