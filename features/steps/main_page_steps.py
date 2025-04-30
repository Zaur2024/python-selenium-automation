from selenium.webdriver.common.by import By
from behave import given, when, then



@given ('Open Target main page')
def open_main(context):
   context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()


@then('Verify search results for {product}')
def verify_search_results(content,product):
    content.app.search.verify_search_results()


@when('click on cart icon')
def cart_page(context):
    context.app.cart.cart_page()


@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    context.app.cart.verify_cart()
