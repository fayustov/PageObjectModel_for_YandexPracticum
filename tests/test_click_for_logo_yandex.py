import allure
from pages.main_page import LogoTesting
from locators.main_page_locators import Locators
from pages.base_page import BasePage


class TestLogoYandex:
    @allure.title('Переход в dzen, через логотип Яндекс')
    def test_jump_after_click_logo_yandex(self, driver):
        logo_button = LogoTesting(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        logo_button.jump_after_click_logo_yandex()
        base_page.switch_window()
        base_page.find_element_located(Locators.dzen_page_id)
        url = driver.current_url
        assert "https://dzen.ru/" in url
        