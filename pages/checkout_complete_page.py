from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    HEADER_TEXT = (By.CLASS_NAME, "complete-header")

    def get_complete_header(self):
        return self.get_text(self.HEADER_TEXT)