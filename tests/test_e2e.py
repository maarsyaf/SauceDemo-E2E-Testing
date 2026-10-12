import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage

class TestE2ECheckout(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def test_complete_e2e_checkout_flow(self):
        """E2E Positive Flow: Login -> Select Product -> Cart -> Checkout -> Complete"""
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(self.driver)
        inventory_page.add_backpack()
        self.assertEqual(inventory_page.get_cart_badge_count(), "1")
        inventory_page.go_to_cart()

        cart_page = CartPage(self.driver)
        self.assertEqual(cart_page.get_item_name(), "Sauce Labs Backpack")
        cart_page.click_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_information("John", "Doe", "12345")
        checkout_page.click_finish()

        complete_page = CheckoutCompletePage(self.driver)
        self.assertEqual(complete_page.get_complete_header().lower(), "thank you for your order!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()