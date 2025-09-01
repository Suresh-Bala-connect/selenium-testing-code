from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
browser=webdriver.Chrome(service=Service)


browser.implicitly_wait(15)

browser.get("https://www.selenium.dev/selenium/web/web-form.html")

text_input=browser.find_element("name","my-textara")
text_input.send_keys("Vanakam Mr. Suresh")

time.sleep(3)
browser.quit()