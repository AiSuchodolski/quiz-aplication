# Instrukcja uruchomienia aplikacji Quiz

## Wymagania
- Python 3.7+
- Zainstalowane pakiety z requirements.txt

## Instalacja zależności

```bash
cd quiz-aplication/Backend
pip install -r requirements.txt
```

## Konfiguracja

1. Utwórz plik `.env` w folderze `Backend` z kluczem OpenAI:
```
OPENAI_API_KEY=twoj_klucz_openai
```

## Uruchomienie

1. Uruchom backend:
```bash
cd quiz-aplication/Backend
python app.py
```

2. Otwórz frontend w przeglądarce:
```
quiz-aplication/Frontend/Quiz Frontend Application.html
```

## Jak używać aplikacji

### 1. Przesyłanie plików
- Kliknij "Prześlij pliki" na stronie głównej
- Przeciągnij pliki do obszaru uploadu lub kliknij aby wybrać
- Obsługiwane formaty: PDF, DOCX, CSV, TXT
- Możesz przesłać wiele plików jednocześnie

### 2. Przetwarzanie danych
- Po przesłaniu plików kliknij "Przetwórz pliki i przygotuj quiz"
- System przetworzy zawartość plików i zapisze w data.txt
- Po przetworzeniu automatycznie przejdziesz do quizu

### 3. Rozpoczęcie quizu
- Quiz rozpocznie się automatycznie po przetworzeniu plików
- Możesz też sprawdzić czy dane są gotowe klikając "Sprawdź czy dane są gotowe"

### 4. Rozwiązywanie quizu
- Odpowiadaj na pytania wybierając A, B, C lub D
- Możesz używać klawiatury (klawisze A, B, C, D)
- Po każdej odpowiedzi zobaczysz czy była poprawna
- Możesz zakończyć quiz w każdej chwili

## Struktura aplikacji

```
quiz-aplication/
├── Backend/
│   ├── app.py                 # Główny serwer Flask
│   ├── quiz_main.py          # Logika quizu
│   ├── parsers/              # Parsery plików
│   │   ├── csv_parser.py
│   │   ├── docx_parser.py
│   │   ├── pdf_txt_parser.py
│   │   └── text_parser.py
│   ├── upload/               # Folder na przesłane pliki
│   ├── data/                 # Folder na przetworzone dane
│   │   └── data.txt
│   └── requirements.txt
└── Frontend/
    └── Quiz Frontend Application.html
```

## API Endpoints

- `GET /` - Strona główna
- `POST /upload` - Przesyłanie plików
- `POST /parse` - Przetwarzanie plików
- `GET /data/status` - Status danych
- `GET /quiz/start` - Rozpoczęcie quizu
- `GET /quiz/question` - Pobranie pytania
- `POST /quiz/answer` - Wysłanie odpowiedzi
- `GET /quiz/result` - Wynik quizu

## Rozwiązywanie problemów

### Backend nie uruchamia się
- Sprawdź czy wszystkie pakiety są zainstalowane
- Sprawdź czy port 5003 jest wolny
- Sprawdź czy masz ustawiony klucz OpenAI

### Błąd podczas przesyłania plików
- Sprawdź czy pliki są w obsługiwanych formatach
- Sprawdź czy pliki nie są zbyt duże
- Sprawdź czy backend jest uruchomiony

### Błąd podczas parsowania
- Sprawdź czy pliki nie są uszkodzone
- Sprawdź czy pliki zawierają tekst (nie są tylko obrazami)
- Sprawdź logi w konsoli backendu

### Quiz nie działa
- Sprawdź czy data.txt został utworzony i zawiera dane
- Sprawdź czy masz ustawiony klucz OpenAI
- Sprawdź czy backend odpowiada na endpointy quizu

