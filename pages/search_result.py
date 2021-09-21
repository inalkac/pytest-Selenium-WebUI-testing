"""
    SearchPage class. Inherited from the BasePage class
"""
from pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_result_elements_list(self, locator):
        result = self.get_elements(locator)
        return result

    def get_result_list(self, list_locator, link_locator, description_locator):
        result_list = self.get_elements(list_locator)
        titles = []
        descriptions = []
        links = []
        for i in range(0, len(result_list)):
            titles.append(self.get_element_text(link_locator))
            descriptions.append(self.get_element_text(description_locator))
            links.append(self.get_element_attr(link_locator, "href"))
        return links, titles, descriptions
    