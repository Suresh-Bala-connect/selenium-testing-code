from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains

Service=Service("c://selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(2)

driver.switch_to.frame(0)

source=driver.find_element("id", "draggable")
target=driver.find_element("id", "droppable")

action=ActionChains(driver)
action.drag_and_drop(source,target).perform()
print("Drag and Drop")
time.sleep(2)
driver.quit()
