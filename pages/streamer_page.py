from pages.BasePage import BasePage
import enum

class Elements(enum.Enum):
    main_content_wrapper = "id>>>page-main-content-wrapper"
    tablist = "xpath>>>//*/ul[@role='tablist']"
    loading_spinner = "xpath>>>//*/div[contains(@class, 'ScLoadingSpinner')]"

class StreamerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.screenshot_counter = 0

    def wait_for_page_load(self):
        self.find_element(Elements['loading_spinner'].value)
        self.waiting_element_not_exist(Elements['loading_spinner'].value)
        self.is_element_display(Elements['main_content_wrapper'].value)
        self.is_element_display(Elements['tablist'].value)

    def take_screenshot(self, filename=None):
        if not filename:
            self.screenshot_counter += 1
            filename = f"streamer_page_screenshot_{self.screenshot_counter}.png"

        screenshot_path = f"screenshots/{filename}"

        # Create screenshots directory if it doesn't exist
        import os
        os.makedirs("screenshots", exist_ok=True)

        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
            return None