from pages.BasePage import BasePage
import enum

class Elements(enum.Enum):
    search_icon = "xpath>>>//*/a[@href='/directory']"
    search_input ="xpath>>>//*/input[@data-a-target='tw-input']"
    search_first_result = "xpath>>>//*/main[@id='page-main-content-wrapper']/div[1]/ul[1]/li[1]"
    search_suggestions = "xpath>>>//*/main[@id='page-main-content-wrapper']/div[1]/ul[1]"
    search_category_results = "xpath>>>//*/div[@role='list']"
    search_channel_results = "xpath>>>//*/div[@role='list']/div[6]/div[1]/article[1]/div[1]/div[1]/div[2]"
    loading_spinner = "xpath>>>//*/div[contains(@class, 'ScLoadingSpinnerCircle')]"


class HomePage(BasePage):

    def click_search_icon(self):
        self.click_element(Elements['search_icon'].value)

    def search_for(self, search_term):
        self.input_element_text(Elements['search_input'].value, search_term)
        self.find_element(Elements['search_suggestions'].value)

    def click_first_search_result(self):
        self.click_element(Elements['search_first_result'].value)
        self.waiting_element_not_exist(Elements['loading_spinner'].value)

    def wait_for_search_results(self):
        self.is_element_display(Elements['search_category_results'].value)
        self.is_element_display(Elements['loading_spinner'].value)

    def select_first_streamer(self):
        self.click_element(Elements['search_channel_results'].value)
