from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestCheckoutInformationPage(BaseTest):
    def test_your_valid_information(self,inventory):
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
        assert checkout_overview_page.get_title_text().__contains__("Overview")

    def test_your_information_empty(self,inventory):
        inventory_page = inventory
        inventory_page.click_shop_cart_button()
        cart_page = CartPage(self.driver)
        cart_page.click_checkout_button()
        checkout_information_page = CheckoutInformationPage(self.driver)
        checkout_information_page.set_first_name("")
        checkout_information_page.set_last_name("")
        checkout_information_page.set_postal_code("")
        checkout_information_page.click_continue_button()
        assert checkout_information_page.get_error_message().__contains__("First Name")

    def test_your_information_no_lastname(self,inventory):
        inventory_page = inventory
        inventory_page.click_shop_cart_button()
        cart_page = CartPage(self.driver)
        cart_page.click_checkout_button()
        checkout_information_page = CheckoutInformationPage(self.driver)
        checkout_information_page.set_first_name(TestData.first_name)
        checkout_information_page.set_last_name("")
        checkout_information_page.set_postal_code(TestData.postal_code)
        checkout_information_page.click_continue_button()
        assert checkout_information_page.get_error_message().__contains__("Last Name")

    def test_your_information_no_postal_code(self,inventory):
        inventory_page = inventory
        inventory_page.click_shop_cart_button()
        cart_page = CartPage(self.driver)
        cart_page.click_checkout_button()
        checkout_information_page = CheckoutInformationPage(self.driver)
        checkout_information_page.set_first_name(TestData.first_name)
        checkout_information_page.set_last_name(TestData.last_name)
        checkout_information_page.set_postal_code("")
        checkout_information_page.click_continue_button()
        assert checkout_information_page.get_error_message().__contains__("Postal Code")
