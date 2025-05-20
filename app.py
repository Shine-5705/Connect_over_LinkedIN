import streamlit as st
import os
import subprocess
from streamlit_extras.let_it_rain import rain
from streamlit_extras.add_vertical_space import add_vertical_space

def save_env_config(email, password, query, people_filter, hiring_vals, locations, companies):
    config_lines = [
        f"LINKEDIN_EMAIL={email}",
        f"LINKEDIN_PASSWORD={password}",
        f"SEARCH_QUERY={query}",
        f"APPLY_PEOPLE_FILTER={'True' if people_filter else 'False'}",
        f"ACTIVELY_HIRING_VALUES={hiring_vals}",
        f"LOCATIONS={locations}",
        f"CURRENT_COMPANIES={companies}"
    ]
    with open("config.env", "w") as f:
        f.write("\n".join(config_lines))

st.set_page_config(page_title="LinkedIn Automation Tool", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #0072b1;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.image("https://cdn-icons-png.flaticon.com/512/174/174857.png", width=80)
st.title("🔍 LinkedIn Automation Tool")
st.caption("Automate search and connection on LinkedIn with custom filters")

add_vertical_space(1)

with st.container():
    email = st.text_input("📧 LinkedIn Email")
    password = st.text_input("🔒 LinkedIn Password", type="password")
    search_query = st.text_input("🔍 Search Query", placeholder="e.g. Data Scientist")
    people_filter = st.checkbox("👥 Apply 'People' Filter")
    hiring_values = st.text_input("💼 Actively Hiring Job Titles", placeholder="e.g. Software Engineer, Product Manager")
    locations = st.text_input("🌍 Locations", placeholder="e.g. India, United States")
    companies = st.text_input("🏢 Current Companies", placeholder="e.g. Google, Microsoft")

add_vertical_space(1)

if st.button("🚀 Run LinkedIn Bot"):
    if email and password and search_query:
        save_env_config(email, password, search_query, people_filter, hiring_values, locations, companies)
        st.success("✅ Config file saved. Running the bot...")

        try:
            subprocess.run(["python", "main.py"], check=True)
            st.balloons()
            rain(emoji="🤖", font_size=30, falling_speed=5, animation_length=1.5)
            st.success("🎉 Bot execution finished.")
        except subprocess.CalledProcessError as e:
            st.error(f"❌ Bot execution failed: {e}")
    else:
        st.error("⚠️ Please enter all required fields (email, password, search query)")