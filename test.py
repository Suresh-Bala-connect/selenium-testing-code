from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time
service = Service("C:/selenium_drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print(driver.title)

time.sleep(15)  # Hold browser open for 5 seconds

# # driver.quit()
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time

# service = Service("C:/selenium_drivers/chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
# time.sleep(2)

# # Locate input box by ID and type text
# input_box = driver.find_element("id", "user-message")
# input_box.send_keys("Hello, Suresh!")

# time.sleep(5)
# driver.quit()
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time

# service = Service("C:/selenium_drivers/chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# time.sleep(10)

# # Locate text input by ID
# text_input = driver.find_element("id", "my-text-id")
# text_input.send_keys("Vanakkam Suresh!")

# # Locate the Submit button and click
# submit_button = driver.find_element("css selector", "button")
# submit_button.click()

# time.sleep(10)
# driver.quit()
