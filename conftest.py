import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function')
def driver():
    service = Service(GeckoDriverManager().install())
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--headless")
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
