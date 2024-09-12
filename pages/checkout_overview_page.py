from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    # checkout_overview_page locators
    finish_button = (By.ID,"finish")
    checkout_overview_title_text = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        super().__init__(driver)

    def get_payment_information(self):
        return self.get_checkout_text(2)

    def get_shipping_information(self):
        return self.get_checkout_text(4)

    def items_total_price(self):
        price_text = self.get_checkout_text(6)  # Get the price text
        # Extract the price part (after the colon) and remove any extra spaces
        price_without_label = price_text.split(':')[-1].strip()

        # Remove the '$' symbol
        price_without_dollar = price_without_label.replace('$', '')

        # Convert to float first, then to int
        total_price = float(price_without_dollar)
        return total_price

    def get_total_with_tax(self):
        price_text = self.get_checkout_text(8)
        price_without_label = price_text.split(':')[-1].strip()
        price_without_dollar = price_without_label.replace('$', '')
        total_price = float(price_without_dollar)
        return total_price

    def get_total_price_cart_list(self):
        total_cart_price = 0  # Initialize total price

        # Loop over the item numbers you want (in this case, 1 and 2)
        for item_number in range(2, 4):
            price_element = self.get_item_price_text(item_number)  # Get the price for each item
            price = float(price_element.text.replace('$', ''))  # Convert the price to float after removing '$'
            total_cart_price += price  # Add the price to the total

        return total_cart_price  # Return the total price

    def finish_button_click(self):
        self.click(self.finish_button)

    def get_title_text(self):
        return self.get_text(self.checkout_overview_title_text)
