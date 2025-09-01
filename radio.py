from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Service=Service("C:/selenium_drivers/chromedriver.exe")
# driver=webdriver.Chrome(Service=Service)
Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()

input=driver.find_element("name","firstname")
input.send_keys("Suresh")
time.sleep(2)
input_01=driver.find_element("name","lastname")
input_01.send_keys("Bala")
time.sleep(2)
# driver.find_element("name", "firstname").send_keys("Suresh")
# driver.find_element("name", "lastname").send_keys("Bala")

driver.find_element("id","sex-0").click()
time.sleep(2)
driver.find_element("id","exp-1").click()
time.sleep(2)