# Viral Post Generator

An AI-powered Streamlit app that generates viral Twitter and LinkedIn posts from a story, script, or idea — tailored to your voice and style.

---

## Overview

This tool uses Anthropic's Claude API (or optionally OpenAI's GPT-4) to generate:
- 5 Twitter posts (short and punchy)
- 5 LinkedIn posts (professional and story-driven)
- Each post includes a **virality score** from 1–10

You can also:
- Upload your **past post scripts** for style matching
- Upload a `.csv` of **viral tweets** to guide tone and structure
- Scrape tweets using `snscrape` (optional, for devs)

---

## Features

- Input your idea, story, or topic
- Select a voice: Funny, Bold, Personal, or Professional
- Upload your past posts or tweet CSVs for tone matching
- Claude (or GPT) generates 10 viral posts ranked by potential
- Robust error handling if scraping/API fails

---

## Tech Stack

- **Python**
- **Streamlit** – for GUI
- **Anthropic Claude API** – AI text generation
- **Pandas** – CSV handling
- **snscrape** – (Optional) Twitter scraping
- **OpenAI GPT-4** – (Fallback option)

---

## Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/viral-post-generator.git
cd viral-post-generator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate     # On Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set your API key in `application.py`:
```python
client = anthropic.Anthropic(api_key="sk-ant-REPLACE-WITH-YOUR-KEY")
```

5. Run the app:
```bash
streamlit run application.py
```

---

## Sample Tweet CSV Format

To inspire the AI with real viral content, upload a CSV like this:

| Tweet                                           | Username     | Date       |
|------------------------------------------------|--------------|------------|
| Startups fail when founders build what they... | growth_guy   | 2025-08-01 |
| Most overnight successes took 5 years...       | noah_builder | 2025-07-28 |

---

## Prompt Logic

Claude is instructed to:
- Understand your tone and style
- Use platform-appropriate structure and language
- Maximize engagement potential
- Provide virality scoring (1–10)

---

## Author

**Matt Lee**  
Personal-use project to automate building-in-public content for social growth.  
Inspired by the need to post consistently without losing creativity.

---

## 🗓 Last Updated
August 14, 2025
