from selenium.webdriver.common.by import By
from base import Page


class Footer(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()

        self.locators = {
            "POPULAR_BTN": (By.ID, 'ru.rambler.kassa:id/text_title'),
            "CATEGORY_BTN": (By.ID, 'ru.rambler.kassa:id/text_message'),
            "SEARCH_BTN": (By.ID, 'ru.rambler.kassa:id/text_title'),
            "MAIN_TEXT": (By.ID, 'ru.rambler.kassa:id/text_message'),
            "TICKET_BTN": (By.ID, 'ru.rambler.kassa:id/button_next'),
            "PROFILE_BTN": (By.ID, 'ru.rambler.kassa:id/button_close'),
        }

    def tap_popular(self):
        self.click(self.locators['POPULAR_BTN'])

    def tap_category(self):
        self.click(self.locators['CATEGORY_BTN'])

    def tap_search(self):
        self.click(self.locators['SEARCH_BTN'])

    def tap_ticket(self):
        self.click(self.locators['TICKET_BTN'])

    def tap_profile(self):
        self.click(self.locators['PROFILE_BTN'])