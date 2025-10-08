# Schowane.pl Landing Page

## Wymagania

- Python 3.10+
- Virtualenv (opcjonalnie)

## Instalacja

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> **Uwaga:** Repozytorium zawiera lekki fallback `app/lib/flask_stub.py`,
> dzięki któremu testy mogą działać nawet w środowiskach offline bez
> zainstalowanego pakietu Flask. W środowisku produkcyjnym/deweloperskim
> nadal rekomendowane jest zainstalowanie oficjalnego Flask.

## Uruchomienie w trybie deweloperskim

```bash
flask --app app:create_app --debug run
```

Aplikacja będzie dostępna pod adresem `http://127.0.0.1:5000/landing`.

## Testy

```bash
pytest
```

## Dokumentacja dodatkowa

- [`docs/seo-recommendations.md`](docs/seo-recommendations.md) – lista priorytetów
  SEO wraz z kolejnymi krokami optymalizacji po wdrożeniu landing page.
- [`docs/cta-telemetry-guide.md`](docs/cta-telemetry-guide.md) – opis przepływu
  danych, konfiguracji loggera oraz sposobów analizy kliknięć CTA.

## Changelog

### PR7 – Kontent i optymalizacja
- Wprowadzono finalny branding (kolor przewodni #31A744) wraz z aktualizacją stylów i logotypów.
- Podmieniono obrazy sekcji hero i korzyści na docelowe zasoby z atrybutami `loading="lazy"` i `srcset`.
- Dodano lekki mechanizm telemetryczny (`/landing/events`) rejestrujący kliknięcia CTA oraz subskrypcje newslettera.
- Zaktualizowano dane kontaktowe, linki prawne oraz CTA w stopce i sekcji końcowej.
