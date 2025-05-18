# search_fill.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def fill_search_bar(driver, query):
    try:
        driver.get("https://www.linkedin.com/feed/")
        time.sleep(5)

        search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
        search_input.clear()
        search_input.send_keys(query)
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)
        print(f"🔍 Searched for: {query}")
    except Exception as e:
        print("❌ Error filling search bar:", e)
