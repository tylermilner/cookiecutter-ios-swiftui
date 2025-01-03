# {{ cookiecutter.project_name }}

- [ ] TODO: Add a description of the project here.

## Getting Started

### Prerequisites

As this is an iOS app, you'll need to have a working development environment for
Apple applications. For this project, you'll need:

- Mac running the latest macOS.
- Latest version of Xcode installed.
- Ruby with `bundler` gem installed.

_TBD_: Expand on how where to get Xcode and how to install Ruby (via version manager
like `rbenv`) and `bundler`.

### Running the Project

- [ ] TODO: Fill in `git clone` repository URL below.

1. Clone/download this repository and open it:

    ```shell
    git clone ...
    ```

2. Install build dependencies:

    ```shell
    bundle install
    ```

3. Open `{{ cookiecutter.__project_name_no_spaces }}.xcodeproj` in Xcode.
4. Click "Run" or press `CMD` + `R` shortcut.

### Running Tests

Tests can be run inside of Xcode using the `CMD` + `U` shortcut or run via Fastlane:

```shell
bundle exec fastlane ios test
```

A convenience script is also available:

```shell
./run-tests.sh
```

### Initial Project Setup for CI/CD

If you want to utilize the Fastlane build automation tools to create builds, then
you'll need to do some initial setup for this project:

- Environment Variables
  - Setup local `.env` file
- Apple Developer Portal
  - Create App ID
- App Store Connect API Key
  - Issuer ID
  - Key ID
  - API key (base64 encoded)
- Code Signing Repository
  - HTTPS URL
  - Access token (e.g. HTTP "Basic" Authorization credentials from GitHub PAT)
  - Encryption passphrase
- Certificates and Provisioning Profiles
  - Setup certificates and provisioning profiles

#### Environment Variables

If it doesn't already exist, create an `.env` file by duplicating `.env.example`
and renaming it to `.env`.

This file will contain the necessary environment variables and secrets for running
CI/CD operations on your local machine. For running these operations on a remote
machine (e.g. CI system), these values will be set in the CI's secrets and variables
settings.

Note that because this `.env` file contains sensitive information, it is
**included** in the `.gitignore` to **prevent** it from being committed to the repository.

#### Apple Developer Portal

In order to create certificates and provisioning profiles, you'll need to create
an App ID in the Apple Developer Portal. This can be done manually or automatically
via fastlane `produce` and the `setup_app_id` lane:

1. Update the value of `FASTLANE_USER` in the `.env` file with the Apple ID for
your Apple Developer account.
2. Update the value of `FASTLANE_TEAM_ID` in the `.env` file with the Team ID for
your Apple Developer account.
3. Run the `setup_app_id` lane:

    ```shell
    bundle exec fastlane ios setup_app_id
    ```

When prompted, enter the verification code sent to your device to authenticate
with the Apple Developer Portal and create the App ID.

Under the hood, Fastlane's `produce` action [doesn't yet support the new App Store
Connect API](https://docs.fastlane.tools/app-store-connect-api/#supported-actionstools),
so it will use the older [two-factor authentication method](https://docs.fastlane.tools/getting-started/ios/authentication/#method-2-two-step-or-two-factor-authentication)
to authenticate with the Apple Developer Portal. If you need to clean up the authentication
cookie that gets stored, you can find it at `~/.fastlane/spaceship/[apple_id]/cookie`:

#### App Store Connect API Key

In order for Fastlane to automatically create and manage certificates and provisioning
profiles, you'll need to create an [App Store Connect API key](https://appstoreconnect.apple.com/access/integrations/api):

1. Create an App Store Connect Team API key with "Developer" access. Download the
key's `.p8` file once generated.
2. Get the base64 encoded value of the `.p8` file:

    ```shell
    cat <key-name>.p8 | base64
    ```

3. Update the value of `APP_STORE_CONNECT_API_KEY_KEY` in the `.env` file with the
base64 encoded value.
4. Update the value of `APP_STORE_CONNECT_API_KEY_KEY_ID` in the `.env` file with
the Key ID value shown in App Store Connect.
5. Update the `APP_STORE_CONNECT_API_KEY_ISSUER_ID` variable in the `.env` file
with the Issuer ID value shown in App Store Connect.

#### Code Signing Repository

Fastlane `match` is used to manage the code signing certificates and provisioning
profiles. Assuming you're using GitHub, create a repository to store these files
and configure the necessary environment variables:

1. Create a private repository to store the code signing certificates and provisioning
profiles (e.g. `{{ cookiecutter.project_root }}-certs`).
2. Update the value of `MATCH_GIT_URL` in the `.env` file with the HTTPS URL of the
repository. The SSH URL can also be used, but it can be more challenging to setup
on CI systems.
3. Generate a [Personal Access Token (PAT)](https://github.com/settings/personal-access-tokens)
with access scoped to the certificates repository. Configure the token's "Contents"
permission with _read and write_ access.
4. [Optional] Generate another PAT, this time configuring the "Contents" permission
with _read-only_ access. This token will be used for the CI system as an additional
safeguard to prevent certificates and profiles from accidentally being changed
by the CI build process.
5. Concatenate your GitHub username and the PAT together using a colon (e.g. `username:token`)
and then base64 encode the result to get your GitHub basic authentication credentials:

    ```shell
    echo -n username:token | base64
    ```

6. Update the value of `MATCH_GIT_BASIC_AUTHORIZATION` in the `.env` file with
the base64 encoded value.
7. Update the value of `MATCH_PASSWORD` in the `.env` file with a secure passphrase
that `match` will use to encrypt/decrypt the certificates.

#### Certificates and Provisioning Profiles

To generate the certificates and provisioning profiles using fastlane `match`,
use the `setup_certs` lane:

```shell
bundle exec fastlane ios setup_certs
```

If prompted, enter your Mac's login keychain password so that `match` can
save the certificates it generates to your keychain.

Note that development certificates created by `match` will have the name "Created
by API". This is due to a limitation in the App Store Connect API (see [here](https://github.com/fastlane/fastlane/discussions/20180)
for more information).

### Creating a Build

A build can be creating using Xcode or via Fastlane:

_TBD_: Document the build creation process.
