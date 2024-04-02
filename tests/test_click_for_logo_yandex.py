import allure
from pages.main_page import MainPage


class TestLogoYandex:
    @allure.title('Переход в dzen, через логотип Яндекс')
    def test_jump_after_click_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        main_page.jump_after_click_logo_yandex()
        main_page.switch_window()
        main_page.find_dzen_logo()
        url = main_page.current_url()
        assert "https://dzen.ru/" in url
        