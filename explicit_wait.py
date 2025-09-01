from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("C:/selenium_drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# ✅ Explicit Wait – ஒரு element மட்டும் load ஆகும்வரை காத்திருக்கும்
wait = WebDriverWait(driver, 10)

# `my-text` ID உடைய textbox-ஐ load ஆகும் வரை selenium காத்திருக்கும்
textbox = wait.until(EC.presence_of_element_located((By.NAME, "my-textarea")))

# Text box இல் value enter செய்கிறது
textbox.send_keys("Vanakkam from Explicit Wait")

time.sleep(2)
driver.quit()
