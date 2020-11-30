import time


def timing(f):
    def timeit(*args, **kwargs):
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        print(f'\ttiming: {f.__name__}({args[1:]}) --> {te-ts} sec')
        return result
    return timeit


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        e = self.find_element(*locator)
        e.click()

    def input(self, text, *locator):
        e = self.find_element(*locator)
        e.clear()
        e.send_key(text)


class Search:
    def __init__(self, token, pattern):
        self.token = token
        self.pattern = pattern

    @classmethod
    def matching_text(cls, token, pattern):
        this = cls(token, pattern)
        if '*' in this.token:
            return this.partially_matches()
        return this.completely_matches()

    def partially_matches(self):
        separate_token = self.token.split('*')[1::2]
        current_pattern = self.pattern
        found_result = []
        for part_token in separate_token:
            found_index = current_pattern.find(part_token)
            if found_index == -1:
                continue
            current_pattern = current_pattern[found_index:]
            found_result.append(part_token)
        return found_result

    def completely_matches(self):
        if self.pattern.find(self.token) == -1:
            return False
        return True


class Wait(Page):
    def __init__(self, driver):
        self.driver = driver
        super(Page, self).__init__()
        # self.timing =

    # def set_timeout(self):
    #     self.driver.implicitly_wait(self.timing)





