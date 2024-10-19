from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM_LINK = (By.XPATH, "//h2[text()='Войти']")
    LOGIN_FORM_LINK = (By.XPATH, "//h2[text()='Зарегистрироваться']")
    NAME_BOOK_MESSAGE = (By.XPATH, "//h2[text()='Зарегистрироваться']")

class ProductPageLocators():
    BUTTON_TO_BUSKET = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    NAME_BOOK = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")
    PRICE_BOOK = (By.XPATH, "//div[@class = 'price_color']")
    NAME_BOOK_MESSAGE = (By.XPATH, "//div[@class = 'alertinner ']/strong")
    PRICE_BOOK_MESSAGE = (By.XPATH, "//div[@class = 'alertinner ']/p/strong")
