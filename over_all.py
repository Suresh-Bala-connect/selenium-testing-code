
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # By is Selector Select
from selenium.webdriver.support.ui import Select # Using drop Down Select
from selenium.webdriver.common.keys import Keys # Keyboard Events Like Ctl+A,C,V
from selenium.webdriver.common.action_chains import ActionChains # Action of UI this is need and use of Double click Button Hover
import os # Using File Uplaod
import time

# Setup ChromeDriver
service = Service("c:/selenium_drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open local HTML file
driver.get("file:///D:/AnjanaInfoTech/Python/test.html")
driver.maximize_window()
time.sleep(2)

# Example: Fill text field
driver.find_element(By.ID, "username").send_keys("Suresh")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("mypassword")
time.sleep(3)

# Example: Click a button
driver.find_element(By.XPATH, '//*[@id="loginForm"]/button').click()
time.sleep(3)

# Input Name
driver.find_element(By.XPATH,'//*[@id="registerForm"]/input[1]').send_keys("Suresh Bala")
time.sleep(2)

# Input Gmail
driver.find_element(By.XPATH,'//*[@id="registerForm"]/input[2]').send_keys("suresh@gmail.com")
time.sleep(2)

# Input Phone Number
driver.find_element(By.XPATH,'//*[@id="registerForm"]/input[3]').send_keys("0987654321")
time.sleep(2)

#Radio Button
driver.find_element("name","gender").click()
time.sleep(2)

#Radio Button
driver.find_element("xpath",'//*[@id="registerForm"]/input[5]').click()
time.sleep(2)

#Drop Down
drop_dowm=Select(driver.find_element("xpath",'//*[@id="registerForm"]/select'))
drop_dowm.select_by_visible_text("HR")
time.sleep(2)


#Screen Short
driver.save_screenshot("C:/Users/Admin/Desktop/form1.png")
time.sleep(2)

#File Upload
upload_input=driver.find_element("xpath",'//*[@id="resumeFile"]')
file_path=os.path.abspath("c:Users/Admin/Desktop/userpass.xlsx")
upload_input.send_keys(file_path)
time.sleep(2)

# Scrolling 
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(3)

#Check Box
check_box=driver.find_element("xpath",'//*[@id="registerForm"]/input[8]')
check_box.click()
time.sleep(2)

#Key Board Events

# First Sending Word in Input Box
send_word=driver.find_element("xpath",'//*[@id="registerForm"]/input[9]')
send_word.send_keys("WelCome Well Done")
time.sleep(2)

# Select All
send_word.send_keys(Keys.CONTROL,'a')
time.sleep(2)

# Select Copy
send_word.send_keys(Keys.CONTROL,'c')
time.sleep(2)

# Select Copy
send_word.send_keys(Keys.CONTROL,'x')
time.sleep(2)

# Select Paste
send_word.send_keys(Keys.CONTROL,'v')
time.sleep(2)

# Submit Button Click
button_click=driver.find_element("xpath",'//*[@id="registerForm"]/button')
button_click.click()
time.sleep(2)

#Alert Handle
alert=driver.switch_to.alert
print("Alert Text :", alert.text)
alert.accept()
time.sleep(3)

#Second Screen shot
driver.save_screenshot("C:/Users/Admin/Desktop/form2.png")
time.sleep(4)

# Drag and drop
source = driver.find_element("xpath",'//*[@id="draggable"]')
target = driver.find_element("xpath",'//*[@id="droppable"]')

actions=ActionChains(driver)
actions.drag_and_drop(source,target).perform()
time.sleep(5)

driver.quit()
