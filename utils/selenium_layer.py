# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


WaitType = {'presence': EC.presence_of_element_located,
            'visibility': EC.visibility_of_element_located,
            'invisibility': EC.invisibility_of_element_located
            }


class Selenium(object):

    def __init__(self, driver):
        sec = 120
        self.driver = driver
        self.driver.set_implicitly = sec
        self.driver.set_page_load_timeout(sec)

    def open_link(self, url):
        self.driver.get(url)

    def waiting_element_not_exist(self, selector, wait_type):
        try:
            _wait_element_localed(self.driver, selector, wait_type)
            return True
        except Exception:
            return False

    def input_element_text(self, selector, text, wait_type):
        _wait_element_localed(self.driver, selector, wait_type)
        element = self.find_element(selector, wait_type)
        if element == '':
            raise Exception
        element.send_keys(text)

    def find_element(self, selector, wait_type, time_out=40, interval=0.2):
        try:
            _wait_element_localed(self.driver, selector, wait_type, time_out, interval)
            element = self.driver.find_element(*_selector_to_by(selector))
        except Exception:
            element = ''

        return element

    def click_element(self, selector, wait_type):
        wait_time = 0
        time.sleep(0.4)
        while wait_time < 10:
            _wait_element_localed(self.driver, selector, wait_type)
            element = self.find_element(selector, wait_type)
            if element == '':
                raise Exception

            if element.is_displayed():
                element.click()
                return True
            else:
                wait_time += 1
                time.sleep(0.5)

        return False

    def is_element_display(self, selector, wait_type):
        element = self.find_element(selector, wait_type, time_out=1.5)
        if element == '':
            return False
        if element.is_displayed():
            return True

    def execute_js(self, js_script):
        self.driver.execute_script(js_script)


def _selector_to_by(selector):
    """
    Change the selector to ('by', 'value') mode

    :param selector: "id>>>username"
    :return: ('by', 'value')
    """
    if ">>>" not in selector:
        raise NameError("selector syntax errors, lack of '>>>'")

    by = selector.split('>>>')[0]
    value = selector.split('>>>')[1]

    if by == "id":
        by = By.ID
    elif by == "name":
        by = By.NAME
    elif by == "link_text":
        by = By.LINK_TEXT
    elif by == "css" or by == "css_selector":
        by = By.CSS_SELECTOR
    elif by == "xpath":
        by = By.XPATH
    elif by == "tag" or by == "tag_name":
        by = By.TAG_NAME
    elif by == "class" or by == "class_name":
        by = By.CLASS_NAME
    elif by == "text" or by == "partial_link_text":
        by = By.PARTIAL_LINK_TEXT
    else:
        raise NameError(
            "please enter correct element attribute, 'id','name','xpath','css','tag','class','text','link_text'.")

    return by, value


def _wait_element_localed(driver, selector, wait_type, time_out=40, interval=0.2):
    """
    Wait for an element localed on DOM.
    """
    type = WaitType[wait_type]
    WebDriverWait(driver, time_out, interval).until(type(_selector_to_by(selector)))


