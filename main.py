import os
from dotenv import load_dotenv
from login import linkedin_login
from search_fill import fill_search_bar
from filters import apply_filters
from connect_follow import scroll_and_click_buttons
from actions import scroll_and_collect_profiles, visit_profiles_and_connect


if __name__ == "__main__":
    load_dotenv("config.env")
    search_query = os.getenv("SEARCH_QUERY")

    if not search_query:
        print("❌ SEARCH_QUERY not found in config.env.")
    else:
        driver = linkedin_login()
        if driver:
            fill_search_bar(driver, search_query)
            apply_filters(driver)
            
            #scroll_and_click_buttons(driver)
            profile_links = scroll_and_collect_profiles(driver)

# Visit and connect
            visit_profiles_and_connect(driver, profile_links)
