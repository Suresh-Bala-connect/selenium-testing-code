from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:/selenium_drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
time.sleep(2)


first_name = driver.find_element("name", "firstname")
first_name.send_keys("Suresh")
time.sleep(3)
print("First Name")

# ✅ Last Name
first_name.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys("Bala")
time.sleep(3)
print("Last Name")

# ✅ Gender: Female
first_name.send_keys(Keys.TAB)   # Move to Female radio
driver.switch_to.active_element.send_keys(Keys.ARROW_RIGHT)  # Move from Male to Female
driver.switch_to.active_element.send_keys(Keys.SPACE)
time.sleep(3)
print("Gender")

# ✅ Experience: 5 years
driver.switch_to.active_element.send_keys(Keys.TAB)  # Go to Exp 1 year
driver.switch_to.active_element.send_keys(Keys.TAB)  # Go to Exp 2 years
driver.switch_to.active_element.send_keys(Keys.TAB)  # Go to Exp 3 years
driver.switch_to.active_element.send_keys(Keys.TAB)  # Go to Exp 4 years
driver.switch_to.active_element.send_keys(Keys.TAB)  # Go to Exp 5 years
driver.switch_to.active_element.send_keys(Keys.SPACE)
time.sleep(3)
print("Experience")

# ✅ Date
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys("11/08/2025")
time.sleep(3)
print("Date")

# ✅ Profession checkbox
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys(Keys.SPACE)
time.sleep(3)
print("Experience")

# ✅ Automation Tool checkbox
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys(Keys.SPACE)
time.sleep(3)
print("Automation Keys")

# ✅ Submit
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()
