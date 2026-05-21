import pytest
import allure

from selenium import webdriver
from selenium.webdriver.firefox.options import Options # Firefox

from url import MAIN_URL, ORDER_URL, TRACK_URL  

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--start-maximized') 
    options.add_argument('--disable-popup-blocking')  # Отключить блокировку всплывающих окон
    driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(5)
    yield driver

    driver.quit()

@pytest.fixture(scope="function")
@allure.step('Открываем браузер Firefox на главной странице')
def main_page(driver):
    driver.get(MAIN_URL)
    return driver


@pytest.fixture(scope="function")
@allure.step('Открываем браузер Firefox на странице заказа самоката')
def order_page(driver):
    driver.get(ORDER_URL)
    return driver

@pytest.fixture(scope="function")
@allure.step('Открываем браузер Firefox на странице отслеживания заказа самоката') 
def track_page(driver):
    driver.get(TRACK_URL)
    return driver

