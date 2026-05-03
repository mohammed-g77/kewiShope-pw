# Kewi Store - Playwright Test Automation Framework

This is a production-level test automation framework built using **Python**, **Playwright**, and **Pytest** for the Kewi E-commerce website (`https://kewi.ps`).

## 📁 Project Structure

The project follows the **Page Object Model (POM)** design pattern to ensure clean, maintainable, and scalable code.

```
kewiShop/
├── .github/
│   └── workflows/
│       └── playwright.yml  # CI/CD pipeline configuration
├── data/
│   └── users.json          # Test data (fixtures) for data-driven testing
├── pages/
│   ├── base_page.py        # Base class containing common Playwright wrapper methods
│   ├── cart_page.py        # Locators and methods for the Shopping Cart
│   ├── home_page.py        # Locators and methods for the Homepage
│   ├── login_page.py       # Locators and methods for the Login page
│   └── product_page.py     # Locators and methods for the Product Details page
├── tests/
│   ├── test_cart.py        # Cart functionality tests
│   ├── test_homepage.py    # Homepage UI and search tests
│   ├── test_login.py       # Data-driven login tests
│   └── test_products.py    # Category browsing and product tests
├── conftest.py             # Pytest configuration and shared fixtures
├── pytest.ini              # Pytest settings (markers, base_url, etc.)
└── requirements.txt        # Python dependencies
```

##  Setup Instructions

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd kewiShop
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install
   ```

## 🧪 Running Tests

You can run the tests using Pytest. The default configuration is set to run tests in headed mode using Chromium.

- **Run all tests:**
  ```bash
  pytest
  ```

- **Run tests headlessly (for CI/CD or faster execution):**
  ```bash
  pytest --headed=false
  ```

- **Run a specific test file:**
  ```bash
  pytest tests/test_login.py
  ```

- **Run tests by marker:**
  ```bash
  pytest -m smoke
  ```

## 🛠 Best Practices Used
- **Page Object Model (POM)**: Locators and actions are strictly separated from test scripts.
- **Explicit Waits & Smart Synchronization**: Uses Playwright's auto-waiting mechanism (no `time.sleep()`).
- **Data-Driven Testing**: Uses `@pytest.mark.parametrize` and JSON fixtures to test multiple datasets without code duplication.
- **API Response Interception**: Validates network requests and responses (`expect_response`) to ensure the backend functions correctly with frontend actions.
- **Reusable Fixtures**: `conftest.py` properly manages shared test setup.
