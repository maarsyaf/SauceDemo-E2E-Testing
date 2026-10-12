import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestCatalogCart(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def test_sort_products_low_to_high(self):
        self.inventory_page.sort_products_by_value("lohi")
        prices = self.inventory_page.get_all_product_prices()
        self.assertEqual(prices, sorted(prices), "Produk tidak terurut asc (Low to High)")

    def test_add_and_remove_item_cart(self):
        self.inventory_page.add_backpack()
        self.assertEqual(self.inventory_page.get_cart_badge_count(), "1")

        self.inventory_page.remove_backpack()
        self.assertFalse(self.inventory_page.is_cart_badge_present())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()