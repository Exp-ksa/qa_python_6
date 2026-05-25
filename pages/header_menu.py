import allure

from locators.header_locator import Header_Locator
from locators.dzen_locator import Dzen_locator
from locators.main_page_locator import Main_Page_Locator
from pages.base_page import BasePage

class NavigationTransitions(BasePage):

    @allure.step('Нажимаем кнопку принятия cookie')
    def click_cookie(self):
        self.click_element(Header_Locator.COOKIE_BUTTON)
    
    def click_yandex_logo(self):
        self.click_element(Header_Locator.LOGO_YANDEX)
    
    def click_scooter_logo(self):
        self.click_element(Header_Locator.LOGO_SCOOTER)

    def get_header_scooter_text(self):
        return self.get_text_from_element(Main_Page_Locator.HEADER_SCOOTER)
    
    def get_current_url_dzen(self):
        return self.get_current_url()
    
    def get_current_url_scooter(self):
        return self.get_current_url()
      
    @allure.step('Проверка открытия новой вкладки и получение URL')
    def click_yandex_logo_and_switch_to_new_tab(self):
        self.click_yandex_logo()
        self.wait_for_window_contains(2)
        self.switch_to_window()

        if self.popup_displayed(Dzen_locator.POPUP_BROWSER_CLOSE):
            self.click_element(Dzen_locator.POPUP_BROWSER_CLOSE)
        
        self.wait_for_element_visible(Dzen_locator.DZEN_FIND)
                
        return self.get_current_url_dzen()

    

    

    


    
    