from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from login_page import LoginPage
import time

service = Service("C:/selenium_drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

login_page = LoginPage(driver)
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login()

time.sleep(3)
driver.quit()
