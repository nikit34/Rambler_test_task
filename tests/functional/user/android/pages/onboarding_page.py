from selenium.webdriver.common.by import By
from .base import Page


class OnboardingPage(Page):
    def __init__(self, driver):
        self.driver = driver

        self.TITLE_TEXT = (By.ID, 'ru.rambler.kassa:id/text_title')
        self.MAIN_TEXT = (By.ID, 'ru.rambler.kassa:id/text_message')

        self.CLOSE_BTN = (By.ID, 'ru.rambler.kassa:id/button_close')
        self.NEXT_BTN = (By.ID, 'ru.rambler.kassa:id/button_next')

    def verify_title_text(self, text):
        text_elem = self.find_element(*self.TITLE_TEXT).text
        print(self.completely_matches(text, text_elem))
        assert self.completely_matches(text, text_elem), f'[FAILED] TITLE TEXT don`t found select - {self.TITLE_TEXT} text - {text}'

    def verify_main_text(self, text):
        text_elem = self.find_element(*self.MAIN_TEXT).text
        print(self.partially_matches(text, text_elem))
        assert self.partially_matches(text, text_elem), f'[FAILED] TITLE TEXT don`t found select - {self.TITLE_TEXT} text - {text}'
