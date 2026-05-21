import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locator import Main_Locator

class NavigationMenu:

    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на кнопку принятия cookie')
    def click_cookie_button(self):
        self.driver.find_element(*Main_Locator.COOKIE_BUTTON).click()

    @allure.step('Нажатие на логотип Яндекс')
    def click_yandex_logo(self):
        self.driver.find_element(*Main_Locator.LOGO_YANDEX).click()
    
    @allure.step('Проверка открытия новой вкладки и получение URL')
    def click_yandex_logo_and_switch_to_new_tab(self):
        self.click_yandex_logo()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windows_after = self.driver.window_handles    
        self.driver.switch_to.window(windows_after[-1])
        
        popup_elements = self.driver.find_elements(*Main_Locator.POPUP_BROWSER_CLOSE)
        if popup_elements and popup_elements[0].is_displayed():
            popup_elements[0].click()
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Main_Locator.DZEN_FIND))
        
        return self.driver.current_url

    @allure.step('Нажатие на логотип Самокат')
    def click_scooter_logo(self):
        self.driver.find_element(*Main_Locator.LOGO_SCOOTER).click()

    @allure.step('Ожидание загрузки логотипа')
    def wait_header_scooter(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Main_Locator.HEADER_SCOOTER))

    @allure.step('Получение текста заголовка')
    def get_header_scooter_text(self):
        text = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Main_Locator.HEADER_SCOOTER))
        return text.text

    @allure.step('Клик по кнопке заказа {button}')
    def click_main_page_order_button(self, button):
        if button == Main_Locator.BUTTON_ORDER:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*button))
            self.driver.find_element(*button).click()
        else:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(button))
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*button))
            self.driver.execute_script("arguments[0].focus();", element)
            element.click()

    


    
    