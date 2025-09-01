from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

download_path="C:/Users/Admin/Downloads"
chrome_options=Options()
chrome_options.add_experimental_option("prefs",{"download.default_directory":download_path})
Service=Service("C:/selenium_drivers/chromedriver.exe")
driver = webdriver.Chrome(service=Service, options=chrome_options)
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element("id","textbox").send_keys("Hello Auto Dwonload")
time.sleep(3)
driver.find_element("id", "createTxt").click()
time.sleep(3)
driver.find_element("id", "link-to-download").click()
time.sleep(3)
driver.quit()