import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestEdgeCases(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def test_direct_url_access_without_login(self):
        """Edge Case: Akses URL Internal Langsung Tanpa Session Login"""
        self.driver.get("https://www.saucedemo.com/inventory.html")
        login_page = LoginPage(self.driver)
        error_msg = login_page.get_error_message()
        self.assertIn("You can only access '/inventory.html' when you are logged in", error_msg)

    def test_performance_glitch_user_login(self):
        """Edge Case: Menangani Delays Halaman dengan Performance Glitch User via Explicit Wait"""
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("performance_glitch_user", "secret_sauce")
        
        inventory_page = InventoryPage(self.driver)
        self.assertIn("inventory.html", inventory_page.get_current_url())

    def test_cart_badge_sync_between_pages(self):
        """Edge Case: Sinkronisasi Cart Badge Saat Item Dihapus dari Halaman Cart"""
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(self.driver)
        inventory_page.add_backpack()
        inventory_page.add_bike_light()
        self.assertEqual(inventory_page.get_cart_badge_count(), "2")

        inventory_page.go_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.remove_backpack()
        self.assertEqual(inventory_page.get_cart_badge_count(), "1")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()