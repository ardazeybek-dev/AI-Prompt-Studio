# AI Prompt Studio 🚀

A web app that turns your simple ideas into professional, cinematic, English image-generation prompts.

You type an idea (e.g. *"a documentary scene about the history of Bergama"*), and the app sends it to a
large language model (Llama 3.1 via Groq) to expand it into a detailed visual prompt.

## Architecture

| Layer     | Technology                    | Role                                          |
|-----------|-------------------------------|-----------------------------------------------|
| Frontend  | React + Vite                  | User interface and API requests               |
| Backend   | FastAPI (Python)              | Groq API integration and prompt generation    |
| AI        | Groq / `llama-3.1-8b-instant` | Turning the idea into a professional prompt   |

## Setup

### 1) Backend (FastAPI)

```bash
cd backend

# Virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# API key: copy .env.example to .env and add your key
copy .env.example .env      # Windows
# cp .env.example .env      # macOS / Linux
```

Add your Groq API key (https://console.groq.com/keys) to `.env`:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
```

> 🔐 **Security:** The API key is no longer hard-coded — it is read from `.env`, and `.env` is not
> committed to git. Never share your key in a public repository.

Start the server:

```bash
python -m uvicorn main:app --reload
```

The backend runs at `http://localhost:8000`.

### 2) Frontend (React + Vite)

In a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` in your browser.

> If the backend runs on a different address, set `VITE_API_URL` in `frontend/.env`
> (see `frontend/.env.example`).

## Helper Script

`backend/modeller.py` — lists the Groq models available to your API key:

```bash
python modeller.py
```

## Project Structure

```
AI-Prompt-Studio/
├── backend/
│   ├── main.py            # FastAPI server + Groq integration
│   ├── modeller.py        # Helper script that lists available models
│   ├── requirements.txt   # Python dependencies
│   └── .env.example       # Example environment variables
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # UI component and API request
│   │   ├── main.jsx       # React entry point
│   │   └── index.css      # Dark theme styles
│   ├── index.html         # HTML template
│   ├── package.json       # Frontend dependencies
│   └── .env.example       # Example environment variables
└── Readme.md
```
