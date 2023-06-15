# Lumynous GitHub Release Action
This action creates GitHub releases automatically.

## Usage

```yml
on:
  push:
    branches:
      - main

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Release
        uses: lumynou5/github-release-action@v1
        with:
          token: ${{github.token}}
```

In this example workflow, it'll create a release whenever push to `main` branch.
The version and the release note will be captured from the changelog following
[Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/).
And a Git tag will be created for the major revision, see [Inputs](#Inputs) for more information.

This is useful to automatically publish releases on pushing to the stable branch when using Git flow, etc.

## Inputs
- `token` (required)
  The GitHub token.
- `changelog`
  The path to the changelog. Default: `CHANGELOG.md`.
- `tag-template`
  The template of the Git tag. Default: `v{version}`.
- `major-tag-template`
  The template of the Git tag of the major version. Doesn't perform if the major version is 0.
  Default: `v{major}`. Empty for no major tag.
- `minor-tag-template`
  The template of the Git tag of the minor version. Default: `v{maojr}.{minor}`. Empty for no minor tag.
- `name-template`
  The template of the GitHub release. Default: `v{version}`.
- `is-draft`
  If the GitHub release is a draft. Default: `false`.

The following list shows the parameters that can be used in templates.
To use parameters, add a parameter name wrapping with braces to your template,
and it will be replaced with data from your changelog;
i.e. `{parameter-name}` will be replaced with the corresponding value.
- `version`
  The version.
- `major`
  The major version.
- `minor`
  The minor version.
- `patch`
  The patch version.
- `prerelease`
  The prerelease name or an empty string.
- `build`
  The build number or an empty string.
- `release-date`
  The release date.

## Outputs
The outputs include all the parameters of templates and the following items in addition.
- `tag`
  The name of the Git tag.
- `major-tag`
  The name of the Git tag of the major version.
- `minor-tag`
  The name of the Git tag of the minor version.
- `html-url`
  The URL to the page of the GitHub release.
- `upload-url`
  The URL to upload assets for the GitHub release.

## License
The source code is distributed under the MIT license.
See [LICENSE.md](LICENSE.md) for further information.
