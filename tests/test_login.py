import pytest

from pages.inventory_page import InventoryPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test_valid_credentials(self, login):
        login_page = login()
        inventory_page = InventoryPage(self.driver)
        actual_title = inventory_page.get_title_text()
        assert actual_title == "Products"

    def test_invalid_credentials(self, login):
        login_page = login(username="invalid_user", password="invalid_password")
        assert login_page.error_text_displayed().__contains__("Username and password do not match")

    def test_no_username(self, login):
        login_page = login(username="", password="invalid_password")
        assert login_page.error_text_displayed().__contains__("Username is required")

    def test_no_password(self, login):
        login_page = login(username="some_user", password="")
        assert login_page.error_text_displayed().__contains__("Password is required")
