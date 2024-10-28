from selenium import webdriver
from selenium.webdriver.common.by import By


class AssertionTest():
    pass


def test_lamdatest_radio_button():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    driver.find_element(By.XPATH,
                        "//h4[contains(text(),'Gender')]"
                        "//following::input[@value='Male']").click()
    driver.find_element(By.XPATH,
                        "//h4[contains(text(),'Age')]"
                        "//following::input[@value='15 - 50']").click()
    driver.find_element(By.XPATH,
                        "//button[text()='Get values']").click()
    gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
    age = driver.find_element(By.CSS_SELECTOR, ".groupradiobutton").text
    print("Gender Object: \t", id(gender))
    print("Male Object: \t", id("Male"))
    # assert gender == "Male", "gender is not correct"
    assert gender is "Male", "gender is not correct"  # IS compares 2 pbjects
    assert driver.title.__contains__("Selenium Grid Online")
    assert "51" in age, "age is not correct"
