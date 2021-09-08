"""
    web elements locators
"""
from selenium.webdriver.common.by import By

class Locators:
    #Homepage locators
    HOMEPAGE_EMAIL_TXTBOX = (By.ID, "user_email")
    LOGIN_LINK = (By.XPATH, "//a[@href = '/login']")
    SEARCH_TXTBOX = (By.XPATH, "//input[@data-test-selector = 'nav-search-input']")

    #Search page locators
    