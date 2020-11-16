from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM_ELEMENT = (By.CSS_SELECTOR, '#login_form')
    EMAIL_LOGIN_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_LOGIN_INPUT = (By.CSS_SELECTOR, '#id_login-password')
    SUBMIT_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTER_FORM_ELEMENT = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_PRICE_FROM_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.XPATH, '//*[@class="btn-group"]/a[contains(@href,"basket/")]')


class BasketPageLocators:
    ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
