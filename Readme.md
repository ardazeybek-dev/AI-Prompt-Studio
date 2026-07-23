# AI Prompt Studio 🚀

Basit fikirlerinizi profesyonel, sinematik ve İngilizce görsel oluşturma promptlarına dönüştüren bir web uygulaması.

Kullanıcı bir fikir yazar (örn. *"Bergama'nın tarihi hakkında belgesel sahnesi"*), uygulama bu fikri
büyük bir dil modeline (Groq üzerinden Llama 3.1) göndererek detaylı bir görsel promptuna çevirir.

## Mimari

| Katman    | Teknoloji                     | Görevi                                            |
|-----------|-------------------------------|---------------------------------------------------|
| Frontend  | React + Vite                  | Kullanıcı arayüzü ve API istekleri                |
| Backend   | FastAPI (Python)              | Groq API entegrasyonu ve prompt üretimi           |
| AI        | Groq / `llama-3.1-8b-instant` | Fikri profesyonel prompta dönüştürme              |

## Kurulum

### 1) Backend (FastAPI)

```bash
cd backend

# Sanal ortam
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate

# Bağımlılıklar
pip install -r requirements.txt

# API anahtarı: .env.example dosyasını .env olarak kopyalayın ve anahtarınızı girin
copy .env.example .env      # Windows
# cp .env.example .env      # macOS / Linux
```

`.env` içine Groq API anahtarınızı yazın (https://console.groq.com/keys):

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
```

> 🔐 **Güvenlik:** API anahtarı artık koda gömülü değil, `.env` dosyasından okunur ve `.env` git'e
> gönderilmez. Anahtarınızı asla public bir repoda paylaşmayın.

Sunucuyu başlatın:

```bash
python -m uvicorn main:app --reload
```

Backend `http://localhost:8000` adresinde çalışır.

### 2) Frontend (React + Vite)

Yeni bir terminalde:

```bash
cd frontend
npm install
npm run dev
```

Tarayıcıda `http://localhost:5173` adresini açın.

> Backend farklı bir adreste çalışıyorsa `frontend/.env` dosyasında `VITE_API_URL` değişkenini ayarlayın
> (bkz. `frontend/.env.example`).

## Yardımcı Script

`backend/modeller.py` — API anahtarınıza açık olan Groq modellerini listeler:

```bash
python modeller.py
```

## Proje Yapısı

```
AI-Prompt-Studio/
├── backend/
│   ├── main.py            # FastAPI sunucu + Groq entegrasyonu
│   ├── modeller.py        # Açık modelleri listeleyen yardımcı script
│   ├── requirements.txt   # Python bağımlılıkları
│   └── .env.example       # Örnek ortam değişkenleri
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # Arayüz bileşeni ve API isteği
│   │   ├── main.jsx       # React giriş noktası
│   │   └── index.css      # Karanlık tema stilleri
│   ├── index.html         # HTML şablonu
│   ├── package.json       # Frontend bağımlılıkları
│   └── .env.example       # Örnek ortam değişkenleri
└── Readme.md
```
