from selenium.webdriver.common.by import By
from .base import Page, Search, Wait
from .action import Action
from .benchmarks.custom import timing


class PopularPage(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        super(Wait, self).__init__()

        self.act = Action(driver)

        self.locators = {
            "MOVE_TITLE": (By.ID, 'ru.rambler.kassa:id/movie_title'),
            "MOVE_TIME": (By.ID, 'ru.rambler.kassa:id/button_time'),
            "PLACE": (By.ID, 'ru.rambler.kassa:id/place'),
            "PLACE_DIST": (By.ID, 'ru.rambler.kassa:id/place_dist'),
            "TV_SESSION_DATA": (By.ID, 'ru.rambler.kassa:id/tvSessionDate'),
            "IMAGE_POSTER": (By.ID, 'ru.rambler.kassa:id/image_poster'),
            "TRAILER_BTN": (By.ID, 'ru.rambler.kassa:id/trailer_button'),
            "FOOTER_TEXT": (By.ID, 'ru.rambler.kassa:id/bb_bottom_bar_title')
        }

    def set_custom_wait(self, wait):
        self.obj_wait.set_wait(self.driver, wait)

    def get_last_custom_wait(self):
        return self.obj_wait.get_last_wait()

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
        assert Search.condition_length(length, sign, length_elem), f'[FAILED] {label} don`t have required length select: {self.locators[label]}'

    @timing
    def exist_elem(self, label):
        elem = self.find_element(*self.locators[label])
        assert elem, f'[FAILED] {label} don`t found select: {self.locators[label]}'

