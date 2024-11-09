"""Test the template generation process."""

from datetime import datetime
from fnmatch import fnmatch
from pathlib import Path
from re import match

import pytest
from pytest_cookies.plugin import Cookies  # type: ignore[import-untyped]
from pytest_cookies.plugin import Result as BakeResult
from yaml import safe_load as yaml_safe_load

# - Constants


PROJECT_NAME = "Demo App"
PROJECT_PATH = "demo-app"
APP_TARGET_NAME = "DemoApp"
APP_TESTS_TARGET_NAME = "DemoAppTests"
APP_UITESTS_TARGET_NAME = "DemoAppUITests"

# - Test Fixtures


@pytest.fixture
def baked_cookies(cookies: Cookies) -> BakeResult:
    """Generate a project template with defaults appropriate for testing, using the
    'cookies' fixture provided by pytest-cookies.
    """
    result = cookies.bake(
        extra_context={
            "project_name": PROJECT_NAME,
            "open_xcode_project": False,
            "remove_xcodegen_yml": False,
            "initialize_git_repo": False,
        },
    )
    assert result.exit_code == 0
    assert result.exception is None
    return result


# - Test Cases


def test_default_configuration(cookies: Cookies) -> None:
    """Test the default values in the cookiecutter.json file."""
    # Arrange
    # Today's date in format M/D/YY
    date = datetime.now().strftime(  # noqa: DTZ005 - ignore "datetime.now() called without a `tz`` argument" warning
        "%-m/%-d/%y"
    )

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
    assert context["deployment_target"] == "18.1"
    assert context["simulator_name"] == "iPhone 16"
    assert context["full_name"] == "First Last"
    assert context["date"] == date
    assert not context[
        "open_xcode_project"
    ]  # False because of the extra_context override
    assert context["remove_xcodegen_yml"]
    assert context["initialize_git_repo"]


def test_project_generation_file_structure(baked_cookies: BakeResult) -> None:
    """Test that the project generation completes successfully with the expected files
    on disk.
    """
    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify that the project directory was created
    assert Path(project_path).is_dir()
    assert Path(project_path).name == PROJECT_PATH

    # Verify that all expected files exist
    expected_file_paths = [
        ".github/workflows/test.yml",
        ".gitignore",
        "fastlane/Appfile",
        "fastlane/Fastfile",
        "Gemfile",
        "Gemfile.lock",
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
        full_file_path = Path(project_path) / file_path
        assert Path(full_file_path).is_file(), f"File not found: {full_file_path}"

    # Verify that no unexpected files exist
    unexpected_files = []
    ignored_patterns = [
        "*.DS_Store",
    ]

    for (
        root,
        _,
        files,
    ) in project_path.walk():
        for file in files:
            path = Path(root) / file
            relative_file_path = path.relative_to(project_path).as_posix()

            if relative_file_path not in expected_file_paths and not any(
                fnmatch(file, pattern) for pattern in ignored_patterns
            ):
                unexpected_files.append(relative_file_path)

    assert not unexpected_files, f"Unexpected files found: {unexpected_files}"


def test_project_name_replaced(baked_cookies: BakeResult) -> None:
    """Test that project_name is replaced correctly in all necessary files."""
    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify project.yml contents
    with Path.open(Path(project_path) / "project.yml") as file:
        project_yml = yaml_safe_load(file)
        assert project_yml["name"] == APP_TARGET_NAME

    # Verify README contents
    with Path.open(Path(project_path) / "README.md") as file:
        readme = file.read()
        assert f"# {PROJECT_NAME}" in readme


def check_swift_files_for_text(
    source_directory: Path,
    pattern: str,
    line_number: int,
) -> None:
    """Check Swift source files for header comment with target name."""
    for root, _, files in source_directory.walk():
        for file in files:
            if file.endswith(".swift"):
                with Path.open(Path(root) / file) as swift_file:
                    lines = [next(swift_file) for x in range(line_number + 1)]
                    assert match(pattern, lines[line_number].strip()), (
                        f"File {file} does not have expected text pattern {pattern} on "
                        "line {line_number}"
                    )


def test_target_name_replaced(baked_cookies: BakeResult) -> None:
    """Test that target_name is replaced correctly in all necessary files."""
    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify project.yml contents
    with Path.open(Path(project_path) / "project.yml") as file:
        project_yml = yaml_safe_load(file)

        assert APP_TARGET_NAME in project_yml["targets"]
        app_target = project_yml["targets"][APP_TARGET_NAME]
        assert APP_TARGET_NAME in app_target["sources"]
        assert (
            f"{APP_TARGET_NAME}/Preview Content"
            in app_target["settings"]["base"]["DEVELOPMENT_ASSET_PATHS"]
        )

        assert APP_TESTS_TARGET_NAME in project_yml["targets"]
        app_tests_target = project_yml["targets"][APP_TESTS_TARGET_NAME]
        assert APP_TESTS_TARGET_NAME in app_tests_target["sources"]
        assert APP_TARGET_NAME in app_tests_target["dependencies"][0]["target"]
        assert (
            APP_TESTS_TARGET_NAME
            in app_tests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]
        )

        assert APP_UITESTS_TARGET_NAME in project_yml["targets"]
        app_uitests_target = project_yml["targets"][APP_UITESTS_TARGET_NAME]
        assert APP_UITESTS_TARGET_NAME in app_uitests_target["sources"]
        assert APP_TARGET_NAME in app_uitests_target["dependencies"][0]["target"]
        assert (
            APP_UITESTS_TARGET_NAME
            in app_uitests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]
        )

    # Verify Fastfile contents
    with Path.open(Path(project_path) / "fastlane/Fastfile") as file:
        fastfile = file.read()
        assert f'scheme = "{APP_TARGET_NAME}"' in fastfile
        assert f'target = "{APP_TARGET_NAME}"' in fastfile

    # Verify target name header comment in Swift source files for each target
    targets = [APP_TARGET_NAME, APP_TESTS_TARGET_NAME, APP_UITESTS_TARGET_NAME]
    for target in targets:
        target_directory = Path(project_path) / target
        check_swift_files_for_text(target_directory, f"//  {target}", 2)

    # Verify string replacements for main app source file
    with Path.open(
        Path(project_path) / APP_TARGET_NAME / f"{APP_TARGET_NAME}App.swift",
    ) as file:
        app_swift = file.read()
        assert f"//  {APP_TARGET_NAME}App.swift" in app_swift
        assert f"struct {APP_TARGET_NAME}App: App" in app_swift
        assert f"extension {APP_TARGET_NAME}" in app_swift


def test_organization_name_replaced(baked_cookies: BakeResult) -> None:
    """Test that organization_name is replaced correctly in all necessary files."""
    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify project.yml contents
    with Path.open(Path(project_path) / "project.yml") as file:
        project_yml = yaml_safe_load(file)

        app_tests_target = project_yml["targets"][APP_TESTS_TARGET_NAME]
        assert (
            f"com.example.{APP_TESTS_TARGET_NAME}"
            in app_tests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]
        )

        app_uitests_target = project_yml["targets"][APP_UITESTS_TARGET_NAME]
        assert (
            f"com.example.{APP_UITESTS_TARGET_NAME}"
            in app_uitests_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]
        )


def test_bundle_identifier_replaced(baked_cookies: BakeResult) -> None:
    """Test that bundle_identifier is replaced correctly in all necessary files."""
    # Arrange
    bundle_identifier_suffix = APP_TARGET_NAME.lower()

    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify project.yml contents
    with Path.open(Path(project_path) / "project.yml") as file:
        project_yml = yaml_safe_load(file)

        app_target = project_yml["targets"][APP_TARGET_NAME]
        assert (
            f"com.example.{bundle_identifier_suffix}"
            in app_target["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"]
        )


# Test deployment target
def test_deployment_target_replaced(baked_cookies: BakeResult) -> None:
    """Test that deployment_target is replaced correctly in all necessary files."""
    # Arrange
    expected_deployment_target = "18.1"

    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify project.yml contents
    with Path.open(Path(project_path) / "project.yml") as file:
        project_yml = yaml_safe_load(file)

        ios_deployment_target = project_yml["options"]["deploymentTarget"]["iOS"]
        assert ios_deployment_target == expected_deployment_target


# Test simulator name
def test_simulator_name_replaced(baked_cookies: BakeResult) -> None:
    """Test that simulator_name is replaced correctly in all necessary files."""
    # Arrange
    expected_simulator_name = "iPhone 16"

    # Act
    project_path = baked_cookies.project_path

    # Assert
    # Verify Fastfile contents
    with Path.open(Path(project_path) / "fastlane/Fastfile") as file:
        fastfile = file.read()
        assert f'default_test_device = "{expected_simulator_name}"' in fastfile


def test_full_name_replaced(baked_cookies: BakeResult) -> None:
    """Test that full_name is replaced correctly in all necessary files."""
    # Arrange
    full_name = "First Last"

    # Act
    project_path = baked_cookies.project_path

    # Assert
    check_swift_files_for_text(project_path, f"//  Created by {full_name} on .*", 4)


def test_date_replaced(cookies: Cookies) -> None:
    """Test that date is replaced correctly in all necessary files."""
    # Arrange
    date = "1/1/24"

    # Act
    result = cookies.bake(extra_context={"open_xcode_project": False, "date": date})

    # Assert
    project_path = result.project_path
    check_swift_files_for_text(project_path, f"//  Created by .* on {date}", 4)


def test_remove_xcodegen_yml(cookies: Cookies) -> None:
    """Test that the XcodeGen YML file is removed correctly."""
    # Act
    result = cookies.bake(
        extra_context={"open_xcode_project": False, "remove_xcodegen_yml": True},
    )

    # Assert
    project_path = result.project_path
    assert not Path.is_file(Path(project_path) / "project.yml")


def test_initialize_git_repo(cookies: Cookies) -> None:
    """Test that the Git repository is initialized correctly."""
    # Act
    result = cookies.bake(
        extra_context={"open_xcode_project": False, "initialize_git_repo": True},
    )

    # Assert
    project_path = result.project_path
    assert Path.is_dir(Path(project_path) / ".git")
