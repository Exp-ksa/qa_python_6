import random

from datetime import datetime, timedelta
from locators.order_page_locator import Order_Page_locator
from locators.header_locator import Header_Locator
from locators.main_page_locator import Main_Page_Locator

class Credentials_1:
    first_name = "Кузьма"
    last_name = "Лебедев"
    address = "Москва, ш. Бульварное, 208"
    station = "1"
    phone = "+71231234567"
    date = (datetime.now() + timedelta(days=1 + random.randint(0, 15))).strftime('%d.%m.%Y')
    rental = "двое суток"
    color = Order_Page_locator.CHOICE_COLOR_SCOOTER_BLACK
    comments_courier = "Позвоните за 30 минут до приезда"
    button = Header_Locator.BUTTON_ORDER

class Credentials_2:
    first_name = "Яна"
    last_name = "Павлова"
    address = "Москва, пр. Коммунаров, д. 7"
    station = "214"
    phone = "83211234567"
    date = (datetime.now() + timedelta(days=1 + random.randint(0, 15))).strftime('%d.%m.%Y')
    rental = "семеро"
    color = Order_Page_locator.CHOICE_COLOR_SCOOTER_GREY
    comments_courier = "Вход со двора, второй подъезд"    
    button = Main_Page_Locator.BIG_BUTTON_ORDER

class Quest:
    quest_0 = ['0', '0','Сколько это стоит? И как оплатить?','Сутки — 400 рублей. Оплата курьеру — наличными или картой.']
    quest_1 = ['1','1', 'Хочу сразу несколько самокатов! Так можно?', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']
    quest_2 = ['2', '2', 'Как рассчитывается время аренды?', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']
    quest_3 = ['3', '3', 'Можно ли заказать самокат прямо на сегодня?', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']
    quest_4 = ['4', '4', 'Можно ли продлить заказ или вернуть самокат раньше?', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']
    quest_5 = ['5', '5', 'Вы привозите зарядку вместе с самокатом?', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']
    quest_6 = ['6', '6', 'Можно ли отменить заказ?','Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']
    quest_7 = ['7', '7', 'Я жизу за МКАДом, привезёте?', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']


    