****************************
Project Overview-
****************************
This project demonstrates automated QA testing for web applications using Python, Playwright, and Pytest.

UI Tests: Automated end-to-end tests for positive, negative, and edge cases, using Page Object Model.
API Tests: Backend validation tests for HTTP status codes, redirects, headers, response times, and negative scenarios, using a reusable API Page Object.
Clean Test Architecture: Tests are separated into UI and API folders for maintainability.


****************************
File Structure-
****************************
playwright-pytest-qa-automation/
├── pages/
│   ├── __init__.py
│   ├── api_page.py
│   ├── check_box_page.py
│   ├── dynamic_control_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── secure_area_page.py
├── tests/
│   ├── __init__.py
│   ├── conf_test.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── test_api.py
│   └── ui/
│       ├── __init__.py
│       ├── test_broken_links.py
│       ├── test_checkbox.py
│       ├── test_dynamic_control.py
│       └── test_login.py
├── .gitignore
├── README.md
├── requirements.txt
└── pytest.ini


****************************
Technologies & Tools - 
****************************
Python – primary programming language
Playwright – for UI automation
Pytest – test framework and assertions
Requests – for API testing
Page Object Model (POM) – for maintainable test code
pytest fixtures – for reusable setup


****************************
How to Run Tests-
****************************
Install dependencies:
pip install -r requirements.txt

Run all UI tests
pytest tests/ui

Run all API tests
pytest tests/api

Run a single test
pytest tests/ui/test_login.py


****************************
Test Coverage
****************************
UI Tests
Login Scenarios: Valid login, invalid login, empty fields, login/logout flow
Checkbox / Dynamic Controls: Check/uncheck boxes, add/remove elements
Broken Links: Verify all links on a page return valid status codes

API Tests
Positive: Login page availability, response headers, response times
Negative: Non-existent endpoints, invalid credentials, redirect validation
