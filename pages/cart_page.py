from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK_BTN = (By.ID, "remove-sauce-labs-backpack")

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def get_item_name(self):
        return self.get_text(self.ITEM_NAME)

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BTN)

    def get_cart_items_count(self):
        return len(self.find_all(self.ITEM_NAME))