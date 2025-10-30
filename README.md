# Lumynous GitHub Release Action

Creates GitHub releases automatically.

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
        uses: lumynou5/github-release-action@v2
        with:
          token: ${{github.token}}
          assets: |
            dist/linux-x86_64
            dist/windows.exe::windows version
            dist/darwin:macos
```

In this example workflow, it'll create a release whenever push to `main` branch.
The version and the release note will be captured from the changelog following
[Keep a Changelog](https://keepachangelog.com/) and
[Semantic Versioning](https://semver.org/).  And a Git tag will be created for
the major revision, see [Inputs](#Inputs) for more information.

This is useful to automatically publish releases on pushing to the stable branch
when using Git flow, etc.

Note that "moving tags" are considered an anti-pattern in Git and should only be
used for GitHub actions.  This is due to GitHub actions' lack of semantic
version functionality, which makes developers have to use tags like `v1` to let
GitHub checkout latest version with major version `1` rather than matching a
version pattern like `^1.0.0`.  To disable creating and editing moving tags, use

```yml
with:
  major-tag-template: ''
  minor-tag-template: ''
```

## Inputs

- `token` (required)
  The GitHub token.
- `changelog`
  The path to the changelog. Default: `CHANGELOG.md`.
- `tag-template`
  The template of the Git tag. Default: `v{version}`.
- `major-tag-template`
  The template of the Git tag of the major version.  Doesn't perform if the
  major version is 0.
  Default: `v{major}`.  Empty for no major tag.
- `minor-tag-template`
  The template of the Git tag of the minor version.
  Default: `v{maojr}.{minor}`.  Empty for no minor tag.
- `name-template`
  The template of the GitHub release.
  Default: `v{version}`.
- `is-draft`
  If the GitHub release is a draft.
  Default: `false`.
- `assets`
  A newline-separated list of files to upload.  Besides file paths, it also
  accpets optional name and label (short description for the asset) separated by
  colons.  For example, `path/to/file:name:label` renames the asset to `name`
  instead of using the basename of the file.  The name can be omitted by leaving
  an empty string there (so two colons in a row) if you want to set label only.
  Default: empty.

The following list shows the parameters that can be used in templates.  To use
parameters, add a parameter name wrapping with braces to your template, and it
will be replaced with data from your changelog; i.e. `{parameter-name}` will be
replaced with the corresponding value.

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

The outputs include all the parameters of templates and the following items in
addition.

- `change`
  The changelog of the latest version.
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
