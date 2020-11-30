from selenium.webdriver.common.by import By
from .base import Page, Wait


class PopularPage(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()

        self.obj_wait = Wait(self.driver)

        self.MAIN_MOVE = (By.ID, '')

    def set_timeout(self, timeout):
        self.obj_wait.set_timeout(timeout)




