from pages.base_page import Page
from pages.main_page import MainPage
from pages.category_page import CategoryPage
from pages.search_page import SearchPage
from pages.profile_page import ProfilePage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.category_page = CategoryPage(driver)
        self.search_page = SearchPage(driver)
        self.profile_page = ProfilePage(driver)
