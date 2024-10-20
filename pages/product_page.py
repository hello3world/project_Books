from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_book_to_busket(self):
        button_add_to_busket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add_to_busket.click()

    def get_name_book_from_product_cart(self):
        text_name_book = self.browser.find_element(
            *ProductPageLocators.NAME_BOOK).text
        return text_name_book

    def get_price_book_from_product_cart(self):
        text_price_book = self.browser.find_element(
            *ProductPageLocators.PRICE_BOOK).text
        return text_price_book

    def should_be_correct_name_product(self):
        text_name_book = self.get_name_book_from_product_cart()
        text_name_book_from_message = self.browser.find_element(
            *ProductPageLocators.NAME_BOOK_MESSAGE).text
        assert text_name_book == text_name_book_from_message, f"incorrect name book - {text_name_book}"

    def should_be_correct_price_product(self):
        text_price_book = self.get_price_book_from_product_cart()
        text_price_book_from_message = self.browser.find_element(
            *ProductPageLocators.PRICE_BOOK_MESSAGE).text
        assert text_price_book == text_price_book_from_message, f"incorrect name book - {text_price_book}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        login_link.click()

