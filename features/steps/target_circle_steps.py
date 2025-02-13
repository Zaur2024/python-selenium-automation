from selenium.webdriver.common.by import By

from behave import given, when, then
from time import sleep

import CSS_selector




@when('Click on Join Target Circle')
def click_on_join_circle(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-lnk='Join Circle ']").click()
    sleep(2)


@then('Verify Sign into your Target account page shown')
def verify_sign_in(context):
    expected_text ='Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize2__8Iex_").text
    assert expected_text in actual_text
    sleep(3)


@when("Click on See today's Target Circle deals")
def see_today_s_target_circle_deals(context):
    context.driver.find_element(By.CSS_SELECTOR,"a[data-lnk='Circle Deals ']").click()
    sleep(2)


@then("Verify see today's Target Circle deals")
def click_on_see_today_s_target_circle_deals(context):
    expected_text ='Target Circle™ Deals'
    actual_text=context.driver.find_element(By.CSS_SELECTOR,"div[data-test='@web/Circle/PageTitle']").text
    assert expected_text in actual_text


@when("Click on Target Circle Bonuses")
def click_on_target_circle_bonuses(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-lnk='Bonus']").click()
    sleep(2)


@then("Verify Target Circle Bonuses page")
def verify_target_circle_bonuses_page(context):
    expected_text ='Target Circle™ Bonus'
    actual_text=context.driver.find_element(By.CSS_SELECTOR,".styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt.styles_x2Margin__M5gHh").text
    assert expected_text in actual_text
    sleep(3)


@when("Click on Target Circle Partners")
def click_on_target_circle_partners(context):
    context.driver.find_element(By.CSS_SELECTOR,"a[data-lnk='Partner']").click()


@then("Verify Target Circle Partners page")
def verify_target_circle_partner_page(context):
    expected_text='Target Circle™ Partners'
    actual_text=context.driver.find_element(By.CSS_SELECTOR,"div[data-test='@web/Circle/PageTitle']").text
    assert expected_text in actual_text


@when("Click on Community support votes")
def click_on_community_support_votes(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-lnk='Voting ']").click()
    sleep(2)


@then("Verify Sign into your Target account page")
def verify_sign_into_your_target_account_page(context):
    expected_text='Sign into your Target account'
    actual_text=context.driver.find_element(By.CSS_SELECTOR, "h1.styles_ndsHeading__HcGpD.styles_fontSize2__8Iex_").text
    assert expected_text in actual_text


@when("Click on Frequently asked questions")
def click_on_frequently_asked_questions(context):
    context.driver.find_element(By.CSS_SELECTOR,"a[href='https://help.target.com/help/subcategoryarticle?childcat=About+Target+Circle%E2%84%A2+Card&parentcat=Target+Circle%E2%84%A2']").click()
    sleep(3)

#  I couldn't verify Get to know Target Circle page
@then("Verify Get to know Target Circle page")
def verify_frequently_asked_questions_page(context):
    expected_text='Get to know Target Circle™'
    actual_text=context.driver.find_element(By.CSS_SELECTOR, (".global-header")).text()
    assert expected_text in actual_text


@when("Click on Learn more about Target Circle 360")
def click_on_learn_more_circle360(context):
    context.driver.find_element(By.CSS_SELECTOR,"a[data-test='@web/slingshot-components/CellsComponent/Link']").click()
    sleep(3)

@then("Verify Target Circle™ 360 page")
def verify_target_circle360_page(context):
    expected_text='Target Circle™ 360'
    actual_text=context.driver.find_element(By.CSS_SELECTOR,"div[data-test='@web/Circle/PageTitle']").text
    assert expected_text in actual_text


@when("Click on Gift a membership")
def click_on_gift_membership(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/p/target-circle-360-8482-annual-membership-giftcard-99/-/A-92626136']").click()
    sleep(3)



@then("Verify One-Year Membership")
def verify_one_year_membership_gift_card(context):
    expected_text='Target Circle 360™ One-Year Membership GiftCard $99'
    actual_text=context.driver.find_element(By.ID, "pdp-product-title-id").text
    assert expected_text in actual_text


@when("Click on Save over 50% as a collage student")
def click_on_school_over50_50(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/l/target-circle-college-student-appreciation/-/N-6v01l']").click()
    sleep(3)



@then("Verify College Student Appreciation")
def college_student_appreciation(context):
    expected_text='Target Circle™ College Student Appreciation'
    actual_text=context.driver.find_element(By.CSS_SELECTOR,"div[data-test='@web/Circle/PageTitle']").text
    assert expected_text in actual_text
    sleep(3)


@when("Click on Save over 50% with government assistance")
def click_on_school_over50_50(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/l/target-circle-government-assistance-verification/-/N-xmii7']").click()
    sleep(2)


@then("Verify Target Circle™ Government Assistance Verification page")
def government_assistance(context):
    expected_text='Target Circle™ Government Assistance Verification'
    actual_text=context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/Circle/PageTitle']").text
    assert expected_text in actual_text



@when("Search for lemon")
def search_for_lemon(context):
    context.driver.find_element(By.ID,"search").send_keys("lemon")
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(10)


@when("Add to card")
def add_to_card(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/p/lemon-each/-/A-15013629#lnk=sametab']").click()
    sleep(2)
    context.driver.find_element(By.ID,"addToCartButtonOrTextIdFor15013629").click()
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR,"[href='/cart']").click()


@then("Verify lemon in the card")
def verify_lemon(context):
    expected_text='Cart'
    actual_text=context.driver.find_element(By.ID, "cart-summary-heading").text
    assert expected_text in actual_text
    sleep(2)













