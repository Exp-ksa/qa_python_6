import allure

#from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locator import Order_Page_locator
from locators.header_locator import Header_Locator
from locators.main_page_locator import Main_Page_Locator
from pages.base_page import BasePage

# Класс страницы заказа самоката
class OrderPageScooter(BasePage):

    @allure.step('Нажимаем кнопку принятия cookie')
    def click_cookie(self):
        self.click_element(Header_Locator.COOKIE_BUTTON)
    
    def wait_order_url(self):
        self.wait_for_element_visible(Order_Page_locator.WHO_IS_SCOOTER_TEXT)
        
    def check_url_order(self):
        return self.get_current_url()

    def set_fist_name(self, first_name):
        self.send_keys_to_element(Order_Page_locator.NAME_FIELD, first_name)

    def set_last_name(self, last_name):
        self.send_keys_to_element(Order_Page_locator.LAST_NAME_FIELD, last_name)
            
    def set_address(self, address):
        self.send_keys_to_element(Order_Page_locator.ADRESS_FIELD, address)
            
    def click_choice_metro(self, station):
        self.click_element(Order_Page_locator.METRO_FIELD)
        locator = (Order_Page_locator.CHOICE_METRO_BUTTON[0], Order_Page_locator.CHOICE_METRO_BUTTON[1].format(station))
        self.wait_for_element_visible(locator)
        self.scroll_to_element(locator)
        self.click_element(locator)
    
    def set_phone(self, phone):
        self.send_keys_to_element(Order_Page_locator.PHONE_FIELD, phone)

    def click_next_button(self):
        self.click_element(Order_Page_locator.NEXT_BUTTON)
    
    @allure.step('Заполнение формы для кого самокат')
    def fill_who_scooter_form(self, first_name, last_name, address, station, phone):
        self.set_fist_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.click_choice_metro(station)
        self.set_phone(phone)
        self.click_next_button()
    
      
    def set_date_rental(self, date):
        self.send_keys_to_element(Order_Page_locator.DATE_FIELD, date)
            
    def click_rental_time(self, rental):
        self.click_element(Order_Page_locator.RENTAL_TIME_FEILD)
        locator = (Order_Page_locator.CHOICE_RENTAL_TIME_BUTTON[0], Order_Page_locator.CHOICE_RENTAL_TIME_BUTTON[1].format(rental))
        self.wait_for_element_visible(locator)
        self.scroll_to_element(locator)
        self.click_element(locator)
    
    def click_color_scooter(self, color):
        self.click_element(color)
    
    def set_coments_courier(self, comment):
        self.send_keys_to_element(Order_Page_locator.COMMENTS_FIELD, comment)
    
    def click_order_button(self):
        self.click_element(Order_Page_locator.ORDER_BUTTON)
    
    @allure.step('Заполнение формы "Про аренду"')
    def fill_rent_form(self, date, rental, color, comment):
        self.set_date_rental(date)
        self.click_rental_time(rental)
        self.click_color_scooter(color)
        self.set_coments_courier(comment)
        self.click_order_button()
    
    @allure.step('Ожидание окна "Хотите оформить заказ?"')
    # Ожидание окна "Хотите оформить заказ?"
    def wait_popup_order(self):
        self.wait_for_element_visible(Order_Page_locator.POPUP_QUESTION_ORDER)
    
    # Клик по кнопке "Да"
    def click_order_yes(self):
        self.click_element(Order_Page_locator.BUTTON_ORDER_YES)
    
    @allure.step('Ожидание окна "Заказ оформлен"')
    # Ожидание окна "Заказ оформлен"
    def wait_order_placed(self):
        self.wait_for_element_visible(Order_Page_locator.ORDER_PLACED_TEXT)

    @allure.step('Получение текста "Заказ оформлен"')    
    def get_order_placed_text(self):
        return self.get_text_from_element(Order_Page_locator.ORDER_PLACED_TEXT)
    
    @allure.step('Клик по кнопке заказа {button}')
    def click_main_page_order_button(self, button):
        if button == Header_Locator.BUTTON_ORDER:
            self.scroll_to_element(button)
            self.click_element(button)
        else:
            self.wait_for_element_visible(button)
            self.scroll_to_element(button)
            self.click_element(button)    
