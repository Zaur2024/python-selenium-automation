#from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from time import sleep

# get the path to the ChromeDriver executable
#driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
#service = Service(driver_path)
#driver = webdriver.Chrome(service=service)
#driver.maximize_window()
#driver.get("https://www.amazoon.com/")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36")
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com")


#Hello,sign in Account and List page
driver.find_element(By.ID,"nav-link-accountList").click()
sleep(3)
#Create your Amazon account
driver.find_element(By.CSS_SELECTOR,'a.a-button-text').click()

# Amazon logo
#driver.find_element(By.CSS_SELECTOR,"i.a-icon.a-icon-logo").click()

# Create account text
#expected_result="Create account"
#actual_result=driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small").text
#assert expected_result in actual_result


# Your name field
#driver.find_element(By.CSS_SELECTOR,"[name='customerName']")

# Mobile number or email field
#driver.find_element(By.CSS_SELECTOR,"input[type='email']")


# Passwords must be at least 6 characters. text
#expected_result="Passwords must be at least 6 characters."
#actual_result=driver.find_element(By.ID,"auth-password-requirement-info").text
#assert expected_result in actual_result


# Re-enter password field
#driver.find_element(By.ID,"ap_password_check")

# Continue button
#driver.find_element(By.CSS_SELECTOR,"input.a-button-input")

#Conditions of Use link
#driver.find_element(By.CSS_SELECTOR,"a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#Privacy Notice link
#driver.find_element(By.CSS_SELECTOR,"a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#Sign in link
driver.find_element(By.CSS_SELECTOR,"a.a-link-emphasis").click()
