import allure
import pytest

from pages.header_menu import NavigationTransitions

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Переходы по лого')
class TestLinkScooter:
    
    @allure.story('Проверка переходов по логотипам')
    @allure.title('При клике на лого Яндекс выполняется переход на главную со страницы "{page_name}"')
    @allure.description('''
        Тест проверяет, что:
        1. При клике на лого Яндекс выполняется переход на страницу Dzen
        2. Открыта главная страница Dzen
    ''')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('Link Logo Yandex', 'Smoke')
    @pytest.mark.parametrize('page_fixture, page_name, ', 
                            [ ['order_page', 'заказа'],
                              ['track_page', 'отслеживания'],
                            ])
    def test_link_scooter_from_page_open_main_page(self, request, page_fixture, page_name):
        # Получаем фикстуру по имени
        driver = request.getfixturevalue(page_fixture)
        link_page = NavigationTransitions(driver)

        url = link_page.click_yandex_logo_and_switch_to_new_tab()
        
        assert 'dzen.ru' in url
    