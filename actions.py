import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


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


def visit_profiles_and_connect(driver, profile_links):
    for link in profile_links:
        try:
            driver.get(link)
            time.sleep(6)

            # Try direct Connect button first
            connected = driver.execute_script("""
                const connectBtn = [...document.querySelectorAll('button')]
                    .find(b => b.textContent.trim() === 'Connect');
                if (connectBtn) {
                    connectBtn.click();
                    return true;
                }
                return false;
            """)

            if connected:
                time.sleep(3)
                driver.execute_script("""
                    const sendBtn = [...document.querySelectorAll('button')]
                        .find(b => b.textContent.trim() === 'Send without a note');
                    if (sendBtn) sendBtn.click();
                """)
                print(f"✅ Connected directly: {link}")
                time.sleep(4)
                continue

            # Try via More > Connect
            used_more = driver.execute_script("""
                const btn = document.querySelector('button[id$="-profile-overflow-action"]');
                if (btn) {
                    btn.click();
                    return true;
                }
                return false;
            """)

            if used_more:
                time.sleep(3)
                found_connect = driver.execute_script("""
                    const connectBtn = Array.from(document.querySelectorAll('span.display-flex.t-normal.flex-1'))
                        .find(el => el.textContent.trim() === 'Connect');
                    if (connectBtn) {
                        connectBtn.click();
                        return true;
                    }
                    return false;
                """)

                if found_connect:
                    time.sleep(3)
                    driver.execute_script("""
                        const sendWithoutNoteBtn = document.querySelector('button[aria-label="Send without a note"]');
                        if (sendWithoutNoteBtn) sendWithoutNoteBtn.click();
                    """)
                    print(f"✅ Connected via More menu: {link}")
                    time.sleep(4)
                else:
                    print(f"❌ Connect option not found in More menu: {link}")
            else:
                print(f"❌ No Connect or More button: {link}")

        except Exception as e:
            print(f"⚠️ Error visiting profile {link}: {e}")
        time.sleep(3)
