from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)

driver.get("https://www.google.com")
print("Hello Suresh")
time.sleep(5)

driver.get("https://www.selenium.dev")
print("Visited Selenium")
time.sleep(2)

driver.back()
print("Back To Google")
time.sleep(5)

driver.forward()
print("Selenium")
time.sleep(5)

driver.refresh()
print("PAge Refresh")
time.sleep(5)