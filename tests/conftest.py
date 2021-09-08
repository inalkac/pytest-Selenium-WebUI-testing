"""
    fixtures used in test cases
"""
import pytest
from pages.webdriver_setup import WebdriverSetup
from pages.home import HomePage

@pytest.fixture
def browser():
    driver_setup = WebdriverSetup()
    driver = driver_setup.getDriver()
    yield driver
    driver.quit()
