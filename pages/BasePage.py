from utils.selenium_layer import Selenium


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = Selenium(self.driver)

    def find_element(self, element, wait_type='visibility'):
        return self.selenium.find_element(element, wait_type)

    def click_element(self, element, wait_type='visibility'):
        self.selenium.click_element(element, wait_type)

    def input_element_text(self, element, text, wait_type='visibility'):
        self.selenium.input_element_text(element, text, wait_type)

    def waiting_element_not_exist(self, element, wait_type='invisibility'):
        return self.selenium.waiting_element_not_exist(element, wait_type)

    def is_element_display(self, element, wait_type='visibility'):
        return self.selenium.is_element_display(element, wait_type)

    def execute_js(self, js):
        self.selenium.execute_js(js)

    def open_link(self, url):
        self.selenium.open_link(url)

    def scroll_down(self, times):
        for _ in range(times):
            self.selenium.execute_js("window.scrollBy(0, window.innerHeight);")