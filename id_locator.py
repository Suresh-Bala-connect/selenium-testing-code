from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service=Service("C:/selenium_drivers/chromedriver.exe")


driver=webdriver.Chrome(service=service)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
time.sleep(2)

# ID Locator
text_input=driver.find_element("id","my-text-id")
text_input.send_keys("Hello Suresh")
time.sleep(2)
# NAME Locator
text_pass=driver.find_element("name","my-password")
text_pass.send_keys("Password")
time.sleep(3)
#XPATH Locator
text_area=driver.find_element("xpath",'/html/body/main/div/form/div/div[1]/label[3]/textarea')
text_area.send_keys("Good Well Done. Keep It. Go Forward")
time.sleep(3)
#CSS Selector
button=driver.find_element("css selector","button")
button.click()
time.sleep(3)