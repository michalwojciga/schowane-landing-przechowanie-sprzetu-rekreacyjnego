# Zalecenia SEO dla landing page Schowane.pl

Poniższa lista obejmuje rekomendacje optymalizacji pod kątem wyszukiwarek,
które można wdrożyć po finalizacji treści i warstwy wizualnej strony.

## Podstawowe metadane
- **Title i description**: utrzymuj długość meta title w przedziale 50–60
  znaków oraz meta description do ~155 znaków. Wpleć główne słowa kluczowe
  takie jak „przechowalnia rzeczy”, „Schowane.pl” i lokalizacja Poradów.
- **Open Graph / Twitter Cards**: dodaj komplet tagów `og:*` oraz `twitter:*`
  z finalną grafiką hero (`static/img/landing/hero-*`). Pozwoli to poprawnie
  prezentować link w mediach społecznościowych.
- **Structured Data**: rozważ wprowadzenie schematu `LocalBusiness` z danymi
  kontaktowymi, godzinami działania i współrzędnymi GPS (83J2+7FC Poradów).

## Słowa kluczowe i treści
- W nagłówkach H1/H2 wykorzystaj frazy „bezpieczna przechowalnia rzeczy” oraz
  „schowki krótkoterminowe” – unikaj keyword stuffing, dbaj o naturalny język.
- Dodaj sekcję FAQ z pytaniami odpowiadającymi na rzeczywiste zapytania
  (np. „Jak zarezerwować schowek w Schowane.pl?”) i zapewnij logiczną
  strukturę H2/H3.
- Zapewnij unikalność copy – nie powielaj opisów z innych materiałów firmowych.

## Wydajność techniczna
- Utrzymuj rozmiary obrazów poniżej 200 kB oraz zapewnij formaty WebP/AVIF
  z fallbackiem JPEG/PNG.
- Skorzystaj z `loading="lazy"` i `decoding="async"` dla obrazów poza
  viewportem oraz ustaw `width/height` w HTML, by uniknąć layout shift.
- Zadbaj o cache statycznych zasobów (nagłówki HTTP, fingerprinting plików).

## Linkowanie i nawigacja
- Dodaj linki wewnętrzne do kluczowych sekcji („Jak to działa”, „Cennik”,
  „FAQ”) oraz linki zewnętrzne do polityki prywatności i regulaminu.
- W stopce uwzględnij dane NAP (nazwa, adres, telefon) w spójnej formie oraz
  link `tel:+48603305030`.

## Monitorowanie i raportowanie
- Regularnie sprawdzaj raporty w Google Search Console (pokrycie, Core Web
  Vitals) oraz śledź indeksację nowych podstron.
- Po wdrożeniu telemetrycznego endpointu CTA zaplanuj automatyczne raporty
  (np. tygodniowe) łączące dane wejściowe z ruchem organicznym.

## Kolejne kroki
- Przed publikacją uruchom Lighthouse (Desktop/Mobile) i utrzymuj wyniki SEO
  oraz Performance powyżej 90 punktów.
- Zapewnij mapę XML sitemap i plik `robots.txt` wskazujący na landing.
- Po wdrożeniu rozważ utworzenie bloga/sekcji aktualności z poradami dot.
  przechowywania rzeczy, aby poszerzać widoczność na long-tail keywords.
