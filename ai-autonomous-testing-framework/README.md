# 🤖 AI-Driven Autonomous Testing Framework

## 🚀 Overview

This project is an intelligent test automation framework built using Playwright, Python, and OpenAI.

It enhances traditional automation by adding:

* AI-based failure analysis
* Self-healing locators
* Smart logging

---

## 🔥 Features

* UI & API Automation using Playwright
* AI failure analysis using GPT
* Self-healing locators
* JSON-based failure logging
* HTML reporting via pytest

---

## 🛠️ Tech Stack

* Python
* Playwright
* Pytest
* OpenAI API

---

## ▶️ Setup

```bash
pip install -r requirements.txt
playwright install
```

Set API Key:

```bash
export OPENAI_API_KEY="your_key"
```

---

## ▶️ Run Tests

```bash
pytest --html=report.html
```

---

## 📊 Sample AI Output

```json
{
  "test": "test_login",
  "error": "locator not found",
  "ai_analysis": "Element not found due to DOM change or incorrect selector"
}
```

---

## 💡 Future Enhancements

* AI-based locator generation
* Dashboard UI
* Test case auto generation

---

## 👨‍💻 Author

Ayush Gupta
