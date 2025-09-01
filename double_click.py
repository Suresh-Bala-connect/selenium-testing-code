from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains

Service=Service("c://selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
time.sleep(2)

double_click=driver.find_element("xpath", "//button[text()='Double-Click Me To See Alert']")
actions=ActionChains(driver)
actions.double_click(double_click).perform()
print ("Double Clicked")
time.sleep(2)

alert=driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
time.sleep(2)
driver.quit()