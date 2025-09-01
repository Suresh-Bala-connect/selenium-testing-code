from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://the-internet.herokuapp.com/upload")

upload_input=driver.find_element("id","file-upload")
file_path=os.path.abspath("C:/Users/Admin/Desktop/Python/fun.py")
print("File path:", file_path) 
upload_input.send_keys(file_path)
time.sleep(3)
driver.find_element("id","file-submit").click()
time.sleep(3)
driver.quit()