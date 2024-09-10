from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    checkout_button = (By.ID, "checkout")
    page_title = (By.CLASS_NAME, 'title')
    continue_shopping_button = (By.ID, "continue-shopping")

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout_button(self):
        self.click(self.checkout_button)

    def get_curt_page_title(self):
        return self.get_text(self.page_title)

    def click_continue_shopping_button(self):
        self.click(self.continue_shopping_button)
