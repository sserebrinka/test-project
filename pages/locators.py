from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")   # invalid link


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, ".alert:nth-child(1) div.alertinner strong")
    PRODUCT_VALUE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_VALUE = (By.CSS_SELECTOR, ".alert:nth-child(3) div.alertinner strong")
