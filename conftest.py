import pytest
from selenium import webdriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utilities.test_data import TestData


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif request.param == "edge":
        driver = webdriver.Edge()
        driver.maximize_window()

    request.cls.driver = driver  # Attach the driver to the test class instance
    driver.get(TestData.url)  # Navigate to the desired URL
    yield driver  # Yield the driver for use in other fixtures or tests

    driver.close()  # Close the driver after the test completes


@pytest.fixture()
def login(initialize_driver):
    def _login(username=TestData.username, password=TestData.password):
        login_page = LoginPage(initialize_driver)
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login_button()
        return login_page  # Return the login page object for further use

    return _login  # Return the _login function, not the login_page object


@pytest.fixture()
def inventory(login, initialize_driver):
    # Call the login function to perform the login and get the driver
    login()  # Use the default credentials or provide custom ones if needed
    inventory_page = InventoryPage(initialize_driver)  # Pass the driver instance to InventoryPage
    inventory_page.click_set_filter_lower_to_higher()
    inventory_page.click_add_item_to_cart_button()
    return inventory_page
