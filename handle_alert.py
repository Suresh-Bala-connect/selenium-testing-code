from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
browser=webdriver.Chrome(service=Service)
browser.get("https://the-internet.herokuapp.com/javascript_alerts")
browser.maximize_window()
time.sleep(2)
alert_button=browser.find_element("xpath",'//*[@id="content"]/div/ul/li[1]/button')
alert_button.click()

alert=browser.switch_to.alert
print(alert.text)
alert.accept()