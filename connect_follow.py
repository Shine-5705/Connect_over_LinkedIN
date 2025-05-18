import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

def scroll_and_click_buttons(driver, scroll_times=5):
    print("⏬ Scrolling and attempting to click 'Connect' or 'Follow' buttons...")

    for _ in range(scroll_times):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(2)

    buttons = driver.find_elements(By.XPATH, "//button[span[text()='Connect'] or span[text()='Follow']]")
    print(f"🔘 Found {len(buttons)} buttons")

    for btn in buttons:
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            time.sleep(0.5)
            btn.click()
            print(f"👉 Clicked: {btn.text}")
            time.sleep(1)
        except ElementClickInterceptedException:
            print("⚠️ Button not clickable (possibly already handled)")
        except Exception as e:
            print("❌ Error clicking button:", e)
