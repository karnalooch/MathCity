# B1 — Style S1/S2/S3 i uczciwy test porównawczy

## Obrazkowe porównania S1/S2/S3

![Trzy style sylwetki C01, ta sama bryła](concepts/REF03_C01_STYLE_TRIPTYCH.svg)

![Trzy style N01, ta sama linia brzegu](concepts/REF04_N01_STYLE_TRIPTYCH.svg)

**Status:** 2 oryginalne porównania SVG istnieją, ale sześć docelowych renderów porównawczych jeszcze NIE powstało. Porównuj te referencje z [prawdziwymi cechami L01/L06](SOURCE_REGISTER.md); schemat nie potwierdza geometrii 1:1.

**Status: DOCUMENTED, NOT_RENDERED, NOT_APPROVED.** Siedem stref jest kandydatem (nie zatwierdzonym masterplanem). Trzy style są autorskie, a nie kopiami GTA czy Mario.

## Dwa widoki testowe — ZABLOKUJ geometrię i kadr
- `LOCK-C01-A`: Jacek od strony placu, w perspektywie pieszego dziecka. Wieża, Atlas i pawilony w jednym ujęciu [L01]. Brief kamery: widok na budynek na wysokości oczu awatara, perspektywa 35 mm *umowny ekwiwalent fotografii*, poziom 16:9, słońce za kamerą. Wygeneruj tę SAMĄ kompozycję dla S1, S2, S3.
- `LOCK-N01-A`: Muchawka od plaży, z krawędzią ścieżki w przedplanie, pomostem i dużą taflą wody, naturalną zielenią, bez wysp poświadczanych jako realne [L06]. ZACHOWAJ to samo ustawienie i proporcje we wszystkich trzech stylach.
- Maksymalnie 2–3 postaci dla skali, jedna prosta ikona minigry, ten sam neutralny **dzień** dla pierwszego porównania.
- Nie zmieniaj bryły prawdziwego landmarku. Wolno zmieniać nasycenie, materiały, kształt małej architektury i detal fantasy.
- Jeśli generator tworzy różną geometrię, wpisz `COMPARABILITY_LIMITED` i nie wyliczaj obiektywnego rankingu na podstawie obrazów.

## S1 „Słoneczne Neonowe Siedlce”
Ciepły wakacyjny klimat pastelowego miasta: brzoskwinia `#FCB5A8`, turkus `#5EDACD`, róż `#FF759A` jako AKCENT, matowe fasady, naturalne drzewa i woda. Historyczne proporcje mają pierwszeństwo; duże kolory na elementach pomocniczych.
- Silne strony: lokalna sylwetka, wyraźny miejski klimat.
- Zagrożenia: tropikalne Miami, asfalt jak lustro, nadmiar różu i neonów.
- NEGATIVE: no palm forests, no Miami skyline, no GTA logo, no realistic violence, no chrome streets.

## S2 „Bajkowa przygoda”
Jasne płaszczyzny, łagodne zaokrąglenia, lekko przeskalowane ławki/portale, bardzo czytelne figury matematyczne. Kolory bardziej nasycone niż S1, ale ratusz nadal jest Jackiem, a pałac ma portyk [L01,L02].
- Silne strony: zabawa, szybko rozpoznawalne cele, prostota mobile.
- Zagrożenia: miasto jak przypadkowa zabawkowa makieta.
- NEGATIVE: no Mario character, no Nintendo props, no distorted historical landmarks.

## S3 „MathCity Signature” (PREFEROWANY DO OCENY, NIE ZATWIERDZONY)
Rozpoznawalne historyczne fasady i zieleń Siedlec + pastelowa paleta S1 + czytelność i interakcje S2. Zmienność krajobrazu naturalna (park/woda/las), a kolor fantastyczny stosowany w UI i punktach wyzwania.
- Silne strony: spójność siedmiu stref, promocja Siedlec, możliwa stylizacja w Roblox.
- Zagrożenia: brak dyscypliny stylu przy kolejnych generacjach assetów.
- NEGATIVE: no photoreal UE landscape, no copyrighted characters, no random floating islands above historical monuments.

## Ocena po wygenerowaniu / obejrzeniu

| Kryterium | Waga | S1 | S2 | S3 | Dowód |
|---|---:|---|---|---|---|
| Rozpoznawalność prawdziwych Siedlec | 30% | NOT_TESTED | NOT_TESTED | NOT_TESTED | porównanie C01/N01 z linkami [L01,L06] |
| Czytelność obrazka 360 px | 20% | NOT_TESTED | NOT_TESTED | NOT_TESTED | mała wersja każdego kadru |
| Wiek 8–11 / przyjazność | 20% | NOT_TESTED | NOT_TESTED | NOT_TESTED | recenzja |
| Spójność 7 proponowanych stref | 15% | NOT_TESTED | NOT_TESTED | NOT_TESTED | moodboard siedmiu |
| Wykonalność w Roblox | 15% | NOT_TESTED | NOT_TESTED | NOT_TESTED | analiza R05–R12; później test runtime |

Oblicz wynik 0–100 jako suma(ocena 0..5 / 5 × waga) WYŁĄCZNIE gdy wszystkie pięć kryteriów ma dowód. Jeżeli brakuje obrazów, pola zostają NOT_TESTED, brak wyniku i zwycięzcy. Punktacja jest recenzją projektową, nie zatwierdzeniem ownera.

### Wymagany output
Sześć faktycznie wygenerowanych obrazów **albo** sześć pełnych promptów i status `PROMPT_READY_IMAGE_NOT_GENERATED`. Oznacz tool i datę; nie myl obrazka AI ze screenshotem Roblox. Obrazy opcjonalnie w `docs/art/concepts/` dopiero z prawami do wyników i bez cudzych zdjęć w paczce.

[Sekcja promptów](CONCEPT_PROMPT_LIBRARY.md) • [Źródła](SOURCE_REGISTER.md) • [Bramki](VISUAL_REVIEW.md).
