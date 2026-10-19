# MathCity — briefs wizualizacji (research, nie assety produkcyjne)

**Status:** 2026-10-18. Ten plik opisuje koncepcje i kryteria akceptacji kadrów. Nie opisuje działających poziomów.

W rozmowie koncepcyjnej powstał panoramiczny **render poglądowy** przedstawiający bajkowe, nadwodne miasto o zachodzie słońca: wieżę zegarową, park, stadion, dworzec, estakady, mosty, fontanny, portale liczbowe i postaci w ruchu. Jest to **moodboard fantasy**, nie wierne zdjęcie Siedlec, nie gotowy układ miasta i nie import UE/Roblox. Plik binarny renderu z rozmowy nie został dołączony do tego commita; w dokumentacji repo pozostają jego opis, paleta oraz własny schemat SVG. Obecne ilustracje: [assets/math_city_concept.jpg](../../assets/math_city_concept.jpg) oraz [assets/math_city_doors.jpg](../../assets/math_city_doors.jpg) (wcześniejsze zasoby, do osobnego przeglądu).

## Referencje graficzne do V01–V23, dostępne na remote

**[OTWÓRZ GALERIĘ 17 OBRAZÓW](VISUAL_REFERENCE_ATLAS.md)**. To **rzeczywiste pliki SVG** w `docs/art/concepts/` pokazujące m.in. siedem stref, C01, N01, pałac, sport, Sekułę, UI, pojazdy, grę matematyczną i 3 style. Każde V-ID jest przypisane w galerii do obrazka. Są to schematy, a **nie finalne promocyjne rendery**.

![Dwa style porównywane w jednym kadrze: w istocie S1/S2/S3](concepts/REF03_C01_STYLE_TRIPTYCH.svg)

![Jeden duży Zalew, a wyspy tylko fantasy](concepts/REF02_N01_MUCHAWKA_HUB.svg)

## Kadry docelowe do wykonania i zatwierdzenia

| ID | Kadr | Wymagane elementy | Test rozpoznawalności / odrzucenia |
| --- | --- | --- | --- |
| V-01 | Panorama całego MathCity (z lotu ptaka) | siedem proponowanych stref w tym Sekuła; ratusz, park, zalew, stadion, basen, dworzec | nie może wyglądać jak anonimowe Miami |
| V-02 | Plac Ratusza Jacek (dzień) | sylwetka ratusza, fontanna, barwne fasady, gracze | Jacek musi być rozpoznawalny |
| V-03 | Plac Jacka (zachód/noc) | pastelowe niebo i stonowane neony | brak nadmiernego Bloom |
| V-04 | Ogrody Aleksandrii | Pałac Ogińskich, ogród, aleje, geometryczne zagadki | pałac i park nie mogą być wyłącznie dekoracją |
| V-05 | Muchawkowe Wyspy | prawdziwa inspiracja zalewem, promenady, most | fantasy wyspy oznaczone jako fantazja |
| V-06 | Stacja Czasu | dworzec, stylizowany pociąg, czytelne zegary | czytelny przepływ przez perony |
| V-07 | Neonowe Błonia | stadion, tor przeszkód, kolorowe bramy | przestrzeń do ruchu, widoczność celu |
| V-08 | Aleja Kultury | teatr / galeria, zabytki, sekwencje muzyczne | szacunek do obiektów historycznych |
| V-09 | Interfejs dziecka PC i mobile | minimapa, paszport odkrywcy, podpowiedzi | tekst czytelny na telefonie |
| V-10 | Arkusz modularnych budynków | bliskie i dalekie LOD, paleta, tekstury | możliwy import do Roblox |

## Brief generatywny / artystyczny do kadru V-01

Autorskie, stylizowane 3D przedstawienie Siedlec jako ogromnego przyjaznego miasta w grze Roblox. W centrum rozpoznawalny polski ratusz zwany Jackiem, obok historyczne kamienice; w zielonej dzielnicy pałac i ogród; dalej duży zalew, stadion, dworzec, budynki kultury. Pastelowe zachody słońca, ciepła brzoskwinia, róż i turkus, energetyczna kompozycja przygodowej platformówki, fontanny, trasy rowerowe, zbierane kryształy i interaktywne puzzle liczbowe. Kamera wysoka 3/4, wszystkie ważne dzielnice widoczne w jednym logicznym układzie. Lokalna architektura jest czytelna; świat pozostaje pomysłowo przekomponowany. Bez kopiowania logotypów, postaci i konkretnych kadrów z innych gier.

**Negatywne wymagania:** brak przemocy, nadmiernej ilości palm, realistycznego miasta Miami, naruszeń praw do znaków, nieczytelnych portali i wielkich pustych osiedli.

## Deliverables dla każdego kadru

- Nazwa, data, wersja koncepcji, autor/narzędzie.
- Referencje miejsca i prawo do wykorzystania zdjęć.
- Jedno zdanie „co musi rozpoznać mieszkaniec Siedlec”.
- Wersja z ludźmi / bez ludzi i czysty blockout.
- Docelowy wynik **w Roblox**, nie tylko render z UE.
- Akceptacja stylistyki przed modelowaniem.

Na tym etapie nie tworzymy assetów produkcyjnych. Art Bible: [ART_BIBLE.md](ART_BIBLE.md).

## Etap A: rozszerzenie obowiązkowych ujęć referencyjnych

*Powiązanie z [41 kartami](../world/atlas/LANDMARK_CATALOG.md). Wszystkie kadry poniżej to propozycje przygotowania; bez kopiowania zdjęć i bez produkcyjnego importu.*

| ID kadru | Miejsce | Referencja | Co ma być widoczne | Granica |
| --- | --- | --- | --- | --- |
| V-11 | Sekuła zimą | [miasto — biegówki](https://siedlce.pl/aktualnosci/2025/aktualnosci-01-2025/trasy-narciarstwa-biegowego-w-siedlcach/show) | realna atmosfera nart BIEGOWYCH, las, spokojny slalom na fikcyjnej pętli | bez sankcji sportowych w strefach pamięci |
| V-12 | Sekuła latem | [Nadleśnictwo](https://siedlce.warszawa.lasy.gov.pl/oferta-edukacyjna/-/asset_publisher/kCS6/content/obiekty-edukacyjne) | droga i osiem edukacyjnych stacji, las, rowery poza strefami wykluczonymi | nie kopiować tablic bez praw |
| V-13 | Górka Grześ | [tożsamość OPEN](../world/atlas/NATURE_CARDS.md) | ujęcie dopiero po potwierdzeniu dokładnego miejsca | NIE geolokalizować na zgadywanym grzbiecie |
| V-14 | Stadion piłkarski ARMS | [operator](https://arm.siedlce.pl/pl/stadion-glowny) | trybuna, murawa, plac sportowy | nie pomylić z Prusa 6 |
| V-15 | Park Wodny | [operator](https://arm.siedlce.pl/pl/hala-basenowa) | zewnętrzny obiekt i wnętrze 8 torów, zjeżdżalnie 48/78m | zdjęcia wnętrza tylko z prawami i bez ujawniania dzieci |
| V-16 | Stadion lekkoatletyczny | [Prusa 6](https://arm.siedlce.pl/pl/stadion-lekkoatletyczny) | bieżnia, skateplaza, parkour | odrębny obiekt od S01 |
| V-17 | „Zielone Siedlce” | [oficjalny szlak](https://turystyka.siedlce.pl/31-siedlce-zielone-siedlce) | logiczna zielona oś Muchawka–Sekuła–Błonia | miejska trasa realna 13,1km ≠ długość trasy gry |

Celem konceptu nie jest zmyślanie ani uznawanie grafiki AI za fotografię Siedlec. Autentyczna sylwetka + autorska stylizacja są oceniane osobno.

## Zalew Muchawka: szczegółowe wymagania kadrowania (2026-10-19)

**Pełna karta** [MUCHAWKA_FEATURE.md](../world/atlas/MUCHAWKA_FEATURE.md) z checklistą `MU-F01…MU-F10`. **Zadanie artystyczne dla wykonawcy:** trzy porównywalne koncepcje Zalewu: autentyczna sylwetka realnego kąpieliska, fantastyczna przestrzeń wodna z wyspami, wariant sportowo-rowerowy. Nie przedstawiać wysp jako prawdziwej geografii.

| ID | Kadr | Wymagana zawartość | Co oznaczyć jako fikcję |
| --- | --- | --- | --- |
| V-18 | Panorama całej strefy Zalewu | duża tafla wody, brzeg, plaża, grobla w osobnym planie | baśniowe wyspy, nietypowe mosty |
| V-19 | Plażowy Hub (perspektywa dziecka) | pomost, rodzinna strefa rekreacyjna, rowery, znaki minigier | sklepy i interaktywni NPC |
| V-20 | Wirtualny Cross i Triathlon | trzy czytelne aktywności w bezpiecznej przestrzeni fantasy | dystanse, trasy, pływanie i sportowy tor gry |
| V-21 | Wyspy Ułamków | 3/4, 1/2 na czytelnych obiektach w wodzie, bez ściany tekstu | wyspy i skarby w całości fikcyjne |
| V-22 | Ekoobserwator | tablica z widokiem na przyrodę, bez wejścia w chronione miejsce | ilość i typ rysunkowych zwierząt |
| V-23 | Muchawka nocą | zachód i nocna panorama, ciepłe pastelowe światła na promenadzie | świecące fantasy platformy |

**Weryfikacja:** autor/agent musi podać źródło realnych elementów, listę celowo wymyślonych elementów oraz narzędzie generowania. Nie tworzyć złudzenia, że render UE / AI jest zdjęciem Siedlec lub dowodem wydajności Roblox. Status: `CONCEPT_BRIEFS_CREATED`, żaden finalny render nie został przygotowany przez ten commit.


## Etap B: pełne karty, workflow renderów i status (2026-10-19)

**Nowe nadrzędne instrukcje do realizacji ujęć:** [SHOT_CARDS_V01_V23.md](SHOT_CARDS_V01_V23.md) opisuje komplet **23** kart, a [CONCEPT_PROMPT_LIBRARY.md](CONCEPT_PROMPT_LIBRARY.md) zawiera gotowe, kontrolowane prompty do porównań C01 i N01 dla S1/S2/S3, lighting L1/L2/L3 oraz UI. [SOURCE_REGISTER.md](SOURCE_REGISTER.md) przechowuje referencje źródłowe L01–L14 i R01–R17. [Wykonawczy runbook dla słabszego LLM](STAGE_B_WEAK_LLM_RUNBOOK.md) określa limity kontekstu i testy.

**Kolejność:** (1) sześć porównawczych obrazów V02/V05 × S1/S2/S3 lub samych promptów, gdy brak generatora, (2) podstawowy V01–V10, (3) ujęcia Sekuły i sportu V11,V12,V14,V15 oraz Muchawki V18,V19,V23, (4) pozostałe V17,V20–V22, (5) V13 pozostaje BLOCKED_GEOLOCATION do potwierdzenia Górki Grześ. Identyczne porównanie = ta sama kamera i pora, nie tylko podobny pomysł.

**Stan 2026-10-19:** 23 karty opisowe, 6 gotowych promptów porównawczych, **17 oryginalnych obrazów pomocniczych SVG**, **0 finalnych renderów, 0 screenshotów Roblox**, status `PROMPT_READY_IMAGE_NOT_GENERATED` dla wizualizacji. Nie oznaczać renderów jako ukończonych na podstawie samej dokumentacji. [Manifest planowanych konceptów](concepts/README.md) i [B8 Review](VISUAL_REVIEW.md).
