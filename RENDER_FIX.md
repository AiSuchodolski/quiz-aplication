# 🔧 Naprawa - Błąd "Service Root Directory is missing"

## Problem
```
==> Service Root Directory "/opt/render/project/src/quiz-aplication/Backend" is missing.
```

## Przyczyna
Render Dashboard ma ustawiony **Root Directory** na `quiz-aplication/Backend`, ale struktura repo nie odpowiada tej ścieżce.

## ✅ Rozwiązanie - W Render Dashboard:

### Krok 1: Usuń .render.yaml tymczasowo
```bash
# Zostań w folderze głównym quiz-aplication
git rm Backend/.render.yaml
git commit -m "Remove render.yaml for manual config"
git push
```

### Krok 2: W Render Dashboard

1. Przejdź do twojego serwisu na Render
2. Kliknij **"Settings"** (lewy sidebar)
3. Przewiń w dół do sekcji **"Build & Deploy"**
4. Znajdź pole **"Root Directory"**
5. **USUŃ** wszystko z tego pola (zostaw PUSTE) lub wpisz `Backend`
6. Upewnij się że:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
7. Kliknij **"Save Changes"**

### Krok 3: Manual Deploy
Po zapisaniu zmian, kliknij **"Manual Deploy"** → **"Deploy latest commit"**

---

## Alternatywa: Poprawna ścieżka w Root Directory

Jeśli chcesz użyć Root Directory, sprawdź strukturę repo:

### Jeśli struktura to:
```
your-repo/
└── Backend/
    └── app.py
```

To **Root Directory** = `Backend`

### Jeśli struktura to:
```
your-repo/
└── quiz-aplication/
    └── Backend/
        └── app.py
```

To **Root Directory** = `quiz-aplication/Backend`

### Sprawdź strukturę:
W terminalu:
```bash
cd path/to/your/repo
ls -la
# Co widzisz?
```

---

## 🎯 Polecane ustawienia Render:

```
Root Directory: (PUSTE lub Backend)
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
```

**Python Version**: 3.11.7 (automatycznie z runtime.txt)

---

## 📋 Po zmianach:

1. Wszystkie zmiany commit i push
2. W Render kliknij "Manual Deploy"
3. Sprawdź Logs - powinno działać!

