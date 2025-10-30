# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]

## [2.0.0] - 2025-10-30
### Added
- Uploading assets is supported now.
### Changed
- If the tag already exists, for example, the main branch is force pushed, now
  the action won't fail and the release will be updated.

## [1.3.0] - 2024-12-24
### Added
- Output the changelog of last version.
### Fixed
- Add output `minor-tag` to action metadata.

## [1.2.0] - 2024-01-16
### Added
- Minor tag.
### Changed
- Major tag of major version 0 is no longer created or moved.
### Fixed
- Templates using multiple parameters work as expected now.

## [1.1.1] - 2023-05-05
### Fixed
- Accidently used tuple for tag name.

## [1.1.0] - 2023-05-05 [YANKED]
### Added
- Outputs the names of the Git tags of the release and the major version; i.e.,
  the filled templates are outputed.
- Input `major-tag-template` can be empty for no major tag now.

## [1.0.1] - 2023-05-01
### Fixed
- Python used to be unable to find the file.

## [1.0.0] - 2023-04-27 [YANKED]
### Added
- First release.

[Unreleased]: https://github.com/lumynou5/github-release-action/compare/v2.0.0...develop
[2.0.0]: https://github.com/lumynou5/github-release-action/releases/tag/v2.0.0
[1.3.0]: https://github.com/lumynou5/github-release-action/releases/tag/v1.3.0
[1.2.0]: https://github.com/lumynou5/github-release-action/releases/tag/v1.2.0
[1.1.1]: https://github.com/lumynou5/github-release-action/releases/tag/v1.1.1
[1.1.0]: https://github.com/lumynou5/github-release-action/releases/tag/v1.1.0
[1.0.1]: https://github.com/lumynou5/github-release-action/releases/tag/v1.0.1
[1.0.0]: https://github.com/lumynou5/github-release-action/releases/tag/v1.0.0
