import os
from dotenv import load_dotenv
from login import linkedin_login
from search_fill import fill_search_bar
from filters import apply_filters
from connect_follow import scroll_and_click_buttons
from connect_profiles import scroll_and_collect_links, connect_to_profiles


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
            profile_links = scroll_and_collect_links(driver)
            connect_to_profiles(driver, profile_links)
