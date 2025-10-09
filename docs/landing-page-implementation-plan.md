# Plan wdrożenia landing page Schowane.pl

## Założenia ogólne
- Stack: Flask, Jinja2, statyczne pliki CSS/JS, opcjonalnie HTMX/Alpine przez CDN.
- Struktura aplikacji: pojedyncza blueprunt/route `landing` renderująca szablon Jinja z osadzonym HTML.
- Stylowanie: czysty CSS w katalogu `static/css/landing.css`; brak kompilacji.
- Obrazy i ikony osadzane w `static/img/landing/` oraz `static/icons/landing/`.
- Testy wizualne manualne w przeglądarce + podstawowe testy Flask (status 200, obecność kluczowych sekcji w HTML).

## Plan iteracyjny (kolejne PR)

### PR 1: Struktura projektu i fundamenty
- [x] Utworzenie blueprintu/route `landing` w Flasku, rejestracja w aplikacji.
- [x] Przygotowanie bazowego szablonu `templates/landing/base.html` z blokami `head_assets`, `body`.
- [x] Dodanie plików statycznych: `static/css/landing.css` (szkielet, zmienne kolorów, reset), `static/js/landing.js` (placeholder na interakcje), katalogów na obrazy i ikony.
- [x] Konfiguracja podstawowych metatagów (title, description, og tags) w bazowym szablonie.
- [x] Dodanie testu Flask (np. w `tests/test_landing.py`) sprawdzającego, że `/landing` zwraca 200.
- [x] Aktualizacja README/ dokumentacji uruchomienia jeśli trzeba.

### PR 2: Nawigacja i sekcja Hero
- [x] Implementacja sekcji `<header>` i sticky navbaru (logo, linki: Jak to działa, Korzyści, Cennik, FAQ, CTA "Zarezerwuj").
- [x] Sekcja Hero: nagłówek, podnagłówek, dwa przyciski CTA, social proof liczbowy.
- [x] Osadzenie docelowego obrazu tła (rzeczywiste zdjęcie lub grafika wygenerowana wg promptu). Tymczasowy placeholder znajduje się w `static/img/landing/image-placeholder.txt` i należy go podmienić finalnym plikiem graficznym.
- [x] Dodanie stylów responsywnych dla hero i navbaru (flex/grid, sticky effect, CTA hover).
- [x] Rozszerzenie testu sprawdzającego obecność linków w HTML (np. `Jak to działa`).

### PR 3: Sekcja Partnerzy / Social Proof + Korzyści
- [x] Sekcja partnerów: lista logotypów / placeholderów w formie ikon, stylowanie w siatce.
- [x] Sekcja korzyści (4 kafelki): ikony z `static/icons/landing/*.svg`, nagłówki, opisy zgodne z copy.
- [x] Upewnienie się, że ikony są dostępne (alt/aria-hidden) i responsywne.
- [x] Dodanie animacji prostych (np. hover) opcjonalnie.
- [x] Rozszerzenie CSS o layout dla sekcji w dwóch rzędach (desktop) i pojedynczej kolumnie (mobile).

### PR 4: Jak to działa + Cennik
- [x] Stworzenie sekcji procesu w 3 krokach z ikonami oraz opisami.
- [x] Sekcja pricing z trzema kartami (Mały sprzęt, Standard, Premium), wyróżnienie środkowego pakietu.
- [x] Dodanie CTA "Zarezerwuj"/"Zapytaj o ofertę" w kartach z obsługą klawiaturą.
- [x] Stylowanie kart (shadow, border-radius, responsywna siatka).
- [x] Aktualizacja testów: sprawdzenie obecności nagłówków "Jak to działa" oraz "Cennik".

### PR 5: Referencje, FAQ, CTA końcowe
- [x] Implementacja sekcji z opiniami (2-3 cytaty z ikoną gwiazdek), stylowanie kart.
- [x] Sekcja FAQ (accordion bez JS lub prosty HTMX/JS do rozkładania odpowiedzi).
- [x] Główna sekcja CTA z wyróżnionym tłem, dużym hasłem i przyciskiem kierującym do formularza.
- [x] Rozważenie dodania `scroll-behavior: smooth` dla całej strony.
- [x] Testy: sprawdzenie, że CTA końcowe istnieje w dokumencie.

### PR 6: Stopka, dostępność, finalne szlify
- [x] Stopka z logo, danymi kontaktowymi, linkami prawnymi, ikonami social media, formularzem newslettera.
- [x] Dodanie walidacji formularza newslettera prostym JS (sprawdzenie formatu e-mail, komunikat błędu).
- [x] Globalne poprawki responsywności (media queries dla tablet/mobile), spacing, typografia.
- [x] Audyt dostępności: kontrasty, aria-labels dla ikon, focus states.
- [x] Uzupełnienie dokumentacji w `docs/` (np. finalny opis sekcji, instrukcja generowania grafik).
- [x] Rozszerzenie testów e2e (np. Flask test sprawdzający obecność fragmentu stopki).

#### Notatki wdrożeniowe PR 6
- Stopka korzysta z gradientowego tła i siatki 4 kolumn, która skaluje się do układu jednokolumnowego na urządzeniach mobilnych.
- Formularz newslettera waliduje adres e-mail po stronie klienta i prezentuje komunikaty stanu z wykorzystaniem `aria-live`.
- Zaktualizowano globalne style `:focus-visible`, formularzy oraz media queries dla sekcji landing page, aby poprawić kontrast, spacing i dostępność na mniejszych ekranach.
- Test integracyjny Flask weryfikuje obecność sekcji newslettera oraz elementów prawnych w stopce.

### PR 7: Kontent i optymalizacja (opcjonalny finał)
- [x] Aktualizacja treści copy na podstawie feedbacku (jeśli zajdzie potrzeba).
- [x] Optymalizacja obrazów (kompresja, `loading="lazy"`), dopisanie `srcset` dla hero.
- [x] Dodanie prostego logowania zdarzeń (np. `htmx` request do zapisania CTA click) jeżeli wymagane przez biznes.
- [x] Finalne QA (manualne checki, Lighthouse offline), zebranie screenshotów.
- [x] Podsumowanie zmian w changelogu/README.

#### Notatki wdrożeniowe PR 7
- Zastąpiono placeholdery graficzne docelowymi obrazami (logo, hero, kafelki korzyści) wraz z atrybutami `loading="lazy"` i `srcset`.
- Ujednolicono branding na kolorze podstawowym #31A744 oraz zaktualizowano dane kontaktowe, linki prawne i CTA.
- Dodano lekki mechanizm telemetryczny (beacon/fetch) wysyłający zdarzenia CTA do endpointu `/landing/events` logującego dane po stronie serwera.

### PR 8: Odświeżenie wizualne i hero carousel
- [x] Przebudowa sekcji hero pod karuzelę ze slajdami (3 grafiki, lazy-load, sterowanie klawiaturą).
- [x] Redukcja zielonych gradientów na tle na rzecz neutralnych szarości przy zachowaniu brandowych CTA.
- [x] Dodanie placeholders SVG dla brakujących grafik i opisów figcaption zwiększających dostępność.
- [x] Opracowanie lekkiego procesu obsługi zapisów newsletterowych z ręcznym przetwarzaniem (patrz `docs/newsletter-operations.md`).

#### Notatki wdrożeniowe PR 8
- Karuzela działa bez zewnętrznych bibliotek: automatyczne przewijanie co 8 s, sterowanie strzałkami i wskaźnikiem dot.
- Neutralna paleta (#eef1f5/#d9dee6) została zastosowana w gradientach sekcji, co zmniejsza nasycenie zieleni przy zachowaniu kontrastu.
- Dokument operacyjny opisuje codzienną rutynę operatora: eksport logów CTA do CSV i ręczne wysyłanie powitań.

## Dodatkowe notatki
- Ikony i grafiki generować zgodnie z promptami z `docs/landing-page-plan.md` i zapisać w repo (jeśli dostępne narzędzia) lub pozostawić placeholdery z opisem.
- Każdy PR powinien aktualizować snapshot HTML (jeśli korzystamy z testów opartych na `BeautifulSoup`) oraz upewnić się, że stylizacja nie łamie layoutu mobilnego (<768px).
- Przygotować prosty skrypt `flask run --debug` w README dla szybkiego podglądu.
- Zachować spójność nazewnictwa klas CSS (`landing-...`).
- Po wdrożeniu PR7 korzystać z dokumentów: `docs/seo-recommendations.md` (lista priorytetów SEO) oraz `docs/cta-telemetry-guide.md` (instrukcja logowania CTA).

