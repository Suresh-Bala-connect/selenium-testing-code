from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element("link text","Click Here").click()
windows = driver.window_handles

driver.switch_to.window(windows[1])
print("New Tab Title:", driver.title)
time.sleep(2)

driver.switch_to.window(windows[0])
print("Back to Orginal title :", driver.title)

time.sleep(2)
driver.quit()