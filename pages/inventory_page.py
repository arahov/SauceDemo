from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    sort_lower_price = (By.XPATH, "//div[@class='right_component']//select["
                                  "@class='product_sort_container']//following-sibling::option[2]")
    shop_cart_button = (By.CLASS_NAME, "shopping_cart_badge")
    title_text = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        super().__init__(driver)

    def click_set_filter_lower_to_higher(self):
        self.click(self.sort_lower_price)

    def click_add_item_to_cart_button(self):
        # by the 2 lowest price items
        for item_number in range(1, 3):
            self.click_add_remove_to_cart("add_item", item_number)

    def click_remove_item_from_cart_button(self):
        self.click_add_remove_to_cart("remove_item", 1)

    def click_shop_cart_button(self):
        self.click(self.shop_cart_button)

    def get_shop_cart_number_of_items_text(self):
        return self.get_text(self.shop_cart_button)

    def get_title_text(self):
        return self.get_text(self.title_text)