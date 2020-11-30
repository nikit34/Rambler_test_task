from selenium.webdriver.common.by import By
from .base import Page


class ProfilePage(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()