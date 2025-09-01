from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)

driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)

driver.save_screenshot("C:/Users/Admin/Desktop/google_home.png")
print("Saved")

driver.quit()