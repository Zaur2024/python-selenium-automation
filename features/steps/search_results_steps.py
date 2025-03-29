from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.support import expected_conditions as EC


from behave import given, when, then
from time import sleep

COLOR_OPTIONS=(By.CSS_SELECTOR,"div[aria-label='Carousel'] li img")
SELECTED_COLOR=(By.CSS_SELECTOR,"[data-test='@web/VariationComponent'] div")


@given ('Open target product {product_id} page')
def open_target(content,product_id):
    content.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors=['Blue Tint','Denim Blue','Marine','Raven']
    actual_colors=[]

    colors=context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color',selected_color)

        selected_color=selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expedted {expected_colors} did not match {actual_colors}'

