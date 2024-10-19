from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_book_to_busket(self):
        button_add_to_busket = self.browser.find_element(*ProductPageLocators.BUTTON_TO_BUSKET)
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
        assert text_price_book == text_price_book_from_message, f"incorrect name book - {text_name_book}"