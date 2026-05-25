from selenium.webdriver.common.by import By

class Header_Locator:
    LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    BUTTON_ORDER = (By.XPATH, ".//div[contains(@class, 'Header_Nav__AGCXC')]/button[contains(@class, 'Button_Button') and text()='Заказать']")
    ORDER_STATUS = (By.CSS_SELECTOR, "button.Header_Link__1TAG7")
    COOKIE_BUTTON = (By.XPATH, ".//button[@id = 'rcc-confirm-button']")