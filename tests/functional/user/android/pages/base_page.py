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


class Search(Page):
    def __init__(self, capacity=100, size_windows=50, *args, **kwargs):
        self.capacity = capacity
        self.size_windows = size_windows
        super(Page, self).__init__(*args, **kwargs)

    @staticmethod
    def matching_text(token, pattern):
        if '*' in token:
            return Search.partially_matches(token, pattern)
        return Search.completely_matches(token, pattern)

    @classmethod
    def partially_matches(cls, token, pattern):
        separate_token = token.split('*')
        current_pattern = pattern
        found_result = []
        for part_token in separate_token:
            found_index = current_pattern.find(part_token)
            if found_index == -1:
                continue
            current_pattern = current_pattern[found_index:]
            found_result.append(part_token)
        return found_result

    @classmethod
    def completely_matches(cls, token, pattern):
        if pattern.find(token) == -1:
            return False
        return True