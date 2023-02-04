# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.1] - 2023-02-04
### Added
- Added buttons to add and remove pets, users to and from groups
### Changed
- Fixed My Pets and My Groups to accurately reflect only the pets and groups that the user owns/belongs to
- Fixed Add Pets to Group to only include user's pets

## [0.6.0] - 2023-01-19
### Added
- Added register, login pages
- Added more views for register, login, dashboard, edit page, etc.
- Added VueJS store persistence
### Changed
- Filtered out hashed user password from relation data
- Various changes to views

## [0.5.1] - 2023-01-17
### Added
- Added more endpoints for updating relations
- Added rudimentary check to make sure user is the one updating field
- Added checks for some relations to make sure we're not removing the last item
- Added more exclusions on response models
### Changed
- Use Tortoise ORM instead of SQLAlchemy
- Refactor everything to use Tortoise ORM
- Only `init_models` once
- Various style changes

## [0.4.1] - 2023-01-10
### Added
- Added register, login endpoints
- Added OAuth support
- Added more fields to User model
### Changed
- Updated User model references everywhere
- Fixed user validation when no user is found

## [0.3.2] - 2023-01-10
### Added
- Added delete methods
- Added Groups, Users view/create pages
- Autopopulate age based on DOB
### Changed
- Return IDs of related models
- Update VueJS homepage with example code

## [0.2.1] - 2023-01-09
### Added
- More endpoints for creating and updating models
- VueJS frontend stubs
### Changed
- Modified relationships between owners, pets, groups to be many-to-many

## [0.1.0] - 2023-01-09
### Added
- Project setup
- `GET`/`POST` actions for all models
- `PATCH` actions for adding users to groups
