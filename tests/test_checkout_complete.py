from conftest import inventory
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestCheckoutComplete(BaseTest):
    def test_go_back_home(self, inventory):
        inventory_page = inventory
        inventory_page.click_shop_cart_button()
        cart_page = CartPage(self.driver)
        cart_page.click_checkout_button()
        checkout_information_page = CheckoutInformationPage(self.driver)
        checkout_information_page.set_first_name(TestData.first_name)
        checkout_information_page.set_last_name(TestData.last_name)
        checkout_information_page.set_postal_code(TestData.postal_code)
        checkout_information_page.click_continue_button()
        checkout_overview_page = CheckoutOverviewPage(self.driver)
        checkout_overview_page.finish_button_click()
        checkout_complete_page = CheckoutCompletePage(self.driver)
        checkout_complete_page.click_button_back_home()
        assert inventory_page.get_title_text() == "Products"
