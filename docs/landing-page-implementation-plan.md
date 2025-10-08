# Plan wdrożenia landing page Schowane.pl

## Założenia ogólne
- Stack: Flask, Jinja2, statyczne pliki CSS/JS, opcjonalnie HTMX/Alpine przez CDN.
- Struktura aplikacji: pojedyncza blueprunt/route `landing` renderująca szablon Jinja z osadzonym HTML.
- Stylowanie: czysty CSS w katalogu `static/css/landing.css`; brak kompilacji.
- Obrazy i ikony osadzane w `static/img/landing/` oraz `static/icons/landing/`.
- Testy wizualne manualne w przeglądarce + podstawowe testy Flask (status 200, obecność kluczowych sekcji w HTML).

## Plan iteracyjny (kolejne PR)

### PR 1: Struktura projektu i fundamenty
- [ ] Utworzenie blueprintu/route `landing` w Flasku, rejestracja w aplikacji.
- [ ] Przygotowanie bazowego szablonu `templates/landing/base.html` z blokami `head_assets`, `body`.
- [ ] Dodanie plików statycznych: `static/css/landing.css` (szkielet, zmienne kolorów, reset), `static/js/landing.js` (placeholder na interakcje), katalogów na obrazy i ikony.
- [ ] Konfiguracja podstawowych metatagów (title, description, og tags) w bazowym szablonie.
- [ ] Dodanie testu Flask (np. w `tests/test_landing.py`) sprawdzającego, że `/landing` zwraca 200.
- [ ] Aktualizacja README/ dokumentacji uruchomienia jeśli trzeba.

### PR 2: Nawigacja i sekcja Hero
- [ ] Implementacja sekcji `<header>` i sticky navbaru (logo, linki: Jak to działa, Korzyści, Cennik, FAQ, CTA "Zarezerwuj").
- [ ] Sekcja Hero: nagłówek, podnagłówek, dwa przyciski CTA, social proof liczbowy.
- [ ] Osadzenie docelowego obrazu tła (rzeczywiste zdjęcie lub grafika wygenerowana wg promptu). Tymczasowy placeholder znajduje się w `static/img/landing/image-placeholder.txt` i należy go podmienić finalnym plikiem graficznym.
- [ ] Dodanie stylów responsywnych dla hero i navbaru (flex/grid, sticky effect, CTA hover).
- [ ] Rozszerzenie testu sprawdzającego obecność linków w HTML (np. `Jak to działa`).

### PR 3: Sekcja Partnerzy / Social Proof + Korzyści
- [ ] Sekcja partnerów: lista logotypów / placeholderów w formie ikon, stylowanie w siatce.
- [ ] Sekcja korzyści (4 kafelki): ikony z `static/icons/landing/*.svg`, nagłówki, opisy zgodne z copy.
- [ ] Upewnienie się, że ikony są dostępne (alt/aria-hidden) i responsywne.
- [ ] Dodanie animacji prostych (np. hover) opcjonalnie.
- [ ] Rozszerzenie CSS o layout dla sekcji w dwóch rzędach (desktop) i pojedynczej kolumnie (mobile).

### PR 4: Jak to działa + Cennik
- [ ] Stworzenie sekcji procesu w 3 krokach z ikonami oraz opisami.
- [ ] Sekcja pricing z trzema kartami (Mały sprzęt, Standard, Premium), wyróżnienie środkowego pakietu.
- [ ] Dodanie CTA "Zarezerwuj"/"Zapytaj o ofertę" w kartach z obsługą klawiaturą.
- [ ] Stylowanie kart (shadow, border-radius, responsywna siatka).
- [ ] Aktualizacja testów: sprawdzenie obecności nagłówków "Jak to działa" oraz "Cennik".

### PR 5: Referencje, FAQ, CTA końcowe
- [ ] Implementacja sekcji z opiniami (2-3 cytaty z ikoną gwiazdek), stylowanie kart.
- [ ] Sekcja FAQ (accordion bez JS lub prosty HTMX/JS do rozkładania odpowiedzi).
- [ ] Główna sekcja CTA z wyróżnionym tłem, dużym hasłem i przyciskiem kierującym do formularza.
- [ ] Rozważenie dodania `scroll-behavior: smooth` dla całej strony.
- [ ] Testy: sprawdzenie, że CTA końcowe istnieje w dokumencie.

### PR 6: Stopka, dostępność, finalne szlify
- [ ] Stopka z logo, danymi kontaktowymi, linkami prawnymi, ikonami social media, formularzem newslettera.
- [ ] Dodanie walidacji formularza newslettera prostym JS (sprawdzenie formatu e-mail, komunikat błędu).
- [ ] Globalne poprawki responsywności (media queries dla tablet/mobile), spacing, typografia.
- [ ] Audyt dostępności: kontrasty, aria-labels dla ikon, focus states.
- [ ] Uzupełnienie dokumentacji w `docs/` (np. finalny opis sekcji, instrukcja generowania grafik).
- [ ] Rozszerzenie testów e2e (np. Flask test sprawdzający obecność fragmentu stopki).

### PR 7: Kontent i optymalizacja (opcjonalny finał)
- [ ] Aktualizacja treści copy na podstawie feedbacku (jeśli zajdzie potrzeba).
- [ ] Optymalizacja obrazów (kompresja, `loading="lazy"`), dopisanie `srcset` dla hero.
- [ ] Dodanie prostego logowania zdarzeń (np. `htmx` request do zapisania CTA click) jeżeli wymagane przez biznes.
- [ ] Finalne QA (manualne checki, Lighthouse offline), zebranie screenshotów.
- [ ] Podsumowanie zmian w changelogu/README.

## Dodatkowe notatki
- Ikony i grafiki generować zgodnie z promptami z `docs/landing-page-plan.md` i zapisać w repo (jeśli dostępne narzędzia) lub pozostawić placeholdery z opisem.
- Każdy PR powinien aktualizować snapshot HTML (jeśli korzystamy z testów opartych na `BeautifulSoup`) oraz upewnić się, że stylizacja nie łamie layoutu mobilnego (<768px).
- Przygotować prosty skrypt `flask run --debug` w README dla szybkiego podglądu.
- Zachować spójność nazewnictwa klas CSS (`landing-...`).

