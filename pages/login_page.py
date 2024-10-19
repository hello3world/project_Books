import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == 'https://selenium1py.pythonanywhere.com/ru/accounts/login/', 'current login is not equal'

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login link is not presented"

    def should_be_register_form(self):
        self.is_element_present(
            *LoginPageLocators.REGISTER_FORM_LINK), "Login link is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(f"{email}")
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.BUTTON_REGISTER).click()