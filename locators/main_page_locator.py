from selenium.webdriver.common.by import By

class Main_Page_Locator: 
    HEADER_SCOOTER = (By.CLASS_NAME, "Home_Header__iJKdX")
    BIG_BUTTON_ORDER = (By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[contains(text(), 'Заказать')]")   
    FAQ_QUESTION = (By.ID, "accordion__heading-{}")
    FAQ_ANSWER = (By.XPATH, ".//div[(@class = 'accordion__panel' and @aria-labelledby='accordion__heading-{}')]")