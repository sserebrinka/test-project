from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")   # invalid link

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    SEE_CART_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    CART_IS_EMPTY_LINK = (By.CSS_SELECTOR, "#content_inner p a")
    CART_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")

    EMAIL_REGISTER = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTER_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REGISTER_2 = (By.CSS_SELECTOR, "#id_registration-password2")

    BUTTON_REGISTER = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, ".alert:nth-child(1) div.alertinner strong")
    PRODUCT_VALUE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_VALUE = (By.CSS_SELECTOR, ".alert:nth-child(3) div.alertinner strong")
