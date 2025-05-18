import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

LOG_FILE = "profile_links.log"

def scroll_and_collect_links(driver, scroll_pause=2, max_scrolls=10):
    profile_links = set()
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    for _ in range(max_scrolls):
        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        
        # Collect profile links visible on page
        profiles = driver.find_elements(By.CSS_SELECTOR, "a.app-aware-link[data-control-name='search_srp_result']")
        for profile in profiles:
            link = profile.get_attribute("href")
            if link and "linkedin.com/in/" in link:
                profile_links.add(link.split('?')[0])  # Clean URL (remove query params)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # No more scroll
        last_height = new_height

    # Save links to log file
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        for link in profile_links:
            f.write(link + "\n")
    print(f"Collected {len(profile_links)} profiles and saved to {LOG_FILE}")
    return list(profile_links)

def connect_to_profiles(driver, links):
    for link in links:
        try:
            driver.get(link)
            time.sleep(3)
            
            # Click "More" button if present
            try:
                more_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='More actions']")
                more_button.click()
                time.sleep(2)
            except NoSuchElementException:
                print("More button not found on profile:", link)
            
            # Click "Connect" if present in dropdown or visible button
            try:
                connect_button = driver.find_element(By.XPATH, "//button[contains(., 'Connect')]")
                connect_button.click()
                time.sleep(2)
                
                # If there's a send now or add note popup, handle it
                try:
                    send_button = driver.find_element(By.XPATH, "//button[contains(., 'Send now')]")
                    send_button.click()
                    time.sleep(2)
                    print(f"Sent connection request to {link}")
                except NoSuchElementException:
                    # If no send button, just close popup or move on
                    print(f"Clicked Connect on {link}, but no send confirmation needed.")
                
            except NoSuchElementException:
                print(f"Connect button not found on profile: {link}")
                
        except Exception as e:
            print(f"Error processing profile {link}: {e}")
