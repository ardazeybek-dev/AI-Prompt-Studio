import os
import traceback

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY tanımlı değil. backend/.env dosyası oluşturup "
        "GROQ_API_KEY=... satırını ekleyin (.env.example dosyasına bakın)."
    )

client = Groq(api_key=GROQ_API_KEY)

app = FastAPI(title="AI Prompt Studio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    text: str

@app.post("/api/generate")
async def generate_prompt(request: PromptRequest):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Sen profesyonel bir prompt mühendisisin. Sana verilen basit fikri alıp detaylı, sinematik ve İngilizce bir görsel oluşturma promptuna dönüştür."
                },
                {
                    "role": "user",
                    "content": f"Fikir: {request.text}"
                }
            ],
            model="llama-3.1-8b-instant",
        )
        return {"prompt": chat_completion.choices[0].message.content}
    except Exception as e:
        print("\n" + "="*40)
        print("🚨 GROQ API HATASI DETAYI 🚨")
        print(traceback.format_exc())
        print("="*40 + "\n")
        raise HTTPException(status_code=500, detail=str(e))