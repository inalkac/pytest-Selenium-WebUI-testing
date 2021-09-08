"""
    Homepage class. Inherited from the BasePage class
"""
from pages.base_page import BasePage
import time
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def signup_by_email(self, locator, email):
        #enter email in text field and press Enter
        self.fill_txt_field(locator, email)
        self.press_Enter(locator)

    def start_signin_flow(self, locator):
        #click Sign In on the homepage
        self.click_element(locator)

    def search_by_keyword(self, locator,text):
        #search for keyword and open search result page
        self.fill_txt_field(locator, text)
        self.press_Enter(locator)
