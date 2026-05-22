import allure
import pytest

from pages.main_page import MainPageScooterFAQ
from data import Quest

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Раздел "Вопросы о важном"')
class TestFaqQuesttion:
    
    @allure.story('Проверка аккордеона FAQ')
    @allure.title('При клике на вопрос "{quest}" отображается соответствующий ответ')
    @allure.description('''
        Тест проверяет, что:
        1. При клике на вопрос в разделе FAQ открывается соответствующий текст
        2. Текст ответа соответствует ожидаемому
    ''')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('FAQ', 'Accordion', 'Smoke')
    @allure.link('https://qa-scooter.praktikum-services.ru', name='Главная страница')
    @pytest.mark.parametrize('questtion, answer, quest, answer_text', 
                             [
                                 ['0', '0', Quest.quest_0, Quest.answer_0], 
                                 ['1', '1', Quest.quest_1, Quest.answer_1],
                                 ['2', '2', Quest.quest_2, Quest.answer_2],
                                 ['3', '3', Quest.quest_3, Quest.answer_3],
                                 ['4', '4', Quest.quest_4, Quest.answer_4],
                                 ['5', '5', Quest.quest_5, Quest.answer_5],
                                 ['6', '6', Quest.quest_6, Quest.answer_6],
                                 ['7', '7', Quest.quest_7, Quest.answer_7]
                             ])
    def test_faq_accordion_opens_correct_answer(self, main_page, questtion, answer, quest, answer_text):
        
        driver = main_page
        
        faq_page = MainPageScooterFAQ(driver)
        faq_page.click_cookie()
        
        actual_text = faq_page.find_questtion_get_answer(questtion, answer)
        
        assert actual_text == answer_text