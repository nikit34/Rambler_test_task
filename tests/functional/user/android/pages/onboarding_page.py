from selenium.webdriver.common.by import By
from .base_page import Page


class OnboardingPage(Page):
    def __init__(self):
        self.TITLE_TEXT = (By.ID, 'ru.rambler.kassa:id/text_title')
        self.MAIN_TEXT = (By.ID, 'ru.rambler.kassa:id/text_message')

        self.CLOSE_BTN = (By.ID, 'ru.rambler.kassa:id/button_close')
        self.NEXT_BTN = (By.ID, 'ru.rambler.kassa:id/button_next')