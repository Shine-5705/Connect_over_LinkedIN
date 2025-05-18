import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

load_dotenv("config.env")

def wait_and_click(driver, by, value, delay=10):
    for _ in range(delay):
        try:
            element = driver.find_element(by, value)
            element.click()
            return element
        except:
            time.sleep(1)
    raise Exception(f"Element not found or not clickable: {value}")

def select_autocomplete_option(driver, input_element, value):
    input_element.clear()
    input_element.send_keys(value)
    time.sleep(2)
    input_element.send_keys(Keys.ARROW_DOWN)
    input_element.send_keys(Keys.RETURN)
    time.sleep(1)

def apply_show_results_near(driver, context_xpath):
    try:
        context = driver.find_element(By.XPATH, context_xpath)
        show_button = context.find_element(By.XPATH, ".//button[span[text()[contains(., 'Show results')]]]")
        show_button.click()
        time.sleep(2)
        print("✅ Clicked 'Show results'")
    except NoSuchElementException:
        print("⚠️ 'Show results' not found within context – maybe already applied.")

def apply_filters(driver):
    if os.getenv("APPLY_PEOPLE_FILTER", "False").lower() == "true":
        try:
            wait_and_click(driver, By.XPATH, "//button[contains(., 'People')]")
            print("✅ People filter applied")
            time.sleep(2)
        except Exception as e:
            print("⚠️ Couldn't click 'People':", e)

    # Actively Hiring
    hiring_values = os.getenv("ACTIVELY_HIRING_VALUES", "").strip()
    if hiring_values:
        try:
            filter_button = wait_and_click(driver, By.ID, "searchFilter_activelyHiringForJobTitles")
            time.sleep(2)
            context_xpath = "//div[contains(@id,'artdeco-hoverable') and .//input[@placeholder='Hiring for job title']]"
            for val in hiring_values.split(","):
                try:
                    input_el = driver.find_element(By.XPATH, "//input[@placeholder='Hiring for job title']")
                    select_autocomplete_option(driver, input_el, val.strip())
                    print(f"✅ Actively hiring: selected '{val.strip()}'")
                except Exception as e:
                    print(f"❌ Failed to select actively hiring: {val.strip()} – {e}")
            apply_show_results_near(driver, context_xpath)
        except Exception as e:
            print("⚠️ Error handling Actively Hiring filter:", e)

    # Locations
    location_values = os.getenv("LOCATIONS", "").strip()
    if location_values:
        try:
            filter_button = wait_and_click(driver, By.ID, "searchFilter_geoUrn")
            time.sleep(2)
            context_xpath = "//div[contains(@id,'artdeco-hoverable') and .//input[@placeholder='Add a location']]"
            for val in location_values.split(","):
                try:
                    input_el = driver.find_element(By.XPATH, "//input[@placeholder='Add a location']")
                    select_autocomplete_option(driver, input_el, val.strip())
                    print(f"✅ Location selected: {val.strip()}")
                except Exception as e:
                    print(f"❌ Failed to select location: {val.strip()} – {e}")
            apply_show_results_near(driver, context_xpath)
        except Exception as e:
            print("⚠️ Error handling Locations filter:", e)

    # Current Company
    company_values = os.getenv("CURRENT_COMPANIES", "").strip()
    if company_values:
        try:
            filter_button = wait_and_click(driver, By.ID, "searchFilter_currentCompany")
            time.sleep(2)
            context_xpath = "//div[contains(@id,'artdeco-hoverable') and .//input[@placeholder='Add a company']]"
            for val in company_values.split(","):
                try:
                    input_el = driver.find_element(By.XPATH, "//input[@placeholder='Add a company']")
                    select_autocomplete_option(driver, input_el, val.strip())
                    print(f"✅ Company selected: {val.strip()}")
                except Exception as e:
                    print(f"❌ Failed to select company: {val.strip()} – {e}")
            apply_show_results_near(driver, context_xpath)
        except Exception as e:
            print("⚠️ Error handling Current Company filter:", e)
