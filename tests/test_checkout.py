# tests/test_checkout.py
import json
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckout(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        inventory = InventoryPage(self.driver)
        inventory.add_backpack()
        inventory.go_to_cart()
        
        cart = CartPage(self.driver)
        cart.click_checkout()
        
        self.checkout_page = CheckoutPage(self.driver)

    def test_checkout_form_ddt(self):
        with open("data/checkout_data.json", "r") as f:
            test_data = json.load(f)

        for data in test_data:
            with self.subTest(scenario=data["scenario"]):
                # Kembalikan ke URL Checkout Step One sebelum tes dijalankan
                self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
                self.checkout_page.fill_information(
                    data["first_name"],
                    data["last_name"],
                    data["postal_code"]
                )
                self.assertEqual(self.checkout_page.get_error_message(), data["expected_error"])

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()