from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains

Service=Service("c://selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
time.sleep(2)

hover_element=driver.find_element("xpath", "//button[text()='Double-Click Me To See Alert']")
actions=ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)
print("Hover Ovr the Button")
time.sleep(2)
driver.quit()