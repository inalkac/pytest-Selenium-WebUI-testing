'''
    As a user
    I want to be able to search repos by the keyword
    So that I can observe the search page with corresponding title and contain

    As a user
    I want to be able to search repos by the keyword
    So that I can observe the list of relevant repos 

    As a user
    I want to click on the first title in search result
    So that I can navigate to repository page
'''
import time
from pages.test_data.test_data import TestData
from pages.locators.locators import Locators
from pages.search_result import SearchPage

def test_open_searchpage(browser):
    page = SearchPage(browser)
    page.open_URL(f"{TestData.SEARCH_PAGE_URL}{TestData.SEARCH_KWD}")
    assert page.get_page_title() == TestData.SEARCHPAGE_TITLE
    assert len(page.get_result_elements_list(Locators.SEARCH_RESULT)) > 0
    assert page.get_element_attr(Locators.SEARCH_FIELD, "value") == TestData.SEARCH_KWD
    
def test_search_result_is_relevant(browser):
    page = SearchPage(browser)
    page.open_URL(f"{TestData.SEARCH_PAGE_URL}{TestData.SEARCH_KWD}")
    result_links, result_titles, result_descriptions = page.get_result_list(Locators.SEARCH_RESULT, Locators.SEARCH_RESULT_LINK, Locators.SEARCH_RESULT_DESCRIPTION)
    assert page.get_element_attr(Locators.SEARCH_FIELD, "value") == TestData.SEARCH_KWD
    for i in range(0, len(result_links)): 
        assert (TestData.SEARCH_KWD in result_titles[i]) or (TestData.SEARCH_KWD in result_descriptions[i])

def test_click_first_link(browser):
    page = SearchPage(browser)
    page.open_URL(f"{TestData.SEARCH_PAGE_URL}{TestData.SEARCH_KWD}")
    result_links, result_titles, result_descriptions = page.get_result_list(Locators.SEARCH_RESULT, Locators.SEARCH_RESULT_LINK, Locators.SEARCH_RESULT_DESCRIPTION)
    page.click_element(Locators.SEARCH_RESULT_LINK)
    assert page.get_current_URL() == result_links[0]