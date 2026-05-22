import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options # Firefox

from url import MAIN_URL, ORDER_URL, TRACK_URL  

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--disable-popup-blocking')  # Отключить блокировку всплывающих окон
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()

    driver.implicitly_wait(5)
    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    driver.get(MAIN_URL)
    return driver


@pytest.fixture(scope="function")
def order_page(driver):
    driver.get(ORDER_URL)
    return driver

@pytest.fixture(scope="function")
def track_page(driver):
    driver.get(TRACK_URL)
    return driver

