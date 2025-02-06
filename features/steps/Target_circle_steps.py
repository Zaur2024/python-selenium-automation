from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#@given ('Open Target main page')
#def target_main_page(context):
#    context.driver.get("https://www.target.com/")


@when('Click on Target Circle link')
def click_on_target_circle(context):
    context.driver.find_element(By.ID,"utilityNav-circle").click()


@when('Click on Join Target Circle')
def click_on_join_circle(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-lnk='Join Circle ']").click()
    sleep(2)


@then('Sign into your Target account')
def verify_sign_in(context):
    expected_text ='Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize2__8Iex_").text
    assert expected_text in actual_text
    sleep(3)