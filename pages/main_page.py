from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators
from .languages import *


class MainPage(BasePage):
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)

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
        
    
                
                