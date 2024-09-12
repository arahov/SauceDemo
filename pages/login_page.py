from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    # login page locators
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_text = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username):
        self.set(self.username_field, username)

    def set_password(self, password):
        self.set(self.password_field, password)

    def click_login_button(self):
        self.click(self.login_button)

    def error_text_displayed(self):
        return self.wait_element_get_text(self.error_text,10)
