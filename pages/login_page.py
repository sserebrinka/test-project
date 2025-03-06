from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Invalid url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), "Register form is not presented"
    
    def should_be_button_register(self):
        assert self.is_element_present(*LoginPageLocators.BUTTON_REGISTER), "Button register is not presented"
    
    def register_new_user(self, email, password):
        self.should_be_register_form()
        
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_2).send_keys(password)

        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()
