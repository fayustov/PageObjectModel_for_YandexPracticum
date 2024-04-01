from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_button_in_header = (By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    order_button_in_footer = (By.XPATH, ".//button[contains(@class, 'Button_UltraBig') and text() = 'Заказать']")
    first_name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    last_name_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    phone_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    st_subway_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
    next_step_order_button = (By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Далее']")
    when_delivery_order = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    time_rent = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    today_time_rent = (By.XPATH, ".//div[text()='сутки']")
    black_color_scooter = (By.ID, "black")
    comment_for_delivery = (By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']")
    accept_order_button = (By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']")
    complete_order_button = (By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Да']")
    order_info = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")
