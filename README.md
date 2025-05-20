# LinkedIn Auto Connect Agent 🤖 + Streamlit UI 🚀

A powerful Selenium-based LinkedIn automation agent, now wrapped in a sleek **Streamlit interface**. This tool logs into LinkedIn, lets you **search dynamically**, apply filters, **auto-connect with relevant people**, and keeps a log — all from a friendly browser interface.

## 🎯 What This Does

- ✅ Logs in securely with your LinkedIn credentials (from `.env` or UI)
- 🔍 Accepts dynamic **search input** via Streamlit
- 🧠 Applies smart filters:
  - **People**
  - **Actively Hiring** (with custom job titles)
  - **Locations**
  - **Current Companies**
- 📜 Scrolls the results page, logs profile URLs
- 🤝 Visits each profile and sends connection requests:
  - Clicks `Connect` directly if visible
  - Or opens the `More` menu and selects `Connect`
- 📝 Saves visited profile links in a timestamped log file

---

## 📺 New: Streamlit UI for Seamless Control

![Streamlit Screenshot](https://github.com/Shine-5705/Connect_over_LinkedIN/assets/screenshot.png)

---

## ⚙️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/Shine-5705/Connect_over_LinkedIN.git
cd Connect_over_LinkedIN
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```

### 3. Add Your Credentials

Create a file called `.env` or `config.env` in the project root:

```env
LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password
```

> Credentials are safely stored using `python-dotenv`. No hardcoding in scripts.

---

## 🧑‍💻 How to Use

Launch the Streamlit app:

```bash
streamlit run app.py
```

Then, enter:

- Your LinkedIn login details
- Search term (e.g., "Data Scientist")
- Filter values (Actively Hiring titles, Locations, Companies)

Click **Start Automation** and let the bot handle everything!

---

## 📁 Project Structure

```
Connect_over_LinkedIN/
│
├── login.py              # Logs into LinkedIn
├── filters.py            # Applies user filters
├── search_fill.py        # Searches user input
├── actions.py            # Scrolls, collects links, connects to profiles
├── main.py               # Entry point logic
├── app.py                # 🌟 Streamlit frontend
├── config.env            # Stores credentials
├── requirements.txt      # Python dependencies
└── logs/                 # Timestamped logs of visited profiles
```

---

## 📌 Best Practices

- Don't spam Connect — use this tool with intent and moderation.
- Add delays (already built-in) to mimic human behavior.
- Use a **fresh `.env`** for different accounts if needed.

---

## ⚠️ Disclaimer

This tool is for **educational and research purposes**. By using it, you agree to take full responsibility for how you automate LinkedIn.

> ❌ Automating connections at scale can violate [LinkedIn's Terms of Service](https://www.linkedin.com/legal/user-agreement).

---

Made with 🧠 + 🕸️ by Shine Gupta  
✨ Contributions welcome!
