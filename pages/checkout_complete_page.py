from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    # checkout_complete_page locators
    page_title = (By.CLASS_NAME, "title")
    button_back_home = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_text(self.page_title)

    def click_button_back_home(self):
        self.click(self.button_back_home)
