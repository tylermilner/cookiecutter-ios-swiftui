# {{ cookiecutter.project_name }}

- [ ] TODO: Add a description of the project here.

## Getting Started

### Prerequisites

As this is an iOS app, you'll need to have a working development environment for
Apple applications. For this project, you'll need:

- Mac running the latest macOS.
- Latest version of Xcode installed.
- Homebrew with `mint` package installed.
- Ruby with `bundler` gem installed.

_TBD_: Expand on how where to get Xcode, how to install Homebrew and `mint`,
and how to install Ruby (via version manager like `rbenv`) and `bundler`.

### Running the Project

- [ ] TODO: Fill in `git clone` repo URL below.

1. Clone or download this repo - `git clone ...`.
2. Install build dependencies - `bundle install`.
3. Open `{{ cookiecutter.__project_name_no_spaces }}.xcodeproj` in Xcode.
4. Click "Run" or press `CMD` + `R` shortcut.

### Running Tests

Tests can be run inside of Xcode using the `CMD` + `U` shortcut or run via Fastlane:

```bash
bundle exec fastlane ios test
```

A convenience script is also available:

```bash
./run-tests.sh
```

### Initial Project Setup for CI/CD

If you're planning to build upon this repo and you want to utilize the Fastlane
build automation tools, you'll need to do some initial setup for this project.

#### Environment Variables

First, create an `.env` file that will contain the necessary environment variables
and secrets by duplicating the `.env.example` file and renaming it to `.env`.

Note that because this `.env` file will contain sensitive information, it is
included in the `.gitignore` file to prevent it from being committed to the repo.

#### App Store Connect API Key

In order for Fastlane to help with provisioning profiles and certificates, you'll
need to create an [App Store Connect API key](https://appstoreconnect.apple.com/access/integrations/api):

1. Create an App Store Connect Team API key with "Developer" access. Download the
key's `.p8` file once generated.
2. Get the base64 encoded value of the `.p8` file: `cat <key-name>.p8 | base64`.
3. Update the value of `APP_STORE_CONNECT_API_KEY_KEY` in the `.env` file with the
base64 encoded value.
4. Update the value of `APP_STORE_CONNECT_API_KEY_KEY_ID` in the `.env` file with
the value shown in App Store Connect.
5. Update the `APP_STORE_CONNECT_API_KEY_ISSUER_ID` variable in the `.env` file
with the value shown in App Store Connect.

### Creating a Build

A build can be creating using Xcode or via Fastlane:

_TBD_: Document the build creation process.
