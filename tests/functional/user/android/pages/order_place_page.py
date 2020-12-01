from selenium.webdriver.common.by import By
from .base import Page, Search, Wait
from .benchmarks.custom import timing


class OrderPlacePage(Page, Wait):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.locators = {
            "TICKET_COUNT_ONE": (By.ID, 'ru.rambler.kassa:id/tickets_count_and_price_text_view'),
            "TICKET_COUNT_PLUS": (By.ID, 'ru.rambler.kassa:id/fee_text_view'),
            "NEXT_BTN": (By.ID, 'ru.rambler.kassa:id/next_button'),
            "LEVEL_MAP_VIEW": (By.ID, 'ru.rambler.kassa:id/level_map_view'),
            "SESSION_SUB_TITLE": (By.ID, 'ru.rambler.kassa:id/session_sub_title_text_view'),
            "SESSION_TITLE": (By.ID, 'ru.rambler.kassa:id/session_title_text_view'),
            "TOOLBAR": (By.ID, 'ru.rambler.kassa:id/toolbar'),
        }

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def get_last_custom_wait(self):
        return self.get_last_wait()

    @timing
    def verify_text(self, text, label):
        text_elem = self.find_element(*self.locators[label]).text
        assert Search.matching_text(text, text_elem), f'[FAILED] {label} don`t found select: {self.locators[label]}'

    @timing
    def tap_btn(self, label):
        self.click(*self.locators[label])

    @timing
    def verify_length_text(self, length, sign, label):
        text_elem = self.find_element(*self.locators[label])
        length_elem = len(text_elem.text)
        assert Search.condition_length(length, sign,
                                       length_elem), f'[FAILED] {label} don`t have required length select: {self.locators[label]}'

    @timing
    def exist_elem(self, label):
        elem = self.find_element(*self.locators[label])
        assert elem, f'[FAILED] {label} don`t found select: {self.locators[label]}'

