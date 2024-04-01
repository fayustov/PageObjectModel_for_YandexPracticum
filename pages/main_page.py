from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    @allure.step('Клик по логотипу Самокат')
    def jump_after_click_logo_scooter(self):
        self.find_element_located_click(MainPageLocators.logo_scooter)

    @allure.step('Клик по логотипу Самокат')
    def jump_after_click_logo_yandex(self):
        self.find_element_located_click(MainPageLocators.logo_yandex)

    def check_cookie(self):
        cookie = self.find_element_located(MainPageLocators.cookie_message)
        if cookie:
            cookie.click()
        else:
            pass

    @allure.step('Возвращаем значение ответа от требуемого вопроса')
    def main_page_questions(self, button, answer):
        self.check_cookie()
        search_field = self.find_element_located(button)
        self.execute_script(search_field)
        self.find_element_to_be_clickable(button)
        search_field.click()
        return self.find_element_located(answer).text
