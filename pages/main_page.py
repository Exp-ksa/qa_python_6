import allure

from pages.base_page import BasePage
from locators.main_page_locator import Main_Page_Locator
from locators.header_locator import Header_Locator

# Класс вопросы о важном
class MainPageScooterFAQ(BasePage):

         
    def click_questtion(self, locator):
        self.click_element(locator)

    @allure.step('Нажимаем кнопку принятия cookie')
    def click_cookie(self):
        self.click_element(Header_Locator.COOKIE_BUTTON)

    def find_questtion_get_answer(self, quest, answer):
        quest = (Main_Page_Locator.FAQ_QUESTION[0], Main_Page_Locator.FAQ_QUESTION[1].format(quest))
        answer = (Main_Page_Locator.FAQ_ANSWER[0], Main_Page_Locator.FAQ_ANSWER[1].format(answer))
        self.scroll_to_element(quest)
        self.wait_for_element_visible(quest)
        self.click_questtion(quest)
        
        return self.get_text_from_element(answer)