import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_status(updates_text: str) -> str:
    prompt = f"""
You are a senior project coordinator writing a professional corporate email.

IMPORTANT RULES:
- Output must be plain text only
- Do NOT use markdown
- Do NOT use *, #, ###, **, bullet symbols, or separators
- Do NOT use tables
- Write in formal corporate email tone
- Structure content using normal paragraphs and numbered lists only

Write a daily project status email based on the tracker updates below.

Tracker updates:
{updates_text}
"""

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="openai/gpt-oss-120b",
    )

    return response.choices[0].message.content.strip()
