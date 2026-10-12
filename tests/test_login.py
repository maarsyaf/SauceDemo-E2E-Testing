import json
import unittest
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.login_page = LoginPage(self.driver)

    def test_login_ddt(self):
        with open("data/login_data.json", "r") as f:
            test_data = json.load(f)

        for data in test_data:
            with self.subTest(scenario=data["scenario"]):
                self.login_page.open()
                self.login_page.login(data["username"], data["password"])

                if data["is_valid"]:
                    self.assertIn(data["expected_url"], self.login_page.get_current_url())
                else:
                    self.assertEqual(self.login_page.get_error_message(), data["expected_error"])

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()