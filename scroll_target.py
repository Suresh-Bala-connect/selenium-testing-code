from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup ChromeDriver
service = Service("C:/selenium_drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open webpage
driver.get("https://www.w3schools.com/")
driver.maximize_window()
time.sleep(2)

# Find element (e.g., footer link)
element = driver.find_element(By.LINK_TEXT, "Privacy Policy")

# Scroll to the element
driver.execute_script("arguments[0].scrollIntoView();", element)

# Wait to see the result
time.sleep(3)
driver.quit()