from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()
time.sleep(2)

# driver.find_element("xpath",'//*[@id="content"]/div/ul/li[1]/button').click()
alert_button=driver.find_element("xpath", '//*[@id="content"]/div/ul/li[2]/button')
alert_button.click()
time.sleep(2)

alert=driver.switch_to.alert
print("Alert Text :", alert.text)
time.sleep(3)
alert.dismiss()
time.sleep(2)