# 🧠 Meeting to Action Agent

## 📌 Overview

**Meeting to Action Agent** is an AI-powered system that transforms meeting discussions into **structured action items** and seamlessly syncs them with **Google Calendar**.

It analyzes meeting transcripts (entered as text or uploaded as `.txt` files), extracts **tasks, assignees, and deadlines**, and enables users to ask **context-aware follow-up questions**

Built using **FastAPI**, **Streamlit**, **LangChain**, and **Google Generative AI**, this project bridges the gap between **discussion and execution**, turning meetings into actionable, trackable outcomes.

## ⚙️ Tech Stack

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### AI & Text Processing

* LangChain
* Google Generative AI
* Sentence Transformers

### Calendar Integration

* Google Calendar API

### Storage & Parsing

* FAISS
* Dateparser
* `ics`

### Environment

* Local Development

---

## ⚙️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY = YOUR_GEMINI_API_KEY
```

---

### 3️⃣ Run Backend (FastAPI)

```bash
uvicorn main:app --reload
```

---

### 4️⃣ Run Frontend (Streamlit)

```bash
streamlit run chat_app.py
```

---

## 🧩 How It Works

1. Users upload or paste meeting transcripts via the Streamlit interface.
2. The FastAPI backend processes the text using **LLM-based analysis**.
3. Tasks, assignees, and deadlines are extracted and structured.
4. Valid tasks are optionally synced to **Google Calendar**.
5. Users can ask follow-up questions to retrieve summaries, responsibilities, and deadlines. is an open-source project, and contributions, experimentation, and learning are welcome.
