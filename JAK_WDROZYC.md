# 🚀 Jak uruchomić deploy po zmianach na GitHub

## Po przesłaniu zmian na GitHub:

### Krok 1: Przejdź do Render Dashboard
Wejdź na: https://dashboard.render.com

### Krok 2: Znajdź swoją aplikację
Kliknij na nazwę Twojej aplikacji (quiz-backend)

### Krok 3: Uruchom manual deploy
Masz **3 opcje**:

#### Opcja A: Manual Deploy (REKOMENDOWANE) ✅
1. W głównym widoku aplikacji znajdź przycisk **"Manual Deploy"** (górny prawy róg)
2. Kliknij **"Manual Deploy"**
3. Wybierz **"Deploy latest commit"**
4. Kliknij **"Deploy"**

#### Opcja B: Re-trigger deploy
1. Przejdź do zakładki **"Logs"**
2. Na górze znajdź **"Retry deploy"** lub **"Redeploy"**
3. Kliknij

#### Opcja C: Zmiana Trigger Settings
1. Przejdź do **Settings**
2. W sekcji **"Auto-Deploy"** wybierz:
   - **"Yes"** - auto-deploy każdy push
   - **"Manual"** - deploy tylko ręcznie
3. Kliknij **"Save Changes"**
4. Potem użyj Opcji A (Manual Deploy)

---

## ⚠️ WAŻNE: Ustaw Root Directory PRZED deploy!

### Przed uruchomieniem deploy, upewnij się że:
1. Przejdź do **Settings**
2. W polu **"Root Directory"** wpisz: `quiz-aplication/Backend`
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
5. Kliknij **"Save Changes"**
6. **TERAZ** uruchom Manual Deploy

---

## 📋 Po uruchomieniu deploy:

### Sprawdź postęp:
1. Wejdź w zakładkę **"Events"** lub **"Logs"**
2. Śledź postęp build
3. Szukaj komunikatów:
   - ✅ "Build successful"
   - ✅ "Starting gunicorn"
   - ✅ "Application successfully started"

### Czas oczekiwania:
- Pierwszy deploy: ~5-10 minut
- Kolejne deploys: ~2-5 minut

### Jeśli będzie błąd:
- Kliknij w zakładkę **"Logs"**
- Sprawdź **"Build Logs"** (w górnej części)
- Skopiuj błąd i sprawdź czy problem został rozwiązany

---

## 🎯 Checklist przed deploy:

- [ ] Zmiany są w GitHubie (git push)
- [ ] Root Directory = `quiz-aplication/Backend`
- [ ] Build Command = `pip install -r requirements.txt`
- [ ] Start Command = `gunicorn app:app --bind 0.0.0.0:$PORT`
- [ ] Kliknąłeś "Save Changes"
- [ ] Uruchomiłeś "Manual Deploy"

---

## ✅ Po udanym deploy:

1. Sprawdź **URL** (na górze Dashboard)
2. Wejdź na ten URL
3. Powinieneś zobaczyć: "Witaj w aplikacji QUIZ!"

Jeśli działa - **Gratulacje!** 🎉

