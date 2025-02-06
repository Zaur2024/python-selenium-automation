from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open target main page')
def open_target_main_page(context):
    context.driver.get("https://www.target.com/")


@when('click card icon')
def click_card(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']").text
    assert expected_text in actual_text
    sleep(3)




@when ('click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.ID,("account-sign-in")).click()


@when('click Sign In')
def click_sign_out(context):
    context.driver.find_element(By.CSS_SELECTOR, ("[data-test='accountNav-signIn']")).click()
