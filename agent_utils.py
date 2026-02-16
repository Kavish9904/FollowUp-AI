import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_tasks_from_text(transcript: str):
    """
    Uses Gemini to extract structured tasks from meeting transcripts.
    Returns parsed JSON list.
    """
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    Extract actionable tasks from the transcript below.

    Return ONLY valid JSON in this format:

    [
      {{
        "person": "Name",
        "task": "Task description",
        "deadline": "YYYY-MM-DD or natural language",
        "status": "Pending"
      }}
    ]

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)

    try:
        tasks = json.loads(response.text.strip())
        return tasks
    except Exception:
        return []
