from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains

Service=Service("c://selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
time.sleep(2)

right_click=driver.find_element("xpath", "//span[text()='right click me']")
actions=ActionChains(driver)
actions.context_click(right_click).perform()
print("Right Clicked")
time.sleep(2)
driver.quit()