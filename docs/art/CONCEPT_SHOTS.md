# MathCity — briefs wizualizacji (research, nie assety produkcyjne)

**Status:** 2026-10-18. Ten plik opisuje koncepcje i kryteria akceptacji kadrów. Nie opisuje działających poziomów.

W rozmowie koncepcyjnej powstał panoramiczny **render poglądowy** przedstawiający bajkowe, nadwodne miasto o zachodzie słońca: wieżę zegarową, park, stadion, dworzec, estakady, mosty, fontanny, portale liczbowe i postaci w ruchu. Jest to **moodboard fantasy**, nie wierne zdjęcie Siedlec, nie gotowy układ miasta i nie import UE/Roblox. Plik binarny renderu z rozmowy nie został dołączony do tego commita; w dokumentacji repo pozostają jego opis, paleta oraz własny schemat SVG. Obecne ilustracje: [assets/math_city_concept.jpg](../../assets/math_city_concept.jpg) oraz [assets/math_city_doors.jpg](../../assets/math_city_doors.jpg) (wcześniejsze zasoby, do osobnego przeglądu).

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
