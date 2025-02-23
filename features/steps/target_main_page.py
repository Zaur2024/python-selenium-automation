from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from sample_script import driver

#driver.implicitly_wait(4)

#@given ('Open Target main page')
#def target_main_page(context):
 #   context.driver.get("https://www.target.com/")


@when('Click on Target Circle link')
def click_on_target_circle(context):
    context.driver.find_element(By.ID,"utilityNav-circle").click()




