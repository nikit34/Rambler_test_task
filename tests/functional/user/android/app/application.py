from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.profile_page = ProfilePage(driver)