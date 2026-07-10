# Changelog

All notable changes to the Apple Liquid Glass theme will be documented in this file.

## [1.0.0] - Initial Release

### Added
- Complete rewrite of the Abyss base into 15 modular stylesheets (`liquid-glass.css`, `variables.css`, `materials.css`, `animations.css`, `layout.css`, `scrollbars.css`, `utilities.css`, `buttons.css`, `inputs.css`, `cards.css`, `sidebar.css`, `header.css`, `player.css`, `dialogs.css`, `login.css`).
- Introduced 3-tier Glass Material System (Thin, Regular, Thick).
- Added `prefers-color-scheme` support for native Dark/Light mode tracking.
- Added `prefers-reduced-motion` support for accessibility.
- Added OLED Dark Mode fallback variables.
- Implemented edge-lighting linear gradients and multiple-layered Apple shadows.
- Apple TV Style floating media cards with 1.03 scale physics.
- Detached, floating sidebar and player UI.

### Changed
- Refactored `theme.css` out as a fallback underlying base, relying entirely on the new Liquid Glass design tokens for primary presentation.
- Migrated all motion curves to `cubic-bezier(.2, .8, .2, 1)`.
- Switched all UI borders to rely on translucent edge-lighting and shadow depth.
- Replaced monolithic blur definitions with modular variables (`--glass-blur-thin`, `--glass-blur-regular`, `--glass-blur-thick`).

### Fixed
- Improved text readability on media cards over bright backdrops by introducing a layered gradient overlay.
- Prevented over-blurring by limiting `backdrop-filter` only to floating elements.
- Ensured cross-browser compatibility by adding solid background `@supports` fallbacks for older browsers without `backdrop-filter`.
