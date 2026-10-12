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
        if first_name:
            self.send_keys(self.FIRST_NAME, first_name)
        if last_name:
            self.send_keys(self.LAST_NAME, last_name)
        if postal_code:
            self.send_keys(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)

    def click_finish(self):
        self.click(self.FINISH_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)