from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)

driver.get("https://www.w3schools.com/")
driver.maximize_window()
time.sleep(2)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)
driver.quit()