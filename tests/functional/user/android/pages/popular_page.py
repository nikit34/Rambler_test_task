from selenium.webdriver.common.by import By
from .base import Page, Wait, timing, Search


class PopularPage(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()

        self.obj_wait = Wait(self.driver)

        self.locators = {
            "MOVE_TITLE": (By.ID, 'ru.rambler.kassa:id/movie_title'),
            "MOVE_TIME": (By.ID, 'ru.rambler.kassa:id/button_time'),
            "PLACE": (By.ID, 'ru.rambler.kassa:id/place'),
            "PLACE_DIST": (By.ID, 'ru.rambler.kassa:id/place_dist'),
            "TV_SESSION_DATA": (By.ID, 'ru.rambler.kassa:id/tvSessionDate'),
            "IMAGE_POSTER": (By.ID, 'ru.rambler.kassa:id/image_poster'),
            "TRAILER_BTN": (By.ID, 'ru.rambler.kassa:id/trailer_button'),
        }

    def set_timeout(self, timeout):
        self.obj_wait.set_timeout(timeout)

    @timing
    def verify_text(self, text, label):
        text_elem = self.find_element(*self.locators[label]).text
        assert Search.matching_text(text, text_elem), f'[FAILED] {label} don`t found select: {self.locators[label]}'

    @timing
    def tap_btn(self, label):
        self.click(*self.locators[label])




