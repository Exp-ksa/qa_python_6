import allure
import pytest

from pages.navigation_menu import NavigationMenu

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Переходы по лого')
class TestLinkScooter:
    
    @allure.story('Проверка переходов по логотипам')
    @allure.title('При клике на лого Самокат выполняется переход на главную со страницы "{page_name}"')
    @allure.description('''
        Тест проверяет, что:
        1. При клике на лого Самокат выполняется переход на главную страницу
        2. Открыта главная страница с заголовком "Самокат"
    ''')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('Link Logo Scooter', 'Smoke')
    @pytest.mark.parametrize('page_fixture, page_name, ', 
                            [ ['order_page', 'заказа'],
                              ['track_page', 'отслеживания'],
                            ])
    def test_link_scooter_from_page_open_main_page(self, request, page_fixture, page_name):
        # Получаем фикстуру по имени
        driver = request.getfixturevalue(page_fixture)
        link_page = NavigationMenu(driver)

        link_page.click_scooter_logo()
        link_page.wait_header_scooter()
        
        assert 'Самокат' in link_page.get_header_scooter_text()
    