"""
    Base class for all pages
"""
from selenium.common.exceptions import ErrorInResponseException
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

    def get_elements(self, by_locator):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        except:
            elements = []
        return elements
    def get_element(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def get_element_attr(self, by_locator, attr):
        return self.wait.until(EC.presence_of_element_located(by_locator)).get_attribute(attr)

    def get_element_text(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator)).text

    def click_element(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def press_Enter(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def fill_txt_field(self, by_locator, text):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def get_css_selector_text(self, headlink, selector):
        selector_text = headlink.find_element_by_css_selector(selector).text
        return selector_text
