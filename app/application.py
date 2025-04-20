from pages.base_page import BasePage
from pages.header import Header
from pages.main import MainPage
from pages.search_results_page import SearchResultsPage







class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page=BasePage(driver)
        self.header=Header(driver)
        self.search=SearchResultsPage(driver)
        self.main_page=MainPage(driver)
        



