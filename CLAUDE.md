# CLAUDE.md

This file guides Claude Code (claude.ai/code) when working in this repository.

## Project

AI Prompt Studio — a full-stack web app that turns a user's simple idea into a detailed English
image-generation prompt via Groq (Llama 3.1).

- **backend/** — FastAPI (Python). Single endpoint: `POST /api/generate` (takes `{ "text": "..." }`,
  returns `{ "prompt": "..." }`).
- **frontend/** — React + Vite single-page app. `handleGenerate` in `src/App.jsx` calls the backend.

## Running

Backend:
```bash
cd backend && pip install -r requirements.txt && python -m uvicorn main:app --reload
```
Frontend:
```bash
cd frontend && npm install && npm run dev
```

## Key rules

- **No API keys in code.** The Groq key is read from `GROQ_API_KEY` in `backend/.env`.
  When adding a new secret, also update `.env.example`.
- The frontend gets the backend address from `import.meta.env.VITE_API_URL`; never hard-code the URL.
- `.env` files are never committed (see `.gitignore`).

## Build

- Frontend production build: `cd frontend && npm run build` → output in `frontend/dist/` (deployable as static).
- The backend cannot be deployed as static; it needs a server environment (Render, Railway, etc.).
