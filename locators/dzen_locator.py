from selenium.webdriver.common.by import By

class Dzen_locator:
    DZEN_FIND = (By.XPATH,".//a[contains(@class, 'logoLink-2h') and contains(@aria-label, 'Логотип Бренда')]")
    POPUP_BROWSER_CLOSE = (By.XPATH, ".//span[@aria-label = 'Закрыть']")