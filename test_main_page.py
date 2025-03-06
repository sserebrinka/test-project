from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"
link_login = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    page.should_be_no_items_in_the_cart()
    page.should_be_text_stating_cart_is_empty()

        