from pages.base_page import Page
from pages.onboarding_page import OnboardingPage
from pages.popular_page import PopularPage
from pages.category_page import CategoryPage
from pages.search_page import SearchPage
from pages.profile_page import ProfilePage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.onboarding_page = OnboardingPage(driver)
        self.main_page = PopularPage(driver)
        self.category_page = CategoryPage(driver)
        self.search_page = SearchPage(driver)
        self.profile_page = ProfilePage(driver)
