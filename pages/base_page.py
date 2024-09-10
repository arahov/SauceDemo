from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    the Purpose of BasePage is to contain methods used in all pages
    """

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def click(self, locator):
        self.find(*locator).click()

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def click_add_remove_to_cart(self, add_remove, item_number):
        # Convert item_number to string and properly concatenate the XPath
        if add_remove == "add_item":
            item_xpath = (f"//div[@class='inventory_list']/div[@class='inventory_item'][{item_number}]//button[contains(@class, 'btn_primary')]")

        else:
            item_xpath = (f"//div[@class='inventory_list']/div[@class='inventory_item'][{item_number}]//button[contains(@class , 'btn_secondary')]")
        # Find the item and click the button
        item = self.find(By.XPATH, item_xpath)
        item.click()

    def get_checkout_text(self, checkout_child_element_number):
        overview = self.find(By.XPATH, f"//div[@class='summary_info']/div[{checkout_child_element_number}]").text
        return overview

    def get_item_price_text(self, item_number):
        item_price = self.find(By.XPATH, f"//div[@class='cart_list']/div[{item_number}]/following::div[7]")
        return item_price

    # checks if error-button is displayed
    def wait_element_is_displayed(self, locator, timeout=10):
        """
        Waits for an element to be present on the page and returns it.

        :param locator: the selector method and locator
        :param timeout: Maximum time to wait for the element (in seconds)
        :return: WebElement once it is found and present on the page
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.is_displayed()

    def wait_element_get_text(self, locator, timeout=10):
        """
        Waits for an element to be present on the page and returns it.

        :param locator: the selector method and locator
        :param timeout: Maximum time to wait for the element (in seconds)
        :return: WebElement once it is found and present on the page
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text
