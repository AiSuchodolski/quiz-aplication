# 🚀 Wdrożenie Frontendu na Vercel

## ✅ Backend już działa!

Najpierw musisz zaktualizować URL backendu w frontendzie.

## Krok 1: Zaktualizuj URL Backend w index.html

### Znajdź URL swojego Render backendu:
1. Wejdź na Render Dashboard
2. Kliknij swoją aplikację backend
3. Na górze zobaczysz URL (np. `https://quiz-backend-xxxx.onrender.com`)
4. **Skopiuj ten URL**

### Zmień w index.html:

Otwórz: `quiz-aplication/Frontend/index.html`

Znajdź linię ~604:
```javascript
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:5003'
    : 'https://YOUR-RENDER-APP.onrender.com'; // ← ZAMIEŃ TUTAJ!
```

Zmień na:
```javascript
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:5003'
    : 'https://quiz-backend-xxxx.onrender.com'; // ← Twój Render URL
```

### Zapisz i wyślij na GitHub:
```bash
cd "C:\Users\ASUS\Desktop\AISuchodolski\Ready 4 AI\Aplikacja\quiz-aplication"
git add Frontend/index.html
git commit -m "Update backend URL for production"
git push
```

---

## Krok 2: Wdróż na Vercel

### Opcja A: Za pomocą GitHub Integration (ZALECANE) ✅

1. Przejdź na: https://vercel.com/dashboard
2. Zaloguj się (użyj GitHub)
3. Kliknij **"Add New..."** → **"Project"**
4. Wybierz repozytorium: `AiSuchodolski/quiz-aplication`
5. W ustawieniach projektu:
   - **Framework Preset**: Other
   - **Root Directory**: `Frontend` ← WAŻNE!
   - **Build Command**: (zostaw puste)
   - **Output Directory**: (zostaw puste)
   - **Install Command**: (zostaw puste)
6. Kliknij **"Deploy"**

### Opcja B: Za pomocą Vercel CLI

```bash
# Zainstaluj Vercel CLI (jeśli nie masz)
npm i -g vercel

# Przejdź do folderu frontend
cd "C:\Users\ASUS\Desktop\AISuchodolski\Ready 4 AI\Aplikacja\quiz-aplication\Frontend"

# Wdróż
vercel

# Wdróż do produkcji
vercel --prod
```

---

## Krok 3: Po wdrożeniu

Vercel da Ci URL (np. `https://quiz-frontend.vercel.app`)

### Sprawdź czy działa:
1. Otwórz URL z Vercel
2. Sprawdź konsolę (F12) - czy są błędy?
3. Przetestuj aplikację

---

## Krok 4: Zaktualizuj CORS w Render (WAŻNE!)

### Po uzyskaniu URL z Vercel:

1. Skopiuj URL frontendu (np. `https://quiz-frontend.vercel.app`)
2. W Render Dashboard → Twoja aplikacja → Settings
3. W sekcji **"Environment"** dodaj zmienną:
   - **Key**: `FRONTEND_URL`
   - **Value**: `https://quiz-frontend.vercel.app`
4. Zapisz

### LUB zaktualizuj app.py:

Edytuj `Backend/app.py` linia ~19:
```python
CORS(app, resources={
    r"/*": {
        "origins": ["https://quiz-frontend.vercel.app", "http://localhost:5003"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "X-OpenAI-API-Key"]
    }
})
```

Zapisz, commit, push:
```bash
git add Backend/app.py
git commit -m "Update CORS with Vercel URL"
git push
```

Render automatycznie wdroży nową wersję.

---

## 🎉 Gotowe!

Teraz masz:
- **Backend**: `https://quiz-backend-xxxx.onrender.com`
- **Frontend**: `https://quiz-frontend.vercel.app`

Wszystko działa! Użytkownicy mogą korzystać z aplikacji online! 🌐

