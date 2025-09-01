from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
time.sleep(2)

driver.find_element("id","tool-1").click()
time.sleep(2)
driver.find_element("id","profession-1").click()
time.sleep(2)