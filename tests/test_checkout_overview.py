from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestCheckoutOverview(BaseTest):
    def test_checkout_information_overview(self, inventory):
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
        assert checkout_overview_page.get_payment_information() == "SauceCard #31337", "payment info is wrong"
        assert checkout_overview_page.get_shipping_information() == "Free Pony Express Delivery!", \
            "Shipping address is wrong"
        assert checkout_overview_page.get_total_price_cart_list() == checkout_overview_page.items_total_price(), \
            "cart items totals are wrong"
        assert abs(checkout_overview_page.get_total_with_tax() - checkout_overview_page.items_total_price() * 1.08) < 0.01, \
            "Total with tax did not match the expected value"
        checkout_overview_page.finish_button_click()
        checkout_complete_page = CheckoutCompletePage(self.driver)
        assert checkout_complete_page.get_page_title().__contains__("Complete")
