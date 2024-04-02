import datetime
import fnmatch
import os
import pytest
import re
import yaml

# - Constants

PROJECT_NAME = "Demo App"
PROJECT_PATH = "demo-app"
APP_TARGET_NAME = "DemoApp"
APP_TESTS_TARGET_NAME = "DemoAppTests"
APP_UITESTS_TARGET_NAME = "DemoAppUITests"

# - Test Fixtures

# Automatically generate a project with defaults appropriate for testing
@pytest.fixture
def baked_cookies(cookies):
    # Generate the project using the 'cookies' fixture provided by pytest-cookies
    result = cookies.bake(extra_context={"project_name": PROJECT_NAME, "open_xcode_project": False, "remove_xcodegen_yml": False, "initialize_git_repo": False})
    assert result.exit_code == 0
    assert result.exception is None
    return result

# - Test Cases

# Test the default values in the cookiecutter.json file
def test_default_configuration(cookies):
    # Arrange
    # Today's date in format M/D/YY
    date = datetime.datetime.now().strftime("%-m/%-d/%y")

    # Act
    result = cookies.bake(extra_context={"open_xcode_project": False})

    # Assert
    context = result.context

    assert context["project_name"] == "My App"
    assert context["__project_name_no_spaces"] == "MyApp"
    assert context["__project_name_no_spaces_lowercase"] == "myapp"
    assert context["project_root"] == "my-app"
    assert context["target_name"] == "MyApp"
    assert context["organization_name"] == "Example"
    assert context["__organization_name_no_spaces_lowercase"] == "example"
    assert context["bundle_identifier"] == "com.example.myapp"
    assert context["full_name"] == "First Last"
    assert context["date"] == date
    assert context["open_xcode_project"] == False # False because of the extra_context override
    assert context["remove_xcodegen_yml"] == True
    assert context["initialize_git_repo"] == True

# Test that the project generation completes successfully with the expected files on disk
def test_project_generation_file_structure(baked_cookies):
    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify that the project directory was created
    assert os.path.isdir(project_path)
    assert os.path.basename(project_path) == PROJECT_PATH

    # Verify that all expected files exist
    expected_file_paths = [
        ".github/workflows/test.yml",
        ".gitignore",
        "run-tests.sh",
        f"{APP_TARGET_NAME}/Assets.xcassets/AccentColor.colorset/Contents.json",
        f"{APP_TARGET_NAME}/Assets.xcassets/AppIcon.appiconset/Contents.json",
        f"{APP_TARGET_NAME}/Assets.xcassets/Contents.json",
        f"{APP_TARGET_NAME}/ContentView.swift",
        f"{APP_TARGET_NAME}/{APP_TARGET_NAME}App.swift",
        f"{APP_TARGET_NAME}/Preview Content/Preview Assets.xcassets/Contents.json",
        f"{APP_TARGET_NAME}.xcodeproj/project.pbxproj",
        f"{APP_TARGET_NAME}.xcodeproj/project.xcworkspace/contents.xcworkspacedata",
        f"{APP_TESTS_TARGET_NAME}/{APP_TESTS_TARGET_NAME}.swift",
        f"{APP_UITESTS_TARGET_NAME}/{APP_UITESTS_TARGET_NAME}.swift",
        "project.yml",
        "README.md",
    ]

    for file_path in expected_file_paths:
        full_file_path = os.path.join(project_path, file_path)
        assert os.path.isfile(full_file_path), f"File not found: {full_file_path}"

    # Verify that no unexpected files exist
    unexpected_files = []
    ignored_patterns = [
        "*.DS_Store",
    ]

    for root, dirs, files, in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(file_path, project_path)

            if relative_file_path not in expected_file_paths and not any(fnmatch.fnmatch(file, pattern) for pattern in ignored_patterns):
                unexpected_files.append(relative_file_path)

    assert not unexpected_files, f"Unexpected files found: {unexpected_files}"

# Test that project_name is replaced correctly in all necessary files
def test_project_name_replaced(baked_cookies):
    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify project.yml contents
    with open(os.path.join(project_path, "project.yml")) as file:
        project_yml = yaml.safe_load(file)
        assert project_yml["name"] == APP_TARGET_NAME

    # Verify README contents
    with open(os.path.join(project_path, "README.md")) as file:
        readme = file.read()
        assert f"# {PROJECT_NAME}" in readme

# Helper function to check Swift source files for header comment with target name
def check_swift_files_for_text(source_directory, pattern, line_number):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(".swift"):
                with open(os.path.join(root, file), 'r') as swift_file:
                    lines = [next(swift_file) for x in range(line_number + 1)]
                    assert re.match(pattern, lines[line_number].strip()), f"File {file} does not have expected text pattern {pattern} on line {line_number}"

# Test that target_name is replaced correctly in all necessary files
def test_target_name_replaced(baked_cookies):
    # Act
    project_path = baked_cookies.project_path
    
    # Assert
    # Verify project.yml contents
    with open(os.path.join(project_path, "project.yml")) as file:
        project_yml = yaml.safe_load(file)

        assert APP_TARGET_NAME in project_yml["targets"]
        app_target = project_yml["targets"][APP_TARGET_NAME]
        assert APP_TARGET_NAME in app_target["sources"]
        assert f"{APP_TARGET_NAME}/Preview Content" in app_target["settings"]["base"]["DEVELOPMENT_ASSET_PATHS"]

        assert APP_TESTS_TARGET_NAME in project_yml["targets"]
        app_tests_target = project_yml["targets"][APP_TESTS_TARGET_NAME]
        assert APP_TESTS_TARGET_NAME in app_tests_target["sources"]
        assert APP_TARGET_NAME in app_tests_target["dependencies"][0]["target"]
        assert APP_TESTS_TARGET_NAME in app_tests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]

        assert APP_UITESTS_TARGET_NAME in project_yml["targets"]
        app_uitests_target = project_yml["targets"][APP_UITESTS_TARGET_NAME]
        assert APP_UITESTS_TARGET_NAME in app_uitests_target["sources"]
        assert APP_TARGET_NAME in app_uitests_target["dependencies"][0]["target"]
        assert APP_UITESTS_TARGET_NAME in app_uitests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]

    # Verify target name header comment in Swift source files for each target
    targets = [APP_TARGET_NAME, APP_TESTS_TARGET_NAME, APP_UITESTS_TARGET_NAME]
    for target in targets:
        target_directory = os.path.join(project_path, target)
        check_swift_files_for_text(target_directory, f"//  {target}", 2)

    # Verify string replacements for main app source file
    with open(os.path.join(project_path, APP_TARGET_NAME, f"{APP_TARGET_NAME}App.swift")) as file:
        app_swift = file.read()
        assert f"//  {APP_TARGET_NAME}App.swift" in app_swift
        assert f"struct {APP_TARGET_NAME}App: App" in app_swift
        assert f"extension {APP_TARGET_NAME}" in app_swift

# Test that organization_name is replaced correctly in all necessary files
def test_organization_name_replaced(baked_cookies):
    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify project.yml contents
    with open(os.path.join(project_path, "project.yml")) as file:
        project_yml = yaml.safe_load(file)

        app_tests_target = project_yml["targets"][APP_TESTS_TARGET_NAME]
        assert f"com.example.{APP_TESTS_TARGET_NAME}" in app_tests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]

        app_uitests_target = project_yml["targets"][APP_UITESTS_TARGET_NAME]
        assert f"com.example.{APP_UITESTS_TARGET_NAME}" in app_uitests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]

# Test that bundle_identifier is replaced correctly in all necessary files
def test_bundle_identifier_replaced(baked_cookies):
    # Arrange
    bundle_identifier_suffix = APP_TARGET_NAME.lower()

    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify project.yml contents
    with open(os.path.join(project_path, "project.yml")) as file:
        project_yml = yaml.safe_load(file)

        app_target = project_yml["targets"][APP_TARGET_NAME]
        assert f"com.example.{bundle_identifier_suffix}" in app_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]

# Test that full_name is replaced correctly in all necessary files
def test_full_name_replaced(baked_cookies):
    # Arrange
    full_name = "First Last"

    # Act
    project_path = baked_cookies.project_path

    # Assert
    check_swift_files_for_text(project_path, f"//  Created by {full_name} on .*", 4)

def test_date_replaced(cookies):
    # Arrange
    date = "1/1/24"

    # Act
    result = cookies.bake(extra_context={"open_xcode_project": False, "date": date})

    # Assert
    project_path = result.project_path
    check_swift_files_for_text(project_path, f"//  Created by .* on {date}", 4)

def test_remove_xcodegen_yml(cookies):
    # Act
    result = cookies.bake(extra_context={"open_xcode_project": False, "remove_xcodegen_yml": True})

    # Assert
    project_path = result.project_path
    assert not os.path.isfile(os.path.join(project_path, "project.yml"))

def test_initialize_git_repo(cookies):
    # Act
    result = cookies.bake(extra_context={"open_xcode_project": False, "initialize_git_repo": True})

    # Assert
    project_path = result.project_path
    assert os.path.isdir(os.path.join(project_path, ".git"))

def test_run_tests_script(baked_cookies):
    # Act
    project_path = baked_cookies.project_path

    # Assert
    run_tests_script_path = os.path.join(project_path, "run-tests.sh")
    assert os.path.isfile(run_tests_script_path)

    with open(run_tests_script_path) as file:
        run_tests_script = file.read()

        assert f"-project {APP_TARGET_NAME}.xcodeproj" in run_tests_script
        assert f"-scheme {APP_TARGET_NAME}" in run_tests_script
