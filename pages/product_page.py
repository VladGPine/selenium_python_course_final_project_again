from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            'No any add to basket button on the product page'

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message_after_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'No any success message on the product page'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is on the product page, but should not be'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message still on the page'

    def added_product_should_has_the_same_title(self, product_title):
        success_adding_message_element = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert product_title == success_adding_message_element.text, \
            'Product title not equal title in success message'

    def should_be_product_price_message_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_FROM_BASKET_MESSAGE), \
            'No any price message in basket on the product page'

    def product_price_in_basket_should_be_equal_the_product_price(self, product_price):
        product_price_from_basket_message_element = self.browser\
            .find_element(*ProductPageLocators.PRODUCT_PRICE_FROM_BASKET_MESSAGE)
        assert product_price in product_price_from_basket_message_element.text, \
            'Product price not equal price in basket message'

    def get_the_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_the_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
