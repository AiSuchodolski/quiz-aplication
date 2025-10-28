# 🧠 Aplikacja Quiz - System Zarządzania Danymi i Quizami

Aplikacja do tworzenia quizów na podstawie przesłanych materiałów edukacyjnych z wykorzystaniem OpenAI.

## 📋 Funkcje

- 📤 Przesyłanie plików (PDF, DOCX, CSV, TXT)
- 🤖 Generowanie pytań quizowych z pomocą AI
- 🔑 Bezpieczne zarządzanie kluczem API OpenAI
- 📊 Śledzenie wyników w czasie rzeczywistym
- 💾 Przechowywanie danych użytkownika

## 🏗️ Struktura projektu

```
quiz-aplication/
├── Backend/          # Flask API (Python)
│   ├── app.py       # Główna aplikacja Flask
│   ├── quiz_main.py # Logika quizu
│   ├── processing.py # Przetwarzanie plików
│   ├── parsers/     # Parsery dla różnych formatów
│   └── requirements.txt
├── Frontend/         # Aplikacja frontend (HTML/CSS/JS)
│   └── index.html
├── DEPLOYMENT.md     # Instrukcje wdrożenia
└── README.md

```

## 🚀 Szybki start

### Lokalnie

#### Backend
```bash
cd Backend
pip install -r requirements.txt
python app.py
```

Backend będzie dostępny na: `http://localhost:5003`

#### Frontend
Po prostu otwórz `Frontend/index.html` w przeglądarce.

### Wdrożenie

Szczegółowe instrukcje wdrażania na **Render.com** (backend) i **Vercel** (frontend) znajdziesz w pliku [DEPLOYMENT.md](./DEPLOYMENT.md).

## 🔑 Konfiguracja klucza API

1. Otwórz aplikację w przeglądarce
2. Na ekranie głównym wprowadź swój klucz API OpenAI
3. Kliknij "Zapisz klucz API"
4. Klucz jest bezpiecznie przechowywany w sessionStorage przeglądarki

## 📖 Jak używać

1. **Wprowadź klucz API**: Najpierw wprowadź swój klucz API OpenAI
2. **Sprawdź dane**: Sprawdź czy są już jakieś dane w systemie
3. **Prześlij pliki**: Prześlij pliki z materiałami (PDF, DOCX, CSV, TXT)
4. **Przetwórz**: Automatycznie przetwarzaj pliki
5. **Zacznij quiz**: Rozpocznij quiz na podstawie przesłanych materiałów

## 🛠️ Technologie

### Backend
- Flask
- OpenAI API
- Flask-CORS
- PyPDF2, python-docx
- Gunicorn (produkcja)

### Frontend
- Vanilla JavaScript
- HTML5/CSS3
- Fetch API

## 📝 Format pytania

Każde pytanie zawiera:
- Pytanie tekstowe
- 4 odpowiedzi (A, B, C, D)
- Poprawną odpowiedź

## 🔒 Bezpieczeństwo

- Klucz API OpenAI jest przechowywany tylko w sessionStorage użytkownika
- Nigdy nie jest wysyłany na serwer bez zgody użytkownika
- Wszystkie połączenia w produkcji używają HTTPS
- CORS jest skonfigurowany z whitelistą domen

## 📄 Licencja

Ten projekt jest dostępny jako przykład edukacyjny.

## 🤝 Wsparcie

W razie problemów sprawdź [DEPLOYMENT.md](./DEPLOYMENT.md) lub otwórz issue w repozytorium.
