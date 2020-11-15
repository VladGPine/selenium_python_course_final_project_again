from .pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_should_see_add_to_basket_button(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_basket_button()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message_after_adding_to_basket()
    page.added_product_should_has_the_same_title(page.get_the_product_title())
    page.should_be_product_price_message_in_basket()
    page.product_price_in_basket_should_be_equal_the_product_price(page.get_the_product_price())
