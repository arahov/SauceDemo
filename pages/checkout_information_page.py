from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutInformationPage(BasePage):
    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    postal_code_field = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    checkout_page_title = (By.CLASS_NAME, "title")
    error_message = (By.XPATH, "//h3[@data-test ='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_first_name(self, first_name):
        self.set(self.first_name_field, first_name)

    def set_last_name(self, last_name):
        self.set(self.last_name_field, last_name)

    def set_postal_code(self, postal_code):
        self.set(self.postal_code_field, postal_code)

    def click_continue_button(self):
        self.click(self.continue_button)

    def get_checkout_title_text(self):
        return self.get_text(self.checkout_page_title)

    def get_error_message(self):
        return self.wait_element_get_text(self.error_message)



