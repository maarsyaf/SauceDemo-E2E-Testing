from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BTN = (By.ID, "remove-sauce-labs-backpack")
    ADD_BIKE_LIGHT_BTN = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def sort_products_by_value(self, option_value):
        select_elem = Select(self.find(self.SORT_DROPDOWN))
        select_elem.select_by_value(option_value)

    def get_all_product_prices(self):
        elements = self.find_all(self.PRODUCT_PRICES)
        return [float(elem.text.replace("$", "")) for elem in elements]

    def add_backpack(self):
        self.click(self.ADD_BACKPACK_BTN)

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BTN)

    def add_bike_light(self):
        self.click(self.ADD_BIKE_LIGHT_BTN)

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def is_cart_badge_present(self):
        return self.is_element_present(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.CART_LINK)