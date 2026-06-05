from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
#download and config the ChromeDriver/ opens the 10 proj page
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/Top10/2025/")
#wait for the page to loead
wait = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.TAG_NAME, "a")))

items = driver.find_elements(By.TAG_NAME, "a")
#empty list to store 
owasp_data=[]
for item in items:
    try:
        text = item.text.strip()
        href = item.get_attribute("href")
        if text.startswith("A0") or text.startswith("A10"):
            print(text)
            
            owasp_data.append({
                "title": text,
                "href": href
            })
        
    except Exception as e:
        print("Skipped element:", e)
        
driver.quit()

print(owasp_data)
print(len(owasp_data))

pd.DataFrame(owasp_data).to_csv("owasp_top_10.csv", index=False)