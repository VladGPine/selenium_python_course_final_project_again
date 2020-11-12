from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM_ELEMENT = (By.CSS_SELECTOR, '#login_form')
    EMAIL_LOGIN_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_LOGIN_INPUT = (By.CSS_SELECTOR, '#id_login-password')
    SUBMIT_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTER_FORM_ELEMENT = (By.CSS_SELECTOR, '#register_form')
