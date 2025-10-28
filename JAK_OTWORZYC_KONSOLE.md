# 🔧 Jak otworzyć konsolę bez F12

## Metoda 1: PPM na stronie
1. Prawy przycisk myszy (PPM) na stronie
2. Wybierz **"Zbadaj"** lub **"Inspect"** lub **"Developer Tools"**

## Metoda 2: Menu przeglądarki
### Chrome/Edge:
1. Kliknij **3 kropki** (⋮) w prawym górnym rogu
2. Wybierz **"Narzędzia deweloperskie"** (Tools → Developer Tools)

### Firefox:
1. Kliknij **3 kreski** (☰) w prawym górnym rogu
2. Wybierz **"Developer Tools"**

## Metoda 3: Klawiatura ekranowa
1. Start → Windows Ease of Access → Klawiatura ekranowa
2. Kliknij **F12** na klawiaturze ekranowej

## Metoda 4: Skróty alternatywne
- **Ctrl + Shift + I** (Windows/Linux)
- **Cmd + Option + I** (Mac)

---

## Co teraz?

### Po otwarciu konsoli:

1. Przejdź do zakładki **"Console"** (na górze)
2. **Wyczyść konsolę** (ikonka: 🚫)
3. Wprowadź klucz API i spróbuj utworzyć quiz
4. **Skopiuj błędy** które się pojawią

### Albo przejdź do zakładki **"Network"**:
1. Wybierz zakładkę **Network**
2. Wyczyść (trash icon 🗑️)
3. Odśwież stronę i spróbuj utworzyć quiz
4. Kliknij na **`quiz/question`** (czerwony request jeśli błąd)
5. Sprawdź:
   - **Headers** tab → czy jest `X-OpenAI-API-Key`?
   - **Response** tab → jaki błąd?

---

## Lub sprawdź logi Render

### To może być szybsze:

1. Wejdź na **Render Dashboard**: https://dashboard.render.com
2. Kliknij swoją aplikację backend
3. Przejdź do zakładki **"Logs"**
4. Odśwież stronę i spróbuj utworzyć quiz
5. **Skopiuj logi** (ostatnie 50 linii wystarczy)

To pokaże dokładny błąd z backendu!

