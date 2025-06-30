# e-Comm QA Suite

This project automates the testing of the e-commerce web application [saucedemo.com](https://saucedemo.com) using Python, Behave (BDD), Playwright (UI & API), and Allure for reporting. It supports advanced Playwright features, external test data, and both UI and API validations.

## Features
- UI automation: product search, add to cart, cart validation, dialogs, image comparison
- API automation: location lookup using latitude/longitude from external data
- Test data: JSON/CSV
- Allure reporting
- Advanced Playwright: network interception, event listeners, assertions, logging

## Project Structure
- `features/` - BDD feature files and step definitions
- `tests/` - Baseline images and test data
- `pages/` - Page Object Model for UI
- `utils/` - Utilities for logging, data, image comparison, API helpers
- `allure-results/` - Allure report output

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Install Playwright browsers: `playwright install`
3. Run tests: `behave`
4. Generate Allure report: `allure serve allure-results`

---

See each folder for more details and usage examples.
