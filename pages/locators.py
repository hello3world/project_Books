from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.XPATH, "//a[@class = 'btn btn-default']")

class LoginPageLocators():
    REGISTER_FORM_LINK = (By.XPATH, "//h2[text()='Войти']")
    LOGIN_FORM_LINK = (By.XPATH, "//h2[text()='Зарегистрироваться']")
    NAME_BOOK_MESSAGE = (By.XPATH, "//h2[text()='Зарегистрироваться']")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    PASSWORD_CONFIRM = (By.NAME, "registration-password2")
    BUTTON_REGISTER = (By.NAME, "registration_submit")

class ProductPageLocators():
    BUTTON_TO_BUSKET = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    NAME_BOOK = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")
    PRICE_BOOK = (By.XPATH, "//p[@class = 'price_color']")
    NAME_BOOK_MESSAGE = (By.XPATH, "//div[@class = 'alertinner ']/strong")
    PRICE_BOOK_MESSAGE = (By.XPATH, "//div[@class = 'alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class = 'alertinner ']")

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")
    BUTTON_PROCEED_TO_CHECKOUT = (By.XPATH, "//a[text() = 'Proceed to checkout']")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")