"""Helper script: lists the Groq models available to your API key.

Usage:
    python modeller.py

Note: the API key is read from the .env file (GROQ_API_KEY); it is never hard-coded.
"""

import os
import sys

from dotenv import load_dotenv
from groq import Groq

# Force UTF-8 output so it doesn't break on the Windows console.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise SystemExit(
        "GROQ_API_KEY is not set. Add GROQ_API_KEY=... to your backend/.env file."
    )

client = Groq(api_key=api_key)

print("\n--- MODELS AVAILABLE TO YOUR API KEY ---")
for model in client.models.list().data:
    print(model.id)
print("----------------------------------------\n")
