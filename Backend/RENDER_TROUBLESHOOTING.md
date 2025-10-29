# 🔧 Rozwiązywanie problemów z wdrożeniem na Render

## Status: failed - Exited with status 1

### Najczęstsze przyczyny błędów:

1. **Problemy z ścieżkami i folderami**
2. **Brakujące zależności**
3. **Problem z importami Python**
4. **Brak uprawnień do folderów**

## 🔍 Jak sprawdzić dokładny błąd:

### W Render Dashboard:
1. Przejdź do swojego serwisu
2. Kliknij zakładkę **"Logs"**
3. Sprawdź **"Build Logs"** - tam znajdziesz dokładny komunikat błędu

## 🛠️ Najczęstsze rozwiązania:

### Problem 1: Błąd "No module named ..."

**Rozwiązanie**: 
- Upewnij się, że wszystkie pliki są w repozytorium
- Sprawdź czy `requirements.txt` zawiera wszystkie potrzebne pakiety

### Problem 2: Błąd "Permission denied" lub problemy z folderami

**Rozwiązanie**:
Render potrzebuje uprawnień do tworzenia folderów. Sprawdź czy:
- Folder `upload` ma plik `.gitkeep` (utwórz jeśli nie ma)
- Folder `data` ma plik `.gitkeep` (utwórz jeśli nie ma)

### Problem 3: Błąd przy starcie Gunicorn

**Rozwiązanie**:
- Upewnij się, że używasz najnowszego Procfile
- Sprawdź czy command: `gunicorn app:app --bind 0.0.0.0:$PORT`

### Problem 4: Import errors dla lokalnych modułów

**Rozwiązanie**:
Wszystkie foldery (`parsers`, `prompts`) muszą mieć plik `__init__.py`

## 📝 Krok po kroku - debugowanie:

### Krok 1: Sprawdź strukturę folderów
```bash
Backend/
├── __init__.py          # ← NOWY! Dodaj jeśli nie ma
├── app.py
├── quiz_main.py
├── processing.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── data/
│   └── data.txt
├── upload/
│   └── (pusty folder lub .gitkeep)
├── parsers/
│   ├── __init__.py
│   ├── csv_parser.py
│   ├── docx_parser.py
│   ├── pdf_txt_parser.py
│   └── text_parser.py
└── prompts/
    ├── __init__.py
    └── quiz_prompt.txt
```

### Krok 2: Upewnij się, że wszystkie pliki są w repozytorium
```bash
git add .
git commit -m "Fix deployment issues"
git push
```

### Krok 3: Jeśli używasz .render.yaml - usuń go tymczasowo

Spróbuj wdrożyć bez `.render.yaml` używając tylko Procfile:
- W Render Dashboard → Settings → Delete deploy key
- Następnie przejdź do Settings → i ustaw ręcznie:
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`

### Krok 4: Alternatywa - użyj gunicorn w startCommand

Zamiast Procfile, w Settings → Start Command wpisz:
```bash
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

## 🆘 Jeśli nadal nie działa:

### Opcja A: Sprawdź czy aplikacja działa lokalnie
```bash
cd Backend
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:5000
# W innym terminalu:
curl http://localhost:5000/
```

### Opcja B: Wyświetl dokładny error z logów

Skopiuj **cały błąd z logów** (Build Logs) i sprawdź:
1. Który dokładnie moduł nie może być zaimportowany?
2. Która komenda failuje?
3. Czy gunicorn się uruchamia?

### Opcja C: Minimalny test deploy

Możesz tymczasowo uprościć `app.py` do minimalnej wersji:

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"status": "ok", "message": "Backend is working!"}

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
```

Jeśli to działa, stopniowo dodawaj resztę funkcjonalności.

## 📧 Podaj więcej informacji:

Jeśli nadal masz problem, podaj:
1. **Pełny błąd z Build Logs** (skopiuj go tutaj)
2. **Którą metodę wdrożenia używasz** (.render.yaml czy ręcznie?)
3. **Czy aplikacja działa lokalnie?**

---
**Pamiętaj**: Najważniejsze to sprawdzić Build Logs w Render Dashboard - tam jest dokładna informacja o tym, co poszło nie tak!




