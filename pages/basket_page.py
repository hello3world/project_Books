from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BUTTON_PROCEED_TO_CHECKOUT)