from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest, faker


link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    if "offer7" in link:
        pytest.xfail("This test is expected to fail for offer7")

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code_2()
    page.elements_matches()

@pytest.mark.xfail(reason="This test is expected to fail", strict=False)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="This test is expected to fail", strict=False)
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappearing_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_cart()
    page.should_be_no_items_in_the_cart()
    page.should_be_text_stating_cart_is_empty()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link_product)
        page.open()
        page.go_to_login_page()

        email = faker.Faker().email()
        password = "robot123!"

        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser): 
        page = ProductPage(browser, link_product)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_product)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.elements_matches()