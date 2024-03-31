from pages.order_page import OrderPage
from pages.base_page import BasePage
from users import UserOne
from users import UserTwo
import allure
import pytest


class TestOrderForFooter:
    @allure.title('Оформление нового товара через кнопку Заказать в футере')
    @pytest.mark.parametrize('first_name, last_name, address, st_subway, phone, date, comment, expected_result',
                             [(UserOne.first_name, UserOne.last_name, UserOne.address, UserOne.st_subway, UserOne.phone,
                               UserOne.date, UserOne.comment, 'Заказ оформлен'),
                              (UserTwo.first_name, UserTwo.last_name, UserTwo.address, UserTwo.st_subway, UserTwo.phone,
                               UserTwo.date, UserTwo.comment, 'Заказ оформлен')])
    def test_order_page_for_footer(self, driver, first_name, last_name, address, st_subway, phone, date, comment,
                                   expected_result):
        page = OrderPage(driver)

        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        page.order_for_footer()
        order_for_footer_button_complete = page.order_scooter(first_name, last_name, address, st_subway, phone, date, comment)
        assert expected_result in order_for_footer_button_complete
