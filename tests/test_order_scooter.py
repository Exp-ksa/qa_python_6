import allure
import pytest

from pages.order_page import OrderPageScooter
from data import Credentials_1, Credentials_2

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Раздел "Заказ самоката"')
class TestOrderScooter:
    
    @allure.story('Проверка заказа самоката')
    @allure.title('Заказ самоката с заполнением всех полей в форме заказа')
    @allure.description('''
        Заказ самоката. Проверка флоу позитивного сценария с двумя наборами данных. 
        Проверка двух точки входа в сценарий: кнопка «Заказать» вверху страницы и внизу.
    ''')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('Order', 'Positive', 'Smoke')
    @allure.link('https://qa-scooter.praktikum-services.ru/order', name='Страница заказа')
    @pytest.mark.parametrize('first_name, last_name, address, station, phone, date, rental, color, comments_courier, button', 
                             [
                                 [Credentials_1.first_name, Credentials_1.last_name, Credentials_1.address, Credentials_1.station, Credentials_1.phone, Credentials_1.date, Credentials_1.rental, Credentials_1.color, Credentials_1.comments_courier, Credentials_1.button], 
                                 [Credentials_2.first_name, Credentials_2.last_name, Credentials_2.address, Credentials_2.station, Credentials_2.phone, Credentials_2.date, Credentials_2.rental, Credentials_2.color, Credentials_2.comments_courier, Credentials_2.button]
                             ])
    def test_scooter_order_positive_flow(self, main_page, first_name, last_name, address, station, phone, date, rental, color, comments_courier, button):
        
        driver = main_page
        order_page = OrderPageScooter(driver)
        order_page.click_cookie_button()
        
        order_page.click_main_page_order_button(button)
        order_page.wait_order_url()

        assert 'order' in order_page.check_url_order()

        order_page.set_fist_name(first_name)
        order_page.set_last_name(last_name)
        order_page.set_address(address)
        order_page.click_choice_metro(station)
        order_page.set_phone(phone)
        order_page.click_next_button()

        order_page.set_date_rental(date)
        order_page.click_rental_time(rental)
        order_page.click_color_scooter(color)
        order_page.set_coments_courier(comments_courier)
        order_page.click_order_button()
        order_page.wait_popup_order()
        order_page.click_order_yes()
        order_page.wait_order_placed()

        assert 'Заказ оформлен' in order_page.get_order_placed_text()