from selenium.webdriver.common.by import By
from base import Page


class PopularDetailPage(Page):
    def __init__(self, driver):
        self.driver = driver