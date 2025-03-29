from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#get the path to the ChromeDriver executable
#driver_path = ChromeDriverManager().install()


#create a new Chrome browser instance
#service = Service(driver_path)
#driver = webdriver.Chrome(service=service)
#driver.maximize_window()
#driver.implicitly_wait(4)
#driver.wait=WebDriverWait(driver, 10)


from behave import given, when, then


@given ('Open Target main page')
def target_main_page(context):
   context.driver.get("https://www.target.com/")


@when('Click on Target Circle link')
def click_on_target_circle(context):
    context.driver.find_element(By.ID,"utilityNav-circle").click()




