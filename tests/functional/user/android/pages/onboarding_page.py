from selenium.webdriver.common.by import By
from .base import Page


class OnboardingPage(Page):
    def __init__(self, driver):
        self.driver = driver

        self.TITLE_TEXT = (By.ID, 'ru.rambler.kassa:id/text_title')
        self.MAIN_TEXT = (By.ID, 'ru.rambler.kassa:id/text_message')

        self.NEXT_BTN = (By.ID, 'ru.rambler.kassa:id/button_next')
        self.CLOSE_BTN = (By.ID, 'ru.rambler.kassa:id/button_close')

    def verify_title_text(self, text):
        text_elem = self.find_element(*self.TITLE_TEXT).text
        assert self.matching_text(text, text_elem), f'[FAILED] TITLE_TEXT don`t found select: {self.TITLE_TEXT}'

    def verify_main_text(self, text):
        text_elem = self.find_element(*self.MAIN_TEXT).text
        assert self.matching_text(text, text_elem), f'[FAILED] MAIN_TEXT don`t found select: {self.MAIN_TEXT}'

    def verify_next_btn(self, text):
        btn_elem = self.find_element(*self.NEXT_BTN).text
        assert self.matching_text(text, btn_elem), f'[FAILED] NEXT_BTN don`t found select: {self.NEXT_BTN}'

    def verify_close_btn(self, text):
        btn_elem = self.find_element(*self.CLOSE_BTN).text
        assert self.matching_text(text, btn_elem), f'[FAILED] CLOSE_BTN don`t found select: {self.CLOSE_BTN}'

    def tap_next_btn(self):
        self.click(*self.NEXT_BTN)

    def tap_close_btn(self):
        self.click(*self.CLOSE_BTN)