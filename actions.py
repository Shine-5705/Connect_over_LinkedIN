import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
def scroll_and_collect_profiles(driver, log_path="profile_links.log"):
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
from selenium.webdriver.common.action_chains import ActionChains


def visit_profiles_and_connect(driver, profile_links):
    for link in profile_links:
        try:
            driver.get(link)
            time.sleep(3)

            # Try direct connect button via JS
            js_direct_connect = """
            const connectBtn = [...document.querySelectorAll('button')].find(b => b.textContent.trim() === 'Connect');
            if (connectBtn) {
                connectBtn.click();
                setTimeout(() => {
                    const sendBtn = [...document.querySelectorAll('button')].find(b => b.textContent.trim() === 'Send without a note');
                    sendBtn?.click();
                }, 800);
                return true;
            }
            return false;
            """

            direct_clicked = driver.execute_script(js_direct_connect)
            if direct_clicked:
                print(f"✅ Connected directly on: {link}")
                time.sleep(2)
                continue

            # If direct connect not found, try More -> Connect -> Send without note via JS
            js_more_connect = """
            let success = false;
            document.querySelectorAll('button[id$="-profile-overflow-action"]').forEach(btn => {
              btn.click();
              setTimeout(() => {
                const connectBtn = Array.from(document.querySelectorAll('span.display-flex.t-normal.flex-1'))
                  .find(el => el.textContent.trim() === 'Connect');
                if(connectBtn){
                  connectBtn.click();
                  setTimeout(() => {
                    const sendWithoutNoteBtn = document.querySelector('button[aria-label="Send without a note"]');
                    sendWithoutNoteBtn?.click();
                  }, 1000);
                  success = true;
                }
              }, 500);
            });
            return success;
            """

            more_connect_clicked = driver.execute_script(js_more_connect)
            if more_connect_clicked:
                print(f"✅ Connected via More menu on: {link}")
            else:
                print(f"❌ Connect not found on: {link}")

            time.sleep(3)
        except Exception as e:
            print(f"⚠️ Error visiting {link}: {e}")
            time.sleep(2)
