# LinkedIn Auto Connect Agent 🤖

An intelligent Selenium-based agent that logs into LinkedIn, searches for people based on configurable criteria, applies multiple filters, scrolls through search results, collects profile links, and automatically sends connection requests.

## 💡 Features

- Logs in using secure credentials stored in `.env`.
- Accepts search term from user input in `main.py`.
- Applies advanced filters like:
  - People
  - Actively Hiring (with job titles)
  - Locations
  - Current Companies
- Scrolls and extracts all profile URLs from the result page.
- Visits each profile and:
  - Clicks `Connect` if available directly.
  - Opens the `More` menu and selects `Connect` if necessary.
- Saves all visited profile links to a fresh log file for each run.

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/linkedin-auto-connect.git
cd linkedin-auto-connect
```

### 2. Install Dependencies

Create a virtual environment and install requirements:

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file (or `config.env`) in the root directory:

```env
LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password
APPLY_PEOPLE_FILTER=True
ACTIVELY_HIRING_VALUES=Data Scientist,Machine Learning Engineer
LOCATIONS=India,United States
CURRENT_COMPANIES=Google,Microsoft
```

> ✅ Use commas to separate multiple values.

## 🚀 How to Run

1. Make sure `chromedriver` is installed and in your PATH.
2. Run the automation:

```bash
python main.py
```

You will be prompted to enter a **name or position** to search for.

## 📁 Project Structure

```
linkedin-auto-connect/
│
├── login.py          # Handles LinkedIn login
├── filters.py        # Applies filters from config
├── search_fill.py         # Searches user input
├── actions.py       # Scrolls, logs, and connects to profiles
├── main.py           # Entry point to orchestrate everything
├── config.env        # Your environment variables
└── requirements.txt  # Python dependencies
```

## 🧠 Notes

- Make sure you're complying with [LinkedIn's terms of service](https://www.linkedin.com/legal/user-agreement) when using automation tools.
- Introduce delays between actions to avoid detection or rate limiting.

## 🛡 Disclaimer

This project is intended for educational purposes only. Use at your own risk. The authors are not responsible for any misuse or account issues.

---

Made with 🧠 + 🕸️ by Shine Gupta