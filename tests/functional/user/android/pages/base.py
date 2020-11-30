import operator


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)


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

    @classmethod
    def condition_length(cls, length, sign, length_elem):
        if not isinstance(length, int):
            length = int(length)
        if not isinstance(length_elem, int):
            length_elem = int(length_elem)
        operators = {
            '<': operator.lt,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne,
            '>=': operator.ge,
            '>': operator.gt
        }
        if sign not in operators:
            raise KeyError('[ERROR] operator sign is invalid')
        operation = operators[sign]
        return operation(length, length_elem)


class Wait:
    def __init__(self):
        self.last_custom_wait = None
        self.custom_wait = 0

    def set_wait(self, context_driver, new_wait):
        self.last_custom_wait = self.custom_wait
        self.custom_wait = new_wait
        try:
            context_driver.implicitly_wait(int(self.custom_wait))
        except TimeoutError as e:
            print(f'[ERROR] timeout was not installed - {e}')

    def get_last_wait(self):
        if self.last_custom_wait is None:
            raise TimeoutError('[ERROR] timeout was not installed')
        return self.last_custom_wait
