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
                                 [Quest.quest_0[0], Quest.quest_0[1], Quest.quest_0[2], Quest.quest_0[3]], 
                                 [Quest.quest_1[0], Quest.quest_1[1], Quest.quest_1[2], Quest.quest_1[3]],
                                 [Quest.quest_2[0], Quest.quest_2[1], Quest.quest_2[2], Quest.quest_2[3]],
                                 [Quest.quest_3[0], Quest.quest_3[1], Quest.quest_3[2], Quest.quest_3[3]],
                                 [Quest.quest_4[0], Quest.quest_4[1], Quest.quest_4[2], Quest.quest_4[3]],
                                 [Quest.quest_5[0], Quest.quest_5[1], Quest.quest_5[2], Quest.quest_5[3]],
                                 [Quest.quest_6[0], Quest.quest_6[1], Quest.quest_6[2], Quest.quest_6[3]],
                                 [Quest.quest_7[0], Quest.quest_7[1], Quest.quest_7[2], Quest.quest_7[3]]
                             ])
    def test_faq_accordion_opens_correct_answer(self, main_page, questtion, answer, quest, answer_text):
        
        driver = main_page
        
        faq_page = MainPageScooterFAQ(driver)
        faq_page.click_cookie()
        
        actual_text = faq_page.find_questtion_get_answer(questtion, answer)
        
        assert actual_text == answer_text