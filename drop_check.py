
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select # For Dropdown Use #
import time
service=Service("C:/selenium_drivers/chromedriver.exe")

browser=webdriver.Chrome(service=service)
browser.get("https://www.selenium.dev/selenium/web/web-form.html")
browser.maximize_window()
time.sleep(3)
#1. Text Box with Name
text_area=browser.find_element("name","my-textarea")
text_area.send_keys("Vanakkam Suresh")
time.sleep(3)
# Select Dropdown Value
drop_down=Select(browser.find_element("name","my-select"))
drop_down.select_by_visible_text("Two")
time.sleep(3)
#click Submit Button
submit_button=browser.find_element("css selector", "button")
submit_button.click()
time.sleep(4)

