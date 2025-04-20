from selenium.webdriver.common.by import By


def verify_cart(self):
    actual_result=self.click(*self.CART_ICON)
