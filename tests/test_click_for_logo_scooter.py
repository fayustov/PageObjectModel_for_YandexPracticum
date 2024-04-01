import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestLogoScooter:

    @allure.title('Переход на главную, через логотип Самокат (из меню Заказать в шапке)')
    def test_jump_after_click_logo_scooter_in_header(self, driver):
        main_page = MainPage(driver)
        order_button = OrderPage(driver)
        logo_button = MainPage(driver)

        main_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        order_button.order_for_header()
        logo_button.jump_after_click_logo_scooter()
        url = main_page.current_url()
        assert url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Переход на главную, через логотип Самокат (из меню Заказать в футере)')
    def test_jump_after_click_logo_scooter_in_footer(self, driver):
        order_button = OrderPage(driver)
        logo_button = MainPage(driver)
        main_page = MainPage(driver)
        main_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        main_page.check_cookie()
        order_button.order_for_footer()
        logo_button.jump_after_click_logo_scooter()
        url = main_page.current_url()
        assert url == "https://qa-scooter.praktikum-services.ru/"
