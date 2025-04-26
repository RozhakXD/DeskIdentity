# 💻 DeskIdentity | Dynamic User-Agent Generator for OS & Browsers
![DeskIdentity Logo](https://github.com/user-attachments/assets/35dd4b64-1bc8-4452-8203-68944c15b719)

**DeskIdentity** adalah API backend yang sederhana namun cerdas, dirancang untuk **menghasilkan user-agent** berdasarkan sistem operasi dan browser pilihan Anda. Solusi ini sangat cocok untuk **web scraping**, **pengujian otomatisasi**, dan **simulasi aktivitas pengguna** 🔍🤖.

## 🚀 Fitur Utama
- **Dukungan berbagai platform**: Windows, macOS, Linux, Android, iOS 🖥️📱
- **API berbasis Django** yang ringan dan cepat ⚡
- **Menghasilkan User-Agent yang dinamis** 🌐
- **Pilihan browser populer**: Chrome, Firefox, Edge, Safari, Opera 🌍

## 🌐 Deploy
Saat ini, DeskIdentity tersedia secara online di:  
[https://deskidentity.pythonanywhere.com](https://deskidentity.pythonanywhere.com)  

## 📦 Instalasi Lokal
```bash
git clone https://github.com/RozhakXD/DeskIdentity.git
cd DeskIdentity
pip install -r requirements.txt
python manage.py runserver
```

## 📚 Dokumentasi API
| Endpoint         | Method | Deskripsi                         |
|------------------|--------|-----------------------------------|
| `/api/generate/` | POST    | Menghasilkan user-agent acak     |

**Contoh Request:**
```bash
POST api/generate/
```

**Contoh Response:**
```json
{
  "os_type": "Linux",
  "browser": "Chrome",
  "count": 5,
  "unique": true
}
```

## 📸 Screenshot
![Welcome to Flows! - Rozhak's Workspace 26_04_2025](https://github.com/user-attachments/assets/d7c5b9a4-1dd8-4c26-8d50-d08c3e7ccddf)

## 🛠 Teknologi yang Digunakan
- **Python 3** 🐍
- **Django** 🕊️
- **REST Framework** 🔗

## 📃 Lisensi
Proyek ini dilisensikan di bawah MIT License. Silakan digunakan dan dikembangkan!
