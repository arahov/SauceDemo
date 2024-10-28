import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("num1, num2, expected_total",
                         [
                             ("25","25","50"),
                             ("10","10","30"),
                             ("30","40","70")
                         ])
def test_lambdatest_two_input_fields(num1, num2, expected_total):
    # driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.ID,"sum1").send_keys(num1)
    driver.find_element(By.ID, "sum2").send_keys(num2)
    driver.find_element(By.XPATH,"//button[text()='Get Sum']").click()
    actual_total = driver.find_element(By.ID,"addmessage").text
    assert actual_total == expected_total, "Actual & Expected Totals Do Not Match"
    driver.quit()

@pytest.mark.parametrize("base",[1,2,3])
@pytest.mark.parametrize("exponent",[4,5,6])
def test_raising_base_to_power(base,exponent):
    result = base ** exponent
    assert result == math.pow(base,exponent)
