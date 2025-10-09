# Obsługa zapisów do newslettera (wersja manualna)

## Cel
Zapewnienie lekkiego procesu obsługi zapisów newsletterowych z landing page,
bez konieczności utrzymywania bazy danych czy systemu mailingowego. Zakładamy
kilka nowych zgłoszeń tygodniowo, dlatego zadania może przejąć operator
obsługi klienta.

## Krok 1 – Konfiguracja logów
1. Upewnij się, że w konfiguracji logowania istnieje handler dla loggera
   `app.landing.events` (szczegóły w `docs/cta-telemetry-guide.md`).
2. Dodaj dedykowany plik na subskrypcje, np. `logs/newsletter.log`, z rotacją
   po 1&nbsp;MB i zachowaniem 3 kopii.
3. W formaterze zapisz pola `event`, `detail` i `user_agent`. Zdarzenie
   `newsletter-subscribe` jest wysyłane automatycznie po poprawnym przesłaniu
   formularza.

```python
LOGGING["handlers"]["newsletter"] = {
    "class": "logging.handlers.RotatingFileHandler",
    "filename": "logs/newsletter.log",
    "maxBytes": 1 * 1024 * 1024,
    "backupCount": 3,
    "encoding": "utf-8",
    "formatter": "json",
}
LOGGING["loggers"]["app.landing.events"]["handlers"].append("newsletter")
```

## Krok 2 – Codzienna praca operatora
1. Raz dziennie otwórz plik `logs/newsletter.log` (można użyć `less` lub
   podglądu w panelu hostingu).
2. Odfiltruj wpisy z ostatnich 24 godzin o nazwie zdarzenia
   `newsletter-subscribe`.
3. Skopiuj adresy e-mail do przygotowanego arkusza (Google Sheets / Excel) w
   kolumnach: data, email, status.
4. Wyślij ręczne powitanie z konta `kontakt@schowane.pl` – gotowy szablon
   tekstowy można trzymać w arkuszu.
5. Ustaw status "kontakt wysłany" i opcjonalnie dodaj notatkę o kolejnych
   krokach (np. telefon, follow-up).

## Krok 3 – Tygodniowe porządki
- W piątek usuń z logu przetworzone wpisy (np. przez nadpisanie pliku pustą
  zawartością po zarchiwizowaniu) – zmniejszy to ryzyko duplikatów.
- W arkuszu zastosuj filtr "status ≠ kontakt wysłany", aby łatwo wychwycić
  subskrybentów wymagających reakcji.
- Jeśli subskrypcji będzie więcej niż 10 tygodniowo, rozważ automatyzację:
  prosty skrypt Python może parsować log i wysyłać wiadomości SMTP na dedykowaną
  skrzynkę operatora.

## Dlaczego to rozwiązanie jest bezpieczne
- Brak przechowywania danych w bazie produkcyjnej – logi można szybko usunąć,
  a dostęp do nich ma tylko operator.
- Mechanizm działa nawet w środowisku bez dostępu do zewnętrznych API.
- W dowolnym momencie można rozszerzyć proces o integrację z CRM lub narzędziem
  mailingowym, wykorzystując te same logi jako źródło prawdy.
