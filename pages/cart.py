from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Cart(BasePage):
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")


    def cart_page(self):
        self.click(*self.CART_ICON)


    def verify_cart(self):
        actual_result = self.click(*self.CART_ICON)

