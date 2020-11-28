from selenium.webdriver.common.by import By
from .base_page import Page


class MainPage(Page):
    ONBOARDING_NEXT_BTN = (By.ID, 'ru.rambler.kassa:id/button_next')
    ONBOARDING_CANCEL_BTN = (By.ID, 'ru.rambler.kassa:id/button_close')

    def tap_popular(self):
        self.click(self.POPULAR_FOOTER_BTN)

    def tap_category(self):
        self.click(self.CATEGORY_FOOTER_BTN)

    def tap_search(self):
        self.click(self.SEARCH_FOOTER_BTN)

    def tap_profile(self):
        self.click(self.PROFILE_FOOTER_BTN)

