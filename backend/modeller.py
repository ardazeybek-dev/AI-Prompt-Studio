"""Yardımcı script: Groq API anahtarınıza açık olan modelleri listeler.

Kullanım:
    python modeller.py

Not: API anahtarı .env dosyasından (GROQ_API_KEY) okunur; koda gömülmez.
"""

import os
import sys

from dotenv import load_dotenv
from groq import Groq

# Windows konsolunda Türkçe karakterler için çıktıyı UTF-8'e sabitle.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise SystemExit(
        "GROQ_API_KEY tanımlı değil. backend/.env dosyasına GROQ_API_KEY=... ekleyin."
    )

client = Groq(api_key=api_key)

print("\n--- API ANAHTARINIZA AÇIK MODELLER ---")
for model in client.models.list().data:
    print(model.id)
print("--------------------------------------\n")
