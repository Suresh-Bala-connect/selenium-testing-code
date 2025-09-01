from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

Service=Service("C:/selenium_drivers/chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()
time.sleep(2)

rows=driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr')

for i, row in enumerate(rows):
    cols=row.find_elements(By.TAG_NAME, "td")
    if cols:
        print(f"ROW{i}", end="")
        for col in cols:
            print(col.text, end=" | ")
        print()
        
found = False
for row in rows:
    cols = row.find_elements("tag name", "td")
    for col in cols:
        if "Germany" in col.text:
            found = True
            print("✅ Germany found in table!")
            break
    if found:
        break

if not found:
    print("❌ Germany not found!")
    
print("Total Rows:", len(rows))
print("Total Columns:", len(rows[1].find_elements("tag name", "td")))

for row in rows[1:]:  # Skip header
    company = row.find_elements("tag name", "td")[0]
    print(company.text)


driver.quit()