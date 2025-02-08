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
    context.driver.find_element(By.ID, "account-sign-in").click()
    sleep(3)

#@when('click Sign In')
#def click_sign_out(context):
#    context.driver.find_element(By.CSS_SELECTOR, ("[data-test='accountNav-signIn']")).click()
#    sleep(3)


@when('From right side navigation menu, click Sign In.')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('Verify Sign in form opened')
def verify_sign_in_form(context):
    expected_sign_in_text = 'Sign into your Target account'
    sleep(5)
    actual_sign_in_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_sign_in_text in actual_sign_in_text, f'Expected {expected_sign_in_text} to be in {actual_sign_in_text}'
    print('Test case passed')






