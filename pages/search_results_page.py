from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
        #SEARCH_RESULTS=(By.XPATH, "//div[data-test='resultsHeading']")
        SEARCH_RESULTS=(By.XPATH, "//div[@data-test='lp-resultsCount']//span[contains(text(), 'results')]")




#target sitede fergli idi 1 daha yoxlayarsan

        def verify_search_results(self):
            actual_result=self.find_element(*self.SEARCH_RESULTS).text
            #assert 'tea' in actual_result, f"Expected text tea not in actual {actual_result}"

