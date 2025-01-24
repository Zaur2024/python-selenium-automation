from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.target.com/")

driver.find_element(By.ID,"account-sign-in").click()
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

# Make sure sign in with password button is shown
driver.find_element(By.ID,"login")

driver.find_element(By.CSS_SELECTOR,"input#search").click()
sleep(5)