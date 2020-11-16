from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'This is not a login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_ELEMENT), \
            'No any login form element'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_ELEMENT), \
            'No any register form element'

    def register_new_user(self, email, password):
        registration_email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_INPUT)
        registration_email_password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_INPUT)
        confirm_registration_email_password_input = self.browser.find_element(*LoginPageLocators
                                                                              .CONFIRM_PASSWORD_REGISTER_INPUT)
        registration_submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTER_BUTTON)

        registration_email_input.send_keys(email)
        registration_email_password_input.send_keys(password)
        confirm_registration_email_password_input.send_keys(password)
        registration_submit_button.click()