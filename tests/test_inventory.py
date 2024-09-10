import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from tests.base_test import BaseTest


class TestInventory(BaseTest):
    def test_inventory_add_items_to_cart(self, inventory):
        inventory_page = inventory
        actual_number_of_items = inventory_page.get_shop_cart_number_of_items_text()
        assert actual_number_of_items == "2"
        inventory_page.click_shop_cart_button()
        cart_page = CartPage(self.driver)
        assert cart_page.get_curt_page_title() == "Your Cart"

    # add 2 items to the cart and then remove 1 item
    @pytest.mark.smoke
    def test_inventory_add_remove_items_cart(self, inventory):
        inventory_page = inventory
        inventory_page.click_remove_item_from_cart_button()
        # assert that the cart shows 1 item
        actual_number_of_items = inventory_page.get_shop_cart_number_of_items_text()
        assert actual_number_of_items == "1"
