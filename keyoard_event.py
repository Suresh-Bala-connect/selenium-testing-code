from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

Service=Service("c://selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)

driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)

search_box=driver.find_element("name","q")
time.sleep(2)
print("What Done")

search_box.send_keys("Hello Python")
time.sleep(2)
print("Send Keys")

# Select all (Ctrl + A)
search_box.send_keys(Keys.CONTROL,'a')
time.sleep(2)
print("Ctrl + A")

#  Copy (Ctrl + C)
search_box.send_keys(Keys.CONTROL,'c')
time.sleep(2)
print("Ctrl + C")

# Clear box and paste (Ctrl + V)
search_box.send_keys(Keys.CONTROL,'v')
time.sleep(2)
print("Ctrl + V")

search_box.send_keys(Keys.ENTER)
print("Ctrl + V")

time.sleep(3)
driver.quit()
