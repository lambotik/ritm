from selenium.webdriver.common.by import By


class SimplePageLocators:
    ELEMENTS = (By.XPATH, "//h5[contains(text(), 'Elements')]")  # Тут тупил потому-то вместо XPATH CSS_SELECTOR
    BUTTONS = (By.XPATH, "//span[@class='text'][.='Buttons']")   # Тут тупил потому-то вместо XPATH CSS_SELECTOR
    DOUBLE_CLICK = (By.CSS_SELECTOR, 'button[id="rightClickBtn"')
    MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')

