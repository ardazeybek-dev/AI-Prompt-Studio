# CLAUDE.md

Bu dosya, bu depoda çalışırken Claude Code'a (claude.ai/code) rehberlik eder.

## Proje

AI Prompt Studio — kullanıcının yazdığı basit fikri, Groq (Llama 3.1) üzerinden detaylı bir
İngilizce görsel oluşturma promptuna dönüştüren full-stack web uygulaması.

- **backend/** — FastAPI (Python). Tek endpoint: `POST /api/generate` (`{ "text": "..." }` alır,
  `{ "prompt": "..." }` döner).
- **frontend/** — React + Vite tek sayfa uygulama. `src/App.jsx` içindeki `handleGenerate` backend'e istek atar.

## Çalıştırma

Backend:
```bash
cd backend && pip install -r requirements.txt && python -m uvicorn main:app --reload
```
Frontend:
```bash
cd frontend && npm install && npm run dev
```

## Önemli kurallar

- **API anahtarları koda gömülmez.** Groq anahtarı `backend/.env` içindeki `GROQ_API_KEY`'den okunur.
  Yeni bir sır eklerken `.env.example` dosyasını da güncelle.
- Frontend, backend adresini `import.meta.env.VITE_API_URL` üzerinden alır; sabit URL yazma.
- `.env` dosyaları asla commit'lenmez (bkz. `.gitignore`).

## Build

- Frontend production build: `cd frontend && npm run build` → çıktı `frontend/dist/` (statik olarak deploy edilebilir).
- Backend statik deploy edilemez; ayrı bir sunucu ortamı (Render, Railway vb.) gerektirir.
