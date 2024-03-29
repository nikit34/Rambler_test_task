from selenium.webdriver.common.by import By
from .base import Page, Search, Wait
from .benchmarks.custom import timing


class OnboardingPage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.locators = {
            "TITLE_TEXT": (By.ID, 'ru.rambler.kassa:id/text_title'),
            "MAIN_TEXT": (By.ID, 'ru.rambler.kassa:id/text_message'),
            "NEXT_BTN": (By.ID, 'ru.rambler.kassa:id/button_next'),
            "CLOSE_BTN": (By.ID, 'ru.rambler.kassa:id/button_close'),
        }

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def get_last_custom_wait(self):
        return self.get_last_wait()

    @timing
    def verify_text(self, text, label):
        text_elem = self.find_element(*self.locators[label]).text
        assert Search.matching_text(text, text_elem), f'[FAILED] {label} don`t found select: {self.locators[label]}'

    @timing
    def tap_btn(self, label):
        self.click(*self.locators[label])

