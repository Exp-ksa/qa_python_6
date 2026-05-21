import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locator import Main_Page_Locator, Main_Locator
from pages.navigation_menu import NavigationMenu

# Класс вопросы о важном
class MainPageScooterFAQ(NavigationMenu):

    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Ищем вопрос и скроллим к нему: {locator}')
    # Поиск вопроса
    def find_questtion(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Нажимаем по вопросу: {locator}')
    # Клик по вопросу
    def click_questtion(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получаем текст ответа: {locator}')
    # Получение текста ответа на вопрос
    def get_answer_text(self, locator):
        answer_text = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        return answer_text.text
        