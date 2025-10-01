# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-10-01

### Added

-   ⚡ **Auto-update feature** for Flask version
-   Smart debounce mechanism (500ms) to optimize performance
-   Visual indicator for auto-update status
-   Comprehensive documentation in `docs/` directory
-   Unit tests with test_model.py
-   Professional README.md with badges and screenshots

### Changed

-   Restructured project for better organization
-   Moved documentation files to `docs/` folder
-   Updated Flask UI to match Streamlit's real-time experience
-   Improved .gitignore for cleaner repository

### Fixed

-   Flask button now hidden (auto-update enabled)
-   Optimized update frequency with debounce

## [1.0.0] - 2025-10-01

### Added

-   Initial release
-   Streamlit implementation with real-time updates
-   Flask implementation with manual button
-   Linear regression model following CRISP-DM methodology
-   Interactive Plotly visualizations
-   Outlier detection and highlighting
-   Model coefficients and R² score display
-   Top 5 outliers table
-   Comprehensive documentation

### Features

-   Generate synthetic data: y = ax + b + noise
-   Adjustable parameters (n, a, noise variance, seed)
-   Blue scatter points for normal data
-   Red diamond markers for outliers
-   Green regression line
-   Responsive design for both desktop and mobile

---

## Version History

-   **v2.0.0** (2025-10-01) - Auto-update feature, improved UX
-   **v1.0.0** (2025-10-01) - Initial release
