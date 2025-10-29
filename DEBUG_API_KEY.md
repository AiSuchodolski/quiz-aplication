# 🔍 Debugowanie - Problem z kluczem API

## Problem
"Błąd podczas generowania pytania. Sprawdź poprawność klucza API."

## 🔎 Kroki diagnostyczne:

### Krok 1: Sprawdź konsolę przeglądarki

1. Otwórz aplikację na Vercel: https://quiz-aplication2.vercel.app
2. Otwórz konsolę (F12) → zakładka **Console**
3. Wprowadź klucz API i spróbuj utworzyć quiz
4. **Skopiuj dokładny błąd** z konsoli

### Krok 2: Sprawdź czy klucz API jest zapisany

W konsoli przeglądarki wpisz:
```javascript
sessionStorage.getItem('openai_api_key')
```

Jeśli pokazuje `null` lub pustą wartość → klucz nie został zapisany

### Krok 3: Sprawdź logi Render (WAŻNE!)

1. Wejdź na Render Dashboard
2. Kliknij swoją aplikację backend
3. Przejdź do zakładki **Logs**
4. Spróbuj utworzyć quiz na frontendzie
5. **Sprawdź co pojawia się w logach** - tam będzie dokładny błąd!

---

## 🚨 Najczęstsze przyczyny:

### 1. Klucz API nie jest wysyłany w nagłówku
**Sprawdź**: W Network tab (F12) czy request do `/quiz/question` ma nagłówek `X-OpenAI-API-Key`?

### 2. Klucz API jest nieważny
**Rozwiązanie**: Sprawdź czy klucz jest poprawny w https://platform.openai.com/api-keys

### 3. CORS blokuje żądanie
**Sprawdź**: W Network tab czy response ma status 400/500 czy CORS error?

### 4. Backend nie ma dostępu do OpenAI
**Sprawdź**: W Render Logs czy jest błąd połączenia z OpenAI API

### 5. Format klucza API jest niepoprawny
**Sprawdź**: Klucz powinien zaczynać się od `sk-` i mieć długość ~51 znaków

---

## 📋 Co mi podaj:

1. **Błąd z konsoli przeglądarki** (Console tab)
2. **Błąd z Network tab** (status code i response)
3. **Logi z Render** (ostatnie 20 linii po próbie utworzenia quizu)
4. **Czy klucz się zapisuje?** (wpisz w console: `sessionStorage.getItem('openai_api_key')`)

---

## 🛠️ Szybkie testy:

### Test 1: Sprawdź czy klucz jest wysyłany
W Network tab:
1. Kliknij request do `/quiz/question`
2. Sprawdź **Headers** → **Request Headers**
3. Szukaj: `X-OpenAI-API-Key: sk-...`

### Test 2: Sprawdź response
W tym samym request:
1. Sprawdź **Response**
2. Jaki jest dokładny komunikat błędu?

### Test 3: Test lokalnie
Jeśli masz backend lokalny:
```bash
cd Backend
python app.py
# W przeglądarce: http://localhost:5003
```
Sprawdź czy działa lokalnie z tym samym kluczem.

---

**Prześlij mi wyniki tych testów!**




