from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/"
link_login = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  
    page.open()                         
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_be_login_page(browser):
    page = LoginPage(browser, link_login)
    page.open()
    page.should_be_login_page()

        