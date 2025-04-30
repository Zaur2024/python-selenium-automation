from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD=(By.ID,'search')
    SEARCH_BUTTON=(By.XPATH,"//button[@data-test='@web/Search/SearchButton']")
    #CART_ICON=(By.XPATH,"//a[@data-test='@web/CartLink']")

    def search_product(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(10)


    #def cart_page(self):
    #    self.click(*self.CART_ICON)

