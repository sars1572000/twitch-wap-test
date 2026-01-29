# Twitch WAP Automation Testing Framework

A Python-based mobile web automation testing framework built with pytest and Selenium, specifically designed for testing Twitch web application mobile functionality.

## 🎯 Test Objectives

This project implements the WAP testing requirements from AQA Home Test:

1. Navigate to Twitch mobile website
2. Click on the search icon
3. Search for "StarCraft II"
4. Scroll down 2 times
5. Select one streamer
6. Wait for the streamer page to fully load and take a screenshot

## 🚀 Test Execution Demo

![Test Execution Demo](demo.gif)

## 📋 Prerequisites

- Python 3.8+
- Chrome Browser
- ChromeDriver (automatically managed)

## 🛠️ Installation & Setup

### 1. Clone Repository
```bash
git clone <repository-url>
cd twitch-wap-test
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Virtual Environment (Recommended)
```bash
python -m venv wap_auto
source wap_auto/bin/activate  # On Windows: wap_auto\Scripts\activate
pip install -r requirements.txt
```

## 🏃‍♂️ Running Tests

### Run All WAP Tests
```bash
pytest -m wap -v
```

### Run Specific Test File
```bash
pytest tests/test_twitch_wap.py -v
```

## 📊 Test Reports

After test execution, the following outputs are generated:
- **HTML Report**: `reports/report.html`
- **Test Logs**: `logs/test.log`
- **Screenshots**: `tests/screenshots/`

## 🏗️ Repository Structure

```
twitch-wap-test/
├── configs/                    # Configuration files
│   └── global.yaml            # Browser and environment settings
├── pages/                     # Page Object Model (POM) classes
│   ├── BasePage.py           # Base page class with common web interactions
│   ├── Pages.py              # Page factory for creating page instances
│   ├── home_page.py          # Twitch home page object
│   └── streamer_page.py      # Streamer page object with popup handling
├── tests/                     # Test files and test-related resources
│   ├── conftest.py           # pytest configuration and fixtures
│   ├── test_twitch_wap.py    # Main WAP test cases
│   └── screenshots/          # Test screenshots storage
├── utils/                     # Utility modules
│   ├── selenium_layer.py     # Custom Selenium wrapper layer
│   ├── get_setting.py        # Configuration management from YAML
│   └── globalvar.py          # Global variable management for test data sharing
├── logs/                      # Test execution logs
├── reports/                   # HTML test reports
├── pytest.ini               # pytest configuration
├── requirements.txt          # Python dependencies
├── CLAUDE.md                 # Claude Code guidance file
└── README.md                 # Project documentation
```