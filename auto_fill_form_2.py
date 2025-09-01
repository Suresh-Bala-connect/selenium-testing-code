from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:/selenium_drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
time.sleep(2)

# First Name
first_name = driver.find_element("name", "firstname")
first_name.send_keys("Suresh")
time.sleep(2)

# Last Name
last_name = driver.find_element("name", "lastname")
last_name.send_keys("Bala")
time.sleep(2)

# Gender: Female
female_radio = driver.find_element("id", "sex-1")
female_radio.send_keys(Keys.SPACE)
time.sleep(2)

# Experience: 5 years
exp_5_radio = driver.find_element("id", "exp-4")
exp_5_radio.send_keys(Keys.SPACE)
time.sleep(2)

# Date
date_field = driver.find_element("id", "datepicker")
date_field.send_keys("11/08/2025")
time.sleep(2)

# Profession: Manual Tester
manual_checkbox = driver.find_element("id", "profession-0")
manual_checkbox.send_keys(Keys.SPACE)
time.sleep(2)

# Automation Tool: Selenium Webdriver
selenium_checkbox = driver.find_element("id", "tool-2")
selenium_checkbox.send_keys(Keys.SPACE)
time.sleep(2)

# Submit
submit_button = driver.find_element("id", "submit")
submit_button.send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()
