from selenium.webdriver.common.by import By
from .base import Page, Search
from .benchmarks.custom import timing


class ErrorsPages(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()

        self.locators = {
            "TEXT_ERROR": (By.ID, 'ru.rambler.kassa:id/text_error'),
            "RETRY_BTN": (By.ID, 'ru.rambler.kassa:id/button_retry'),
            "TOOLBAR": (By.ID, 'ru.rambler.kassa:id/toolbar')
        }

    @timing
    def verify_text(self, text, label):
        text_elem = self.find_element(*self.locators[label]).text
        assert Search.matching_text(text, text_elem), f'[FAILED] {label} don`t found select: {self.locators[label]}'

    @timing
    def tap_btn(self, label):
        self.click(*self.locators[label])

    @timing
    def exist_elem(self, label):
        elem = self.find_element(*self.locators[label])
        assert elem, f'[FAILED] {label} don`t found select: {self.locators[label]}'

    @timing
    def not_exist_elem(self, label):
        elem = self.find_element(*self.locators[label])
        assert not bool(elem), f'[FAILED] {label} do found select: {self.locators[label]}'
