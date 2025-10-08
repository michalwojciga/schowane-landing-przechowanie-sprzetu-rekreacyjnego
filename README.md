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
