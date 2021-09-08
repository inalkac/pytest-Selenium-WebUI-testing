"""
    As a user  
    I want to enter homepage URL to the browser
    to open and observe the home page

    As a user  
    I want to click SignUp button on the homepage 
    to start the signup process

    As a user
    I want to click SignIn button on the homepage
    to start the signin process
    
    As a user
    I want to enter search keyword on the homepage
    to search for repos and browse search result
"""
from pages.home import HomePage
from pages.test_data.test_data import TestData
from pages.locators.locators import Locators


def test_open_homepage(browser):
    page = HomePage(browser)
    page.open_URL(TestData.URL)
    assert page.get_page_title() == TestData.HOMEPAGE_TITLE

def test_start_signup(browser):
    page = HomePage(browser)
    page.open_URL(TestData.URL)
    page.signup_by_email(Locators.HOMEPAGE_EMAIL_TXTBOX, TestData.NEW_USER_EMAIL)
    url_for_assert = TestData.SIGNUP_PAGE_URL.replace("@","%40")
    assert page.get_current_URL() == url_for_assert

def test_start_signin(browser):
    page = HomePage(browser)
    page.open_URL(TestData.URL)
    page.start_signin_flow(Locators.LOGIN_LINK)
    assert page.get_current_URL() == f"{TestData.URL}/login"

def test_search(browser):
    page = HomePage(browser)
    page.open_URL(TestData.URL)
    page.search_by_keyword(Locators.SEARCH_TXTBOX, TestData.SEARCH_KWD)
    assert f"{TestData.SEARCH_PAGE_URL}{TestData.SEARCH_KWD}" in page.get_current_URL()