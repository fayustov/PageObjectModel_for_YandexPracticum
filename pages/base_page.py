from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def find_element_located_click(self, locator):
        self.find_element_located(locator).click()

    def find_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Element not found in {locator}')

    def execute_script(self, locator):
        return self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def switch_window(self):
        window_after = self.driver.window_handles[1]
        return self.driver.switch_to.window(window_after)
        