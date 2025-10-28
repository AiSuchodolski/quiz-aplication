# 🚀 Instrukcja Wdrożenia - Quiz Application

## Przegląd
Aplikacja Quiz składa się z:
- **Backend** (Flask) - Render.com
- **Frontend** (HTML/CSS/JS) - Vercel

---

## 📦 Backend na Render.com

### Wymagania wstępne
- Konto na [Render.com](https://render.com)
- Git repository (GitHub/GitLab/Bitbucket)

### Kroki wdrożenia

#### 1. Przygotowanie repozytorium
```bash
# Upewnij się, że wszystkie pliki są zapisane
cd quiz-aplication/Backend
git add .
git commit -m "Ready for deployment"
git push
```

#### 2. Konfiguracja na Render.com

1. Zaloguj się na [Render Dashboard](https://dashboard.render.com)
2. Kliknij **"New +"** → **"Web Service"**
3. Połącz swoje repozytorium
4. **WAŻNE**: Ustawienia Root Directory:
   - Jeśli Backend jest w root repo → zostaw **PUSTE** lub wpisz `Backend`
   - Jeśli Backend jest w `quiz-aplication/Backend` → wpisz `quiz-aplication/Backend`
5. Ustawienia:
   - **Name**: quiz-backend (lub dowolna nazwa)
   - **Region**: Najbliższy do twoich użytkowników
   - **Branch**: main/master
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`

#### 3. Zmienne środowiskowe (opcjonalne)
W sekcji "Environment" dodaj (jeśli potrzebujesz):
```
PORT=5000
FLASK_ENV=production
```

#### 4. Deploy
Kliknij **"Create Web Service"**

#### 5. Skopiuj URL
Po wdrożeniu skopiuj URL (np. `https://quiz-backend-xxxx.onrender.com`)

---

## 🌐 Frontend na Vercel

### Wymagania wstępne
- Konto na [Vercel](https://vercel.com)
- Konto GitHub/GitLab/Bitbucket (wymagane przez Vercel)

### Kroki wdrożenia

#### 1. Zaktualizuj URL Backend w frontendzie

Edytuj plik `quiz-aplication/Frontend/index.html`:

Znajdź linię 604:
```javascript
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:5003'
    : 'https://YOUR-RENDER-APP.onrender.com'; // Zastąp to URL twojego Render app
```

Zastąp `YOUR-RENDER-APP.onrender.com` **URL twojego backendu z Render** (np. `quiz-backend-xxxx.onrender.com`)

```javascript
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:5003'
    : 'https://quiz-backend-xxxx.onrender.com';
```

#### 2. Wdróż na Vercel

**Opcja A: Za pomocą Vercel CLI**

```bash
# Zainstaluj Vercel CLI
npm i -g vercel

# Przejdź do folderu frontend
cd quiz-aplication/Frontend

# Wdróż
vercel

# Następnie wdróż do produkcji
vercel --prod
```

**Opcja B: Za pomocą GitHub Integration**

1. Zaloguj się na [Vercel Dashboard](https://vercel.com/dashboard)
2. Kliknij **"Add New..."** → **"Project"**
3. Zaimportuj repozytorium
4. W ustawieniach:
   - **Framework Preset**: Other
   - **Root Directory**: `quiz-aplication/Frontend`
   - **Build Command**: (zostaw puste)
   - **Output Directory**: (zostaw puste)
5. Kliknij **"Deploy"**

---

## ⚙️ Konfiguracja CORS (ważne!)

### Po wdrożeniu na Vercel

1. Skopiuj URL twojego frontendu z Vercel (np. `https://quiz-app.vercel.app`)
2. Edytuj plik `Backend/app.py` w repozytorium
3. Znajdź sekcję CORS (około linii 17-23)
4. Zmień:
```python
CORS(app, resources={
    r"/*": {
        "origins": ["*"],  # Zmień na URL twojego frontendu
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "X-OpenAI-API-Key"]
    }
})
```

Na:
```python
CORS(app, resources={
    r"/*": {
        "origins": ["https://YOUR-VERCEL-APP.vercel.app", "https://localhost:5003"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "X-OpenAI-API-Key"]
    }
})
```

5. Wdróż ponownie na Render:
```bash
git add Backend/app.py
git commit -m "Update CORS for production"
git push
```

---

## 🔧 Testowanie

### Lokalnie
```bash
# Backend
cd Backend
python app.py

# Frontend - otwórz w przeglądarce
# Plik: quiz-aplication/Frontend/index.html
```

### Produkcja
1. Otwórz URL z Vercel
2. Sprawdź czy klucz API jest zapisywany
3. Prześlij plik
4. Rozpocznij quiz

---

## 🐛 Rozwiązywanie problemów

### Backend nie odpowiada
- Sprawdź logi na Render Dashboard
- Upewnij się, że PORT jest ustawiony
- Sprawdź czy requirements.txt zawiera wszystkie zależności

### CORS Error w przeglądarce
- Upewnij się, że URL frontendu jest dodany do CORS origins
- Sprawdź czy backend jest wdrożony i działa

### Błąd "Module not found"
- Sprawdź czy wszystkie pliki Python są w repozytorium
- Upewnij się, że requirements.txt zawiera wszystkie zależności

### API Key nie działa
- Upewnij się, że nagłówek X-OpenAI-API-Key jest wysyłany
- Sprawdź konsole przeglądarki (F12) dla błędów

---

## 📝 Uwagi bezpieczeństwa

1. **Klucz API OpenAI**: Jest przechowywany tylko w sessionStorage przeglądarki użytkownika
2. **CORS**: Konfigurowany jest white-list domen
3. **Debug mode**: Wyłączony w produkcji (`debug=False`)
4. **HTTPS**: Wszystkie połączenia w produkcji używają HTTPS

---

## 🎉 Gotowe!

Po wdrożeniu:
- Backend: `https://your-backend.onrender.com`
- Frontend: `https://your-frontend.vercel.app`

Użytkownicy mogą teraz korzystać z aplikacji bez instalowania niczego lokalnie!

