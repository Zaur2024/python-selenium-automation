"""

from selenium.webdriver.common.by import By

#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from behave import given, when, then
from time import sleep


import CSS_selector
#from features.steps.target_main_page import driver

#driver.wait=WebDriverWait(driver, 10)



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


@then('Verify Get to know Target Circle')
def verify_get_to_know_circle(context):
    expected_text="Get to know Target Circle"
    actual_text=context.driver.find_element(By.ID,"j_id0:contentTemplate:j_id24:j_id25:j_id30").text
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


@when("Click on Find a card right for you")
def find_a_card_right(context):
    context.driver.find_element(By.XPATH, "//a[@href='/circlecard']").click()
    sleep(2)


@then("Verify circle card logo")
def circle_card_logo(context):
    expected_text='Get the most from your Target Circle™️ Card'
    actual_text=context.driver.find_element(By.CSS_SELECTOR, ".styles_ndsHeading__HcGpD.styles_fontSize2__8Iex_.styles_x2Margin__M5gHh").text
    assert expected_text in actual_text
    sleep(2)



@when("Search for lemon")
def search_for_lemon(context):
    context.driver.find_element(By.ID,"search").send_keys("lemon")
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='/p/lemon-each/-/A-15013629#lnk=sametab']"))).click()


@when("Add to card")
def add_to_card(context):
    #context.driver.find_element(By.CSS_SELECTOR, "[href='/p/lemon-each/-/A-15013629#lnk=sametab']").click()
    #sleep(2)
    context.driver.find_element(By.ID,"addToCartButtonOrTextIdFor15013629").click()
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR,"[href='/cart']").click()


# homework 5.1
@when("Search for lemon")
def search_for_lemon(context):
    context.driver.wait.until(EC.visibility_of_element_located((By.ID, "search"))).send_keys("lemon")
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"))).click()
    sleep(4)


@when("Add to card")
def add_to_card(context):
    #use this to remove the popup. Its better way.
    context.driver.wait.until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "heroImg"))
    )


    context.driver.wait.until(
        EC.element_to_be_clickable((By.ID, "addToCartButtonOrTextIdFor15013629"))
    ).click()

    context.driver.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-test='orderPickupButton']"))
    ).click()


    context.driver.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='/cart']"))
    ).click()


@then("Verify lemon in the card")
def verify_lemon(context):
    expected_text='Cart'
    actual_text=context.driver.find_element(By.ID, "cart-summary-heading").text
    assert expected_text in actual_text
    sleep(2)


@when("search for {product}")
def search_product(context,product):
    context.driver.find_element(By.ID,"search").send_keys(product)
    context.driver.find_element(By.XPATH,("//button[@data-test='@web/Search/SearchButton']")).click()


@then("Verify result for milk")
def result_for_milk(context):
    expected_text='milk'
    actual_result=context.driver.find_element(By.XPATH,("//div[@data-test='lp-resultsCount']")).text
    assert expected_text in actual_result
    sleep(2)


@then("Verify result for bread")
def result_for_bread(context):
    expected_text='bread'
    actual_result=context.driver.find_element(By.XPATH,("//div[@data-test='lp-resultsCount']")).text
    assert expected_text in actual_result
    sleep(2)



@then('Verify at least 10 benefit cells')
def verify_at_least(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    assert len(elements)>=10


"""