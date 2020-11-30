from appium.webdriver.common.touch_action import TouchAction
from .base import Page

class Action(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()

        self.height = None
        self.width = None

    @classmethod
    def click(cls, driver, *locator):
        this = cls(driver)
        e = this.find_element(*locator)
        e.click()

    def input(self, text, *locator):
        e = self.find_element(*locator)
        e.clear()
        e.send_key(text)

    def get_size_screen(self):
        size = self.driver.get_window_size()
        self.height = size['height']
        self.width = size['width']
        return size

    def calc_coords_to_percent(self, x1, y1, x2, y2):
        px1 = x1 / self.width * 100
        py1 = y1 / self.height * 100
        px2 = x2 / self.width * 100
        py2 = y2 / self.height * 100
        return px1, py1, px2, py2

    def calc_percent_to_coords(self, px1, py1, px2, py2):
        x1 = px1 / 100 * self.width
        y1 = py1 / 100 * self.height
        x2 = px2 / 100 * self.width
        y2 = py2 / 100 * self.height
        return x1, y1, x2, y2

    # def dragdrop(self, px1, px2, py1, py2):
    #     pass
    #
    # def move_obj_from_elem_to_elem(self, obj, elem1, elem2):
    #     pass

    # def move_obj_at_delta_coords(self, obj, dx, dy):
    #     actions = TouchAction(self.driver)
    #     actions.tap_and_hold(obj)
    #     actions.move_to(obj, dx, dy)
    #     actions.perform()

         # actions = ActionChains(driver)
         # actions.move_to(element, 10, 10)
         # actions.perform()



