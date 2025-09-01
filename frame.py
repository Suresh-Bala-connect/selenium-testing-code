from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")
time.sleep(3)

text_box=driver.find_element("id","tinymce")
text_box.clear()
time.sleep(3)

text_box.send_keys("Hello Suresh")
driver.switch_to.default_content()

time.sleep(3)
driver.quit()
