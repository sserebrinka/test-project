from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math, re


class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        self.should_be_button()
        self.click_to_button()
        print("Product added to cart")
    
    def elements_matches(self):
        self.should_be_disappearing_message()
        self.should_not_be_success_message()
        self.should_be_elements_before_add()
        self.should_be_elements_after_add()
        self.should_be_values_match()
    
    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), 'Button "add to basker" is not presented'

    def should_be_elements_before_add(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_VALUE), "Product value is not presented"

    def should_be_elements_after_add(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_CART), "Product name in cart is not presented"
        assert self.is_element_present(*ProductPageLocators.CART_VALUE), "Cart value is not presented"

    def should_be_values_match(self):
        product_name_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_cart_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text

        product_value_text = re.findall(r'\d+', self.browser.find_element(*ProductPageLocators.PRODUCT_VALUE).text)
        cart_value_text = re.findall(r'\d+', self.browser.find_element(*ProductPageLocators.CART_VALUE).text)

        assert product_name_text == product_name_in_cart_text, "The name of the products does not match"
        assert product_value_text == cart_value_text, "The values of the goods do not match"
    
    def click_to_button(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def solve_quiz_and_get_code_parametrize(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_CART), \
        "Success message is presented, but should not be"
    
    def should_be_disappearing_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_CART), \
        "Success message is presented, but it must disappear"
        