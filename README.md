## 📌 Project Overview

The goal of this project is to validate the core functionalities of the **SauceDemo** website through automated UI tests, including:

- User authentication with multiple account types
- Page navigation
- Adding products to the cart
- Checkout process
- Error handling and edge cases

## 🗂️ Project Structure

```
saucedemo-project/
│
├── base_object/          # Core WebDriver logic and base page objects
├── files/                # Test data and resources
├── pages/                # Page Object classes for each web page
├── support/              # Helpers, utilities, and config files
├── tests/                # Test cases written with Pytest
├── conftest.py           # Pytest fixtures
├── config.py             # Configuration settings
└── requirements.txt      # Dependencies
```

## 🚀 Getting Started

### 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/szubarau/saucedemo-project.git
cd saucedemo-project
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### ▶️ Running Tests

To run all tests:
```bash
pytest
```

Useful options:
```bash
pytest -v         # Verbose output
pytest -k login   # Run tests matching "login"
```

## ⚙️ Configuration

Edit the `config.py` file to change:

- Base URL (`BASE_URL`)
- Test user credentials:
  - `standard_user`
  - `locked_out_user`
  - `problem_user`
  - `performance_glitch_user`
- Common password: `secret_sauce`

## 🧱 Technologies Used

- 🐍 Python 3
- 🧪 Pytest
- 🌐 Selenium WebDriver
- 🧼 Page Object Model (POM)