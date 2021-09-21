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
    SEARCH_RESULT = (By.XPATH, "//ul[@class = 'repo-list']/li")
    SEARCH_RESULT_DESCRIPTION = (By.XPATH, "//p[@class = 'mb-1']")
    SEARCH_RESULT_LINK = (By.XPATH, "//li[contains(@class, 'repo-list-item')]/div[2]/div/div/a")
    SEARCH_FIELD = (By.NAME, "q")
    