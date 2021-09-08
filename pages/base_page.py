"""
    Base class for all pages
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_URL(self, URL):
        self.driver.get(URL)

    def get_current_URL(self):
        self.wait.until(EC.url_changes)
        return self.driver.current_url
        
    def get_page_title(self):
        return self.driver.title

    def test_get_elements():
        pass
        return []

    def click_element(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    def press_Enter(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def fill_txt_field(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        
    def get_text():
        pass
        return ""