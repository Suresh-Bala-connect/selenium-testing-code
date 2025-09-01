from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)

driver.get("https://www.amazon.com/s?k=laptops")
driver.maximize_window()
time.sleep(2)

last_height=driver.execute_script("return document.body.scrollHeight")

while True:
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    
    new_height=driver.execute_script("return document.body.scrollHeight")
    
    if new_height==last_height:
        break
    last_height=new_height
    print("Infinite Scroll Completed")
    driver.quit()