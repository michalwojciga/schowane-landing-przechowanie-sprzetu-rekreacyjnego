# Instrukcja wykorzystania logowania CTA

Moduł `landing` udostępnia lekki mechanizm telemetryczny pozwalający na
rejestrowanie kliknięć w kluczowe elementy call-to-action (CTA) oraz zapisy do
newslettera. Poniżej opisano sposób jego działania i dalszego wykorzystania.

## Przepływ danych
1. Elementy HTML oznaczone atrybutem `data-landing-track="<nazwa_zdarzenia>"`
   wywołują funkcję `trackLandingEvent` zdefiniowaną w `static/js/landing.js`.
2. Skrypt próbuje wysłać dane przez `navigator.sendBeacon`; w razie potrzeby
   korzysta z `fetch` z ustawionym `keepalive`.
3. Endpoint serwerowy `/landing/events` (zdefiniowany w `app/landing/__init__.py`)
   przyjmuje żądanie POST z ładunkiem JSON i loguje je do loggera
   `app.landing.events`.

## Struktura zdarzenia
```jsonc
{
  "event": "cta-primary-click",
  "detail": {
    "meta": "hero"
  },
  "ts": "2024-05-20T10:33:12.123Z"
}
```
- `event` – wymagana nazwa zdarzenia (string, snake/kebab-case).
- `detail` – opcjonalny obiekt z dodatkowymi informacjami (np. kontekst CTA).
- `ts` – znacznik czasu ISO 8601 generowany w przeglądarce.

## Konfiguracja loggera
Dodaj konfigurację loggera w pliku produkcyjnym (np. `logging.conf` lub w kodzie
aplikacji):
```python
LOGGING = {
    "version": 1,
    "loggers": {
        "app.landing.events": {
            "handlers": ["cta_events"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "handlers": {
        "cta_events": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/landing-cta.log",
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 5,
            "formatter": "json",
        },
    },
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": "%(asctime)s %(event)s %(detail)s %(user_agent)s",
        },
    },
}
```
Dzięki temu każde kliknięcie CTA zostanie zapisane w pliku `logs/landing-cta.log`
we wskazanym formacie JSON.

## Analiza danych
- **Agregacja tygodniowa**: załaduj logi do narzędzia typu BigQuery, Redshift
  lub prostego arkusza kalkulacyjnego. Grupuj po `event` oraz `detail.meta`, aby
  zidentyfikować najskuteczniejsze CTA.
- **Porównania kanałów**: zestawiaj liczbę kliknięć CTA z sesjami z Google
  Analytics / Matomo. Pozwoli to ocenić konwersje dla ruchu płatnego vs
  organicznego.
- **Alerty**: skonfiguruj proste powiadomienia (np. cron + skrypt), które
  poinformują o spadku kliknięć poniżej ustalonego progu.

## Rozszerzenia
- Dodaj nowe atrybuty `data-landing-track` do kampanii marketingowych (np.
  banerów promocyjnych) – mechanizm automatycznie je obsłuży bez zmian w
  backendzie.
- Jeśli wymagane jest przechowywanie danych w bazie, rozszerz endpoint o zapis
  do tabeli `landing_events` (kolumny: `id`, `event`, `detail`, `user_agent`,
  `created_at`).
- Połącz logi CTA z systemem CRM, aby śledzić pełną ścieżkę konwersji.
