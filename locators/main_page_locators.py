from selenium.webdriver.common.by import By


class Locators:
    question_one_button = (By.ID, "accordion__heading-0")
    answer_question_one = (By.ID, "accordion__panel-0")
    question_two_button = (By.ID, "accordion__heading-1")
    answer_question_two = (By.ID, "accordion__panel-1")
    question_three_button = (By.ID, "accordion__heading-2")
    answer_question_three = (By.ID, "accordion__panel-2")
    question_four_button = (By.ID, "accordion__heading-3")
    answer_question_four = (By.ID, "accordion__panel-3")
    question_five_button = (By.ID, "accordion__heading-4")
    answer_question_five = (By.ID, "accordion__panel-4")
    question_six_button = (By.ID, "accordion__heading-5")
    answer_question_six = (By.ID, "accordion__panel-5")
    question_seven_button = (By.ID, "accordion__heading-6")
    answer_question_seven = (By.ID, "accordion__panel-6")
    question_eight_button = (By.ID, "accordion__heading-7")
    answer_question_eight = (By.ID, "accordion__panel-7")
    logo_scooter = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    logo_yandex = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    cookie_message = (By.ID, 'rcc-confirm-button')
    dzen_page_id = (By.ID, "__SVG_SPRITE_NODE__")
