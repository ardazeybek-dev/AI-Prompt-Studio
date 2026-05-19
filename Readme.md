ack-End (Arka Yüz) Kurulumu
Backend klasörüne geçiş yapın, sanal ortamı (virtual environment) aktifleştirin ve gerekli kütüphaneleri yükleyin:

Bash
cd backend
# Sanal ortam oluşturma (Eğer yoksa)
python -m venv venv

# Sanal ortamı aktifleştirme (Windows)
.\\venv\\Scripts\\activate

# Gerekli kütüphanelerin yüklenmesi
pip install fastapi uvicorn pydantic groq

API Anahtarı Yapılandırması 🔑
backend/main.py dosyası içerisinde yer alan api_key alanına kendi Groq API anahtarınızı girmeniz gerekmektedir:

Python
client = Groq(api_key="BURAYA_GROQ_API_KEYINIZI_YAZIN")
Güvenlik Uyarısı: API anahtarınızı GitHub gibi açık platformlarda herkese açık şekilde paylaşmamanız, projenin güvenliği ve kotanızın tükenmemesi açısından kritik önem taşımaktadır.

Arka Yüzü Başlatın:
Bash
python -m uvicorn main:app --reload
Sunucu varsayılan olarak http://localhost:8000 adresinde çalışmaya başlayacaktır.
Front-End (Ön Yüz) Kurulumu
Yeni bir terminal sekmesi açın, frontend klasörüne geçiş yapın ve bağımlılıkları yükleyip projeyi ayağa kaldırın:

Bash
cd frontend
# Node modüllerini yükleyin
npm install

# Ön yüzü yerel sunucuda başlatın
npm run dev
Tarayıcınızda http://localhost:5173 (veya terminalde belirtilen local port) adresine giderek uygulamayı kullanmaya başlayabilirsiniz.
Proje Klasör Yapısı
Plaintext
ai-prompt-studio/
├── backend/
│   ├── main.py          # FastAPI Sunucu Kodları ve Groq Entegrasyonu
│   └── modeller.py      # API Modellerini Listeleme ve Test Scripti
├── frontend/
│   ├── src/
│   │   ├── App.jsx      # Ön Yüz Arayüz Bileşeni ve API İstek Mekanizması
│   │   ├── main.jsx     # React Giriş Noktası
│   │   └── index.css    # Özelleştirilmiş Karanlık Tema Stilleri
│   ├── index.html       # Ana HTML Şablonu
│   └── package.json     # Ön Yüz Bağımlılık Listesi
└── venv/                # Python Sanal Ortam Klasörü
