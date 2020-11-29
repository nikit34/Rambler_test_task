from selenium.webdriver.common.by import By
from base import Page


class OrderProductsPage(Page):
    def __init__(self, driver):
        self.driver = driver