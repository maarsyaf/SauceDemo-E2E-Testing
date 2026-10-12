# pages/checkout_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def fill_information(self, first_name="", last_name="", postal_code=""):
        # Bersihkan dan isi First Name
        fn_field = self.find(self.FIRST_NAME)
        fn_field.clear()
        if first_name:
            fn_field.send_keys(first_name)

        # Bersihkan dan isi Last Name
        ln_field = self.find(self.LAST_NAME)
        ln_field.clear()
        if last_name:
            ln_field.send_keys(last_name)

        # Bersihkan dan isi Postal Code
        pc_field = self.find(self.POSTAL_CODE)
        pc_field.clear()
        if postal_code:
            pc_field.send_keys(postal_code)

        self.click(self.CONTINUE_BTN)

    def click_finish(self):
        self.click(self.FINISH_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)