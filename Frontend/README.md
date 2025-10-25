# Aplikacja Quiz - Frontend

## Opis
Nowoczesny frontend dla aplikacji quizowej, który umożliwia zarządzanie danymi i tworzenie quizów na podstawie przesłanych materiałów.

## Funkcjonalności

### 1. Zarządzanie danymi
- **Sprawdzanie statusu danych** - wyświetla aktualną zawartość pliku `data.txt`
- **Podgląd danych** - możliwość przeczytania wszystkich danych przed podjęciem decyzji
- **Zachowanie danych** - opcja zachowania istniejących danych
- **Usuwanie danych** - opcja usunięcia wszystkich danych przed dodaniem nowych

### 2. Przesyłanie plików
- **Obsługiwane formaty**: PDF, DOCX, CSV, TXT
- **Drag & Drop** - przeciągnij i upuść pliki
- **Walidacja plików** - sprawdzanie poprawności formatu
- **Automatyczne przetwarzanie** - po przesłaniu plik jest automatycznie przetwarzany

### 3. System quizu
- **Dynamiczne pytania** - pytania generowane na podstawie przesłanych materiałów
- **Wybór odpowiedzi** - kliknięcie lub skróty klawiszowe (A, B, C, D)
- **Natychmiastowy feedback** - pokazuje poprawną odpowiedź po wyborze
- **Śledzenie wyniku** - aktualizacja wyniku w czasie rzeczywistym
- **Statystyki końcowe** - podsumowanie wyników z oceną

## Instrukcja użytkowania

### Krok 1: Sprawdzenie danych
1. Otwórz aplikację w przeglądarce
2. Kliknij "Sprawdź dane"
3. Zobacz aktualną zawartość bazy danych
4. Zdecyduj czy zachować istniejące dane czy je usunąć

### Krok 2: Przesyłanie plików
1. Kliknij "Prześlij pliki"
2. Przeciągnij plik do obszaru upload lub kliknij aby wybrać
3. Plik zostanie automatycznie przesłany i przetworzony
4. Po przetworzeniu możesz:
   - Rozpocząć quiz
   - Przesłać kolejny plik

### Krok 3: Rozpoczęcie quizu
1. Po przesłaniu i przetworzeniu plików kliknij "Rozpocznij quiz"
2. Odpowiadaj na pytania klikając odpowiedzi lub używając klawiszy A, B, C, D
3. Zobacz natychmiastowy feedback po każdej odpowiedzi
4. Kontynuuj do końca quizu lub zakończ wcześniej klawiszem Q

### Krok 4: Wyniki
1. Zobacz swój końcowy wynik
2. Otrzymaj ocenę na podstawie procentu poprawnych odpowiedzi
3. Wybierz czy chcesz zagrać ponownie czy wrócić do głównego menu

## Skróty klawiszowe
- **A, B, C, D** - wybór odpowiedzi w quizie
- **Q** - zakończenie quizu

## Wymagania techniczne
- Nowoczesna przeglądarka internetowa (Chrome, Firefox, Safari, Edge)
- Backend aplikacji uruchomiony na porcie 5003
- Połączenie internetowe dla komunikacji z API

## Struktura plików
```
Frontend/
├── index.html          # Główny plik aplikacji
└── README.md           # Ten plik
```

## API Endpoints
Aplikacja komunikuje się z backendem przez następujące endpointy:
- `GET /quiz/processing` - sprawdzenie statusu danych
- `POST /quiz/processing` - decyzja o zachowaniu/usunięciu danych
- `POST /quiz/upload` - przesyłanie plików
- `POST /quiz/write_data` - zapisywanie danych z pliku
- `DELETE /quiz/delete_upload_file` - usuwanie pliku z upload
- `GET /quiz/start` - rozpoczęcie quizu
- `GET /quiz/question` - pobranie pytania
- `POST /quiz/answer` - wysłanie odpowiedzi
- `GET /quiz/result` - pobranie aktualnego wyniku

## Rozwiązywanie problemów

### Backend nie odpowiada
- Sprawdź czy backend jest uruchomiony na porcie 5003
- Sprawdź połączenie internetowe
- Sprawdź czy nie ma blokady przez firewall

### Pliki nie są przesyłane
- Sprawdź czy format pliku jest obsługiwany (PDF, DOCX, CSV, TXT)
- Sprawdź czy plik nie jest uszkodzony
- Sprawdź czy backend ma dostęp do folderu upload

### Quiz nie działa
- Sprawdź czy dane zostały poprawnie przetworzone
- Sprawdź czy plik data.txt zawiera treść
- Sprawdź czy backend ma dostęp do OpenAI API

## Wsparcie
W przypadku problemów sprawdź:
1. Logi backendu w konsoli
2. Konsolę przeglądarki (F12)
3. Połączenie sieciowe
4. Poprawność konfiguracji API
