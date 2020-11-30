from selenium.webdriver.common.by import By
from .base import Page, Wait


class PopularPage(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        # self.timeout = self.driver

        self.MAIN_MOVE = (By.ID, '')

    # def set_timeout(self, timeout):
    #     self.timeout = Wait(timeout).set_timeout()




