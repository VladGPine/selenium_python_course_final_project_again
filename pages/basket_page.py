from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, \
            'This is not the basket page'

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), \
            'Items presented on basket page, but should not'

    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert 'Your basket is empty' in empty_basket_message, \
            'Basket is not empty'
