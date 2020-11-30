from selenium.webdriver.common.by import By
from .base import Page


class SearchPage(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__(driver)

    def input_search(self, search_phrase):
        self.input(search_phrase, '<*locator>')

    def verify_search_result(self, search_phrase):
        result_text = self.find_element('<*locator>').text
        assert search_phrase in result_text, f'Expected {search_phrase} be in {result_text}'