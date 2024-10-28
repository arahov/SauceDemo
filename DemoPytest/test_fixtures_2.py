import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def start_automation_fixture():
    print("Start Test With Automatic Fixture")


@pytest.fixture(scope="function")
def setup_teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    driver.maximize_window()
    driver.find_element(By.ID, "input-email").send_keys("arahotest@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("@1234arahotest")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    print("Log In")
    yield
    driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
    print("Log Out")


@pytest.mark.usefixtures("setup_teardown")
def test1_order_history_title():
    driver.find_element(By.PARTIAL_LINK_TEXT, "Order").click()
    assert driver.title == "Order History"
    print("Test 1 is Complete")


@pytest.mark.usefixtures("setup_teardown")
def test2_change_password():
    driver.find_element(By.PARTIAL_LINK_TEXT, "Password").click()
    assert driver.title == "Change Password"
    print("Test 2 is Complete")
