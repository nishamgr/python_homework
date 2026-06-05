from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
import json

#create browser and launch
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#url of lib /opens the webpage
lib_url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(lib_url)

wait = WebDriverWait(driver, 15)
wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li"))
)
#find the link and print the first 50 
lis = driver.find_elements(By.TAG_NAME, "a")
print("li count:", len(lis))
for li in lis[:50]:
    text = li.text.strip()
    if text:
        print(text)
     
print("cp-search-result count:", 
      len(driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result")))

#get all the book results
li_elements = driver.find_elements(By.TAG_NAME, "li")
print("Found:", len(li_elements))

for e, li in enumerate(li_elements[:20]):
    print("\n-------- LI", e, "-------")
    print(li.get_attribute("outerHTML")[:500])

#empty list to store all scraped book data
source = driver.page_source
print("Contains 'Spanish'?", "Spanish" in source)

source = driver.page_source
#find search results 
books = driver.find_elements(
    By.CSS_SELECTOR, "li.cp-search-result-item"
)
#empty list
results = []
#loop thru eacah book result
for i, book in enumerate(books):

    try:
        #extracting the book title
        title_element = book.find_element(
            By.CSS_SELECTOR,
            "span.title-content"
        ).text.strip()

        print("FOUND TITLE:", title_element)
        #adding book title 
        results.append({
            "Title": title_element
        })

    except Exception as e:
        print("ERROR:", e)

        print(book.get_attribute("outerHTML")[:5000])
        break
        
        
print("Results:", len(results))
print(results[:3])

print(driver.title)
print(driver.current_url)

driver.quit()

#creating a df
df = pd.DataFrame(results)
print(df.head())

#write df to csv
df.to_csv("get_books.csv", index=False)

#write results list to JSON
with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
    
print("CSV and JSON files saved successfully.")