import softest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AssertionTest(softest.TestCase):
    pass


    def test_lamdatest_radio_button(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
        driver.find_element(By.XPATH,
                            "//h4[contains(text(),'Gender')]//following::input[@value='Male']").click()
        driver.find_element(By.XPATH,
                            "//h4[contains(text(),'Age')]//following::input[@value='15 - 50']").click()
        driver.find_element(By.XPATH,"//button[text()='Get values']").click()
        gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
        age = driver.find_element(By.CSS_SELECTOR, ".groupradiobutton").text
        self.soft_assert(self.assertIs("male", gender, "Gender Os Not Correct"))
        self.soft_assert(self.assertTrue(driver.title.__contains__("Selenium Grid Online")))
        self.soft_assert(self.assertIn("51",age,"Age is not correct"))
        self.assert_all("verify Gender , title, Age")
