from selenium.webdriver.common.by import By
from base import Page


class Footer(Page):
    def __init__(self, driver):
        self.driver = driver

        self.POPULAR_BTN = (By.ID, '')
        self.CATEGORY_BTN = (By.ID, '')
        self.SEARCH_BTN = (By.ID, '')
        self.TICKET_BTN = (By.ID, '')
        self.PROFILE_BTN = (By.ID, '')

    def tap_popular(self):
        self.click(self.POPULAR_BTN)

    def tap_category(self):
        self.click(self.CATEGORY_BTN)

    def tap_search(self):
        self.click(self.SEARCH_BTN)

    def tap_ticket(self):
        self.click(self.TICKET_BTN)

    def tap_profile(self):
        self.click(self.PROFILE_BTN)