from pages import login_page
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestCart(BaseTest):
    def test_checkout(self, inventory):
        inventory_page = inventory
        inventory_page.click_shop_cart_button()
        cart_page = CartPage(self.driver)
        cart_page.click_checkout_button()
        checkout_information_page = CheckoutInformationPage(self.driver)
        assert checkout_information_page.get_checkout_title_text().__contains__("Your Information")

    def test_continue_shopping(self, inventory):
        inventory_page = inventory
        inventory_page.click_shop_cart_button()
        cart_page = CartPage(self.driver)
        cart_page.click_continue_shopping_button()
        assert inventory_page.get_title_text() == "Products"
