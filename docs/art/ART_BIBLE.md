# MathCity — Art Bible v0.1 (kierunek wizualny)

## Galeria referencji, obowiązkowa przed modelowaniem

**[ZOBACZ 17 plansz SVG](VISUAL_REFERENCE_ATLAS.md)** | [źródła rzeczywistych miejsc](SOURCE_REGISTER.md). To oryginalne **schematy artystyczne**, nie zdjęcia ani rendery gotowej gry.

![Trzy style ratusza Jacek](concepts/REF03_C01_STYLE_TRIPTYCH.svg)

![Trzy style Zalewu Muchawka](concepts/REF04_N01_STYLE_TRIPTYCH.svg)

**Status:** PROPOZYCJA, 2026-10-18. Właściciel wskazał dwie inspiracje: klimat **GTA: Vice City** i przygodową, kolorową czytelność **Super Mario Odyssey**. Powstaje **odrębna autorska estetyka MathCity**, bez przenoszenia czyichkolwiek postaci, map, assetów, logo ani muzyki.

## Krótkie hasło

**Siedlce w promieniach pastelowego zachodu słońca, z błyszczącymi akcentami i lekką, przyjazną geometrią 3D.** Realne zabytki rozpoznawalne w uproszczonych sylwetkach, do tego fantastyczny transport, fontanny, kwiaty, ogrody, neonowe portale i lekkie elementy platformówki.

## Paleta startowa

| Funkcja | Barwa | HEX | Sugerowane zastosowanie |
| --- | --- | --- | --- |
| Ciepła baza | Brzoskwinia | #FCB5A8 | elewacje, zachód słońca |
| Akcent 1 | Neonowy róż | #FF759A | szyldy, portale, nagrody |
| Akcent 2 | Turkus | #5EDACD | dachy, woda, interakcje |
| Niebo / chłód | Błękit | #6684E6 | cienie, duże płaszczyzny |
| Światło | Słoneczny żółty | #FFC865 | drogi, nagrody, oświetlenie |
| Akcent nocny | Fiolet | #7162BB | niebo, noc, magia |

Paleta jest robocza i **nie jest zaimportowanym materiałem w Roblox**. Nie używać samych barw do oznaczania prawidłowych odpowiedzi; potrzebne ikony, tekst i wzory.

## Dwa warianty atmosfery

### „Słoneczne MathCity”

- Przyjemne niebo, rozproszone światło, delikatnie ciepła tonacja.
- Kremowe i pastelowe elewacje, odróżniające się barwnie dzielnice.
- Czytelne sylwetki wieży Jacka, Pałacu Ogińskich i stadionu.
- Krótkie kontrasty, przyjazne cienie, minimalny szum tekstur.

### „MathCity After Dark”

- Granatowo-fioletowe niebo i różowo-turkusowe neony w wybranych miejscach.
- Nie przesadzać z Bloom, kontrastem i migotaniem.
- Ważne zabytki oświetlone jak punkt orientacyjny, ulice bez ostrego stroboskopu.
- Tryb spokojny / ograniczania efektów dla użytkowników wrażliwych.

## Bryły, detale, postaci

- Robloxowy charakter postaci zachowujemy; otoczenie może być bogatsze, ale nie powinno wyglądać jak hiperrealistyczna skórka z UE.
- Duże, czytelne bryły. Okna, gzymsy i balkony modelowane tylko tam, gdzie wpływają na sylwetkę lub bliski kadr.
- Zróżnicowanie elewacji: kit 8–12 modułów ścian, dachów, narożników, okien i drzwi, reużywany w mieście.
- Materiały nie mogą mieć „plastikowego lustra”; roughness i metalness stonowane.
- Zieleniec: drzewa o prostych koronach, kolorowe rabaty, miękkie krzewy, czytelne alejki.
- Palmy tylko jako punktowa fantazja/festiwal, nie jako fikcyjny podstawowy krajobraz Siedlec.
- Szyldy i HUD po polsku; krótkie frazy, wielkie przyciski, dobrze widoczne strefy interakcji.

## Priorytety szczegółowości

1. **L0** sylwetki ikon miasta na panoramie.
2. **L1** bliski spacer wokół ratusza, pałacu, parku, wody.
3. **L2** minigry i elementy, których gracz dotyka.
4. **L3** mniej ważna zabudowa modułowa i tło.

Jeden spójny budżet materiałów oraz atlas / trim sheets dla powtarzalnych elementów. Docelowe liczby zatwierdzić dopiero po benchmarkach Roblox.

## Wytyczne do porównawczych renderów

Dla **tego samego ujęcia** przygotować:
- render bez efektów (kontrola brył);
- dzień;
- golden hour;
- noc;
- wersję Roblox Studio na docelowym ustawieniu jakości;
- w miarę możliwości zbliżony kadr z telefonicznego klienta Roblox.

**Uwaga:** render UE jest tylko wizją, nie dowodem wydajności ani identycznego obrazu w Roblox. Szczegóły produkcji: [pipeline](../tech/CONTENT_PIPELINE.md).

## Referencje i własność intelektualna

Inspiracji z Vice City i Odyssey używamy wyłącznie do opisu parametrów artystycznych (kolor, rytm, czytelność, energia). Nie kopiujemy żadnych chronionych elementów graficznych. Zob. [prawa](../legal/RIGHTS_AND_COMPLIANCE.md).

Opis kadrów: [CONCEPT_SHOTS.md](CONCEPT_SHOTS.md). Schemat masterplanu: [MATHCITY_WORLD_SCHEMATIC.svg](MATHCITY_WORLD_SCHEMATIC.svg).

## Etap A — palety biotopów i sportu (PROPOZYCJA)

- **Sekuła lato:** zielone korony, naturalne brązy i mięta, czytelne żółte znaczniki przygód poza rzeczywistymi strefami pamięci.
- **Sekuła zima:** czyste biele, miękkie cienie błękitne, turkusowe strzałki, realistyczna czytelność leśnych tras narciarstwa biegowego i uproszczony parkour wyłącznie fantasy.
- **Stadion i basen:** jasna architektura ARMS, turkus i brzoskwinia; wewnątrz basenu czytelne 8 torów i ślizgi bez agresywnego bloom, który zakłóca czytanie cyfr.
- **Górka Grześ:** nie projektować finalnego profilu terenu przed potwierdzeniem miejsca; ewentualna bajkowa strefa saneczkowa musi być wyraźnie fikcyjna.

Źródła i kadry: [world/atlas/PHOTO_REFERENCES](../world/atlas/PHOTO_REFERENCES.md), [CONCEPT_SHOTS](CONCEPT_SHOTS.md).


## Etap B — aktualizacja techniczna 2026-10-19 (DOCUMENTED / NOT APPROVED)

Ten plik jest ogólną paletą i zasadami artystycznymi. **Szczegółowym wykonawczym wejściem** są:
- [Stage B README](STAGE_B_README.md), [instrukcja dla słabszego LLM](STAGE_B_WEAK_LLM_RUNBOOK.md) i [mikro-zadania](TASK_PACKETS.md).
- [3 porównywalne style S1–S3](STYLE_VARIANTS.md) dla stałych kadrów ratusza C01 i zalewu N01.
- [7 proponowanych dzielnic](DISTRICT_LOOKDEV.md), [postaci i pojazdy](CHARACTER_AND_VEHICLES.md), [światło L1–L3](LIGHTING_LOOKDEV.md).
- [Katalog 23 szczegółowych kadrów](SHOT_CARDS_V01_V23.md), [pełne prompty](CONCEPT_PROMPT_LIBRARY.md), [UI mobile](UI_VISUAL_GUIDE.md) i [modułowe assety](MODULAR_ASSET_GUIDE.md).
- [Zweryfikowane źródła Roblox i Siedlce](SOURCE_REGISTER.md) oraz [QA](VISUAL_REVIEW.md).

**Krytyczne korekty względem starszych tutoriali:** Roblox `LightingStyle` (Soft/Realistic), a nie poleganie na `Lighting.Technology`; PBR/SurfaceAppearance wymaga sprawdzenia map OpenGL i pojedynczego zestawu UV; 20k trójkątów to limit pojedynczej siatki, a mobilne UI musi szanować bezpieczne obszary i strefy kciuków. Wszystkie liczby wydajności i parametry materiałów to przyszłe wyniki testów, nie obietnice.

**Nie ma jeszcze plików z finalnymi wizualizacjami ani akceptacji wariantu S1/S2/S3.** Render AI/UE nie jest screenshotem Roblox. Etap A pozostaje PARTIAL.
