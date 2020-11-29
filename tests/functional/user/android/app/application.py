from pages.base_page import Page

from pages.onboarding_page import OnboardingPage

from pages.popular_page import PopularPage
from pages.category_page import CategoryPage
from pages.search_page import SearchPage
from pages.ticket_page import TicketPage
from pages.profile_page import ProfilePage

from pages.footer import Footer

from pages.popular_detail_page import PopularDetailPage
from pages.profile_support_page import ProfileSupportPage

from pages.order_place_page import OrderPlacePage
from pages.order_category_page import OrderCategoryPage
from pages.order_products_page import OrderProductsPage
from pages.order_page import OrderPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)

        self.onboarding_page = OnboardingPage(driver)

        self.popular_page = PopularPage(driver)
        self.category_page = CategoryPage(driver)
        self.search_page = SearchPage(driver)
        self.ticket_page = TicketPage(driver)
        self.profile_page = ProfilePage(driver)

        self.footer = Footer(driver)

        self.popular_detail_page = PopularDetailPage(driver)
        self.profile_support_page = ProfileSupportPage(driver)

        self.order_place_page = OrderPlacePage(driver)
        self.order_category_page = OrderCategoryPage(driver)
        self.order_products_page = OrderProductsPage(driver)
        self.order_page = OrderPage(driver)
