import allure

#from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locator import Order_Page_locator
from pages.navigation_menu import NavigationMenu

# Класс страницы заказа самоката
class OrderPageScooter(NavigationMenu):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки страницы')
    def wait_order_url(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Order_Page_locator.WHO_IS_SCOOTER_TEXT))

    @allure.step('Проверка страницы заказа самоката')
    # Проверка страницы заказа самоката
    def check_url_order(self):
        return self.driver.current_url

    @allure.step('Ввод имени в поле "Имя"')
    # Ввод имени в поле "Имя"
    def set_fist_name(self, first_name):
        self.driver.find_element(*Order_Page_locator.NAME_FIELD).clear()
        self.driver.find_element(*Order_Page_locator.NAME_FIELD).send_keys(first_name)
    
    @allure.step('Ввод имени в поле "Фамилия"')
    # Ввод фамилии в поле "Фамилия"
    def set_last_name(self, last_name):
        self.driver.find_element(*Order_Page_locator.LAST_NAME_FIELD).clear()
        self.driver.find_element(*Order_Page_locator.LAST_NAME_FIELD).send_keys(last_name)
    
    @allure.step('Ввод имени в поле "Адрес"')
    # Ввод адреса в поле "Адрес"
    def set_address(self, address):
        self.driver.find_element(*Order_Page_locator.ADRESS_FIELD).clear()
        self.driver.find_element(*Order_Page_locator.ADRESS_FIELD).send_keys(address)
    
    @allure.step('Выбор станции метро')
    # Выбор станции метро
    def click_choice_metro(self, station):
        self.driver.find_element(*Order_Page_locator.METRO_FIELD).click()
        locator = (Order_Page_locator.CHOICE_METRO_BUTTON[0], Order_Page_locator.CHOICE_METRO_BUTTON[1].format(station))
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
        self.driver.find_element(*locator).click()
    
    @allure.step('Ввод телефонного номера')
    # Ввод телефонного номера
    def set_phone(self, phone):
        self.driver.find_element(*Order_Page_locator.PHONE_FIELD).clear()
        self.driver.find_element(*Order_Page_locator.PHONE_FIELD).send_keys(phone)
    
    @allure.step('Клик по кнопке "Далее"')
    # Клик по кнопке "Далее"
    def click_next_button(self):
        self.driver.find_element(*Order_Page_locator.NEXT_BUTTON).click()
    
    @allure.step('Ввод даты в поле "Когда привезти самокат"')
    # Ввод даты в поле "Когда привезти самокат"   
    def set_date_rental(self, date):
        self.driver.find_element(*Order_Page_locator.DATE_FIELD).clear()
        self.driver.find_element(*Order_Page_locator.DATE_FIELD).send_keys(date)
    
    @allure.step('Выбор срока аренды')
    # Выбор срока аренды
    def click_rental_time(self, rental):
        self.driver.find_element(*Order_Page_locator.RENTAL_TIME_FEILD).click()
        locator = (Order_Page_locator.CHOICE_RENTAL_TIME_BUTTON[0], Order_Page_locator.CHOICE_RENTAL_TIME_BUTTON[1].format(rental))
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
        self.driver.find_element(*locator).click()
    
    @allure.step('Выбор цвета самоката')
    # Выбор цвета самоката   
    def click_color_scooter(self, color):
        self.driver.find_element(*color).click()
    
    @allure.step('Ввод комментария в поле "Комментарий"')
    # Ввод комментария в поле "Комментарий"
    def set_coments_courier(self, comment):
        self.driver.find_element(*Order_Page_locator.COMMENTS_FIELD).send_keys(comment)
    
    @allure.step('Клик по кнопке "Заказать"')
    # Клик по кнопке "Заказать"
    def click_order_button(self):
        self.driver.find_element(*Order_Page_locator.ORDER_BUTTON).click()
    
    @allure.step('Ожидание окна "Хотите оформить заказ?"')
    # Ожидание окна "Хотите оформить заказ?"
    def wait_popup_order(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Order_Page_locator.POPUP_QUESTION_ORDER))
    
    @allure.step('Клик по кнопке "Да"')
    # Клик по кнопке "Да"
    def click_order_yes(self):
        self.driver.find_element(*Order_Page_locator.BUTTON_ORDER_YES).click()
    
    @allure.step('Ожидание окна "Заказ оформлен"')
    # Ожидание окна "Заказ оформлен"
    def wait_order_placed(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Order_Page_locator.ORDER_PLACED_TEXT))

    @allure.step('Получение текста "Заказ оформлен"')    
    def get_order_placed_text(self):
        order = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Order_Page_locator.ORDER_PLACED_TEXT))
        return order.text
    
        
