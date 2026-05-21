import allure
import pytest

from locators.locator import Main_Page_Locator
from pages.main_page import MainPageScooterFAQ

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Раздел "Вопросы о важном"')
class TestFaqQuesttion:
    
    @allure.story('Проверка аккордеона FAQ')
    @allure.title('При клике на вопрос "{questtion}" отображается соответствующий ответ')
    @allure.description('''
        Тест проверяет, что:
        1. При клике на вопрос в разделе FAQ открывается соответствующий текст
        2. Текст ответа соответствует ожидаемому
    ''')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('FAQ', 'Accordion', 'Smoke')
    @allure.link('https://qa-scooter.praktikum-services.ru', name='Главная страница')
    @pytest.mark.parametrize('questtion, answer, answer_text', 
                             [
                                 [Main_Page_Locator.FAQ_QUESTION_PRICE, Main_Page_Locator.FAQ_ANSWER_PRICE, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'], 
                                 [Main_Page_Locator.FAQ_QUESTION_SEVERAL_SCOOTERS, Main_Page_Locator.FAQ_ANSWER_SEVERAL_SCOOTERS,'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                                 [Main_Page_Locator.FAQ_QUESTION_TIME, Main_Page_Locator.FAQ_ANSWER_TIME, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                                 [Main_Page_Locator.FAQ_QUESTION_ORDER_TODAY, Main_Page_Locator.FAQ_ANSWER_ORDER_TODAY, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                                 [Main_Page_Locator.FAQ_QUESTION_EXTEND_RETURN, Main_Page_Locator.FAQ_ANSWER_EXTEND_RETURN, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                                 [Main_Page_Locator.FAQ_QUESTION_CHARGE, Main_Page_Locator.FAQ_ANSWER_CHARGE, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                                 [Main_Page_Locator.FAQ_QUESTION_CANCEL_ORDER, Main_Page_Locator.FAQ_ANSWER_CANCEL_ORDER, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                                 [Main_Page_Locator.FAQ_QUESTION_MKAD, Main_Page_Locator.FAQ_ANSWER_MKAD, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
                             ])
    def test_faq_accordion_opens_correct_answer(self, main_page, questtion, answer, answer_text):
        
        driver = main_page
        
        faq_page = MainPageScooterFAQ(driver)
        
        faq_page.find_questtion(questtion)
        
        faq_page.click_questtion(questtion)
        
        actual_text = faq_page.get_answer_text(answer)
        
        assert actual_text == answer_text