from selenium.webdriver.chrome.service import Service
from utils import get_setting
import pytest
from selenium import webdriver
from utils import globalvar



def pytest_configure(config):
    marker_list = ["wap"]
    for markers in marker_list:
        config.addinivalue_line("markers", markers)


@pytest.fixture(scope='module')
def mobile_chrome_driver():
    global driver
    browser_type = globalvar.get_value('browser_type')

    chrome_options = webdriver.ChromeOptions()
    
    # Mobile emulator settings - iPhone 12 Pro dimensions
    mobile_emulation = {
        "deviceMetrics": {
            "width": 390,
            "height": 844,
            "pixelRatio": 3.0
        },
        "userAgent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/14.1.2 Mobile/15E148 Safari/604.1"
        )
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    if browser_type == "headless":
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--window-size=390,844")
        chrome_options.add_argument('--no-sandbox')
    
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
    print("✓ Mobile Chrome Driver closed")


@pytest.fixture(scope='session', autouse=True)
def set_global_data():
    globalvar.create_global_dict()
    settings = get_setting.get_global_setting()
    globalvar.set_value("browser_type", settings['browser_type'])


