import time
import os
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

def scroll_and_collect_profiles(driver, log_path="profile_links.log"):
    # Ensure a fresh log file each time
    if os.path.exists(log_path):
        os.remove(log_path)
    profile_links = set()
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        time.sleep(2)
        cards = driver.find_elements(By.XPATH, "//a[contains(@href, '/in/') and @data-test-app-aware-link]")
        for card in cards:
            href = card.get_attribute("href")
            if href and "/in/" in href:
                profile_links.add(href)
        
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    with open(log_path, "w", encoding="utf-8") as f:
        for link in profile_links:
            f.write(link + "\n")
    print(f"✅ Collected {len(profile_links)} profile links.")

    return list(profile_links)

def visit_profiles_and_connect(driver, profile_links):
    for link in profile_links:
        try:
            driver.get(link)
            time.sleep(3)

            try:
                connect_btn = driver.find_element(By.XPATH, "//button[contains(., 'Connect')]")
                connect_btn.click()
                time.sleep(1)
                print(f"✅ Connected via direct button: {link}")
                continue
            except NoSuchElementException:
                pass

            try:
                more_btn = driver.find_element(By.XPATH, "//button[contains(., 'More')]")
                more_btn.click()
                time.sleep(1)
                connect_in_menu = driver.find_element(By.XPATH, "//span[text()='Connect']/ancestor::button")
                connect_in_menu.click()
                print(f"✅ Connected via More menu: {link}")
            except NoSuchElementException:
                print(f"❌ Connect not found on: {link}")
            except ElementClickInterceptedException:
                print(f"⚠️ Could not click Connect for: {link}")

        except Exception as e:
            print(f"⚠️ Error visiting {link}: {e}")
        time.sleep(2)
