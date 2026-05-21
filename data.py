import random

from datetime import datetime, timedelta
from locators.locator import Order_Page_locator, Main_Locator

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
    button = Main_Locator.BUTTON_ORDER

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
    button = Main_Locator.BIG_BUTTON_ORDER