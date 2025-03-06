from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators, MainPageLocators
from .languages import *


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        self.should_be_login_link()
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
    
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_cart(self):
        self.should_be_see_cart_link()
        self.browser.find_element(*MainPageLocators.SEE_CART_LINK).click()
    
    def should_be_see_cart_link(self):
        assert self.is_element_present(*MainPageLocators.SEE_CART_LINK), "See cart link is not presented"

    def should_be_no_items_in_the_cart(self):
        assert self.is_not_element_present(*MainPageLocators.CART_ITEMS), "There are items in the basket, but they shouldn't be"

    def should_be_text_stating_cart_is_empty(self):
        cart_message_link = self.browser.find_element(*MainPageLocators.CART_IS_EMPTY_LINK).text
        cart_message = self.browser.find_element(*MainPageLocators.CART_IS_EMPTY).text
        cart_message = cart_message.replace(cart_message_link, " ").strip()

        current_language = get_language_from_ui(cart_message)
        expected_language = languages.get(current_language, "There is no available language")

        assert cart_message == expected_language, "There is no empty bucket message"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True
    
    