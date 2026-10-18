# Etap B — mikro-zadania do wysyłania lekkim LLM, jeden packet na turę

**Warunek:** Najpierw przeczytać [STAGE_B_WEAK_LLM_RUNBOOK](STAGE_B_WEAK_LLM_RUNBOOK.md) i [SOURCE_REGISTER](SOURCE_REGISTER.md). Te pakiety nie są poleceniem budowy gry ani uruchamiania Unreal/Roblox. Nie potrzebują tysięcy tokenów kontekstu jednocześnie.

## P0: Inwentaryzacja i blokady (B0)
**CZYTAJ:** docs/README.md, docs/art/STAGE_B_README.md, docs/world/STAGE_A_README.md.  
**ZRÓB:** wypisz listę plików, stan A/PARTIAL, listę pustych lub niedostępnych referencji; nie twórz kopii GDD.  
**ZAPISZ:** tylko docs/art/STAGE_B_README.md (jeśli brak aktualnej informacji).  
**TEST:** 7 stref / 41 ID / N07 OPEN; liczniki spójne.  
**STOP:** jeśli repo/branch nieosiągalne; nie zgaduj zawartości.

## P1: Ujednolić trzy style (B1)
**CZYTAJ:** docs/art/STYLE_VARIANTS.md, docs/art/ART_BIBLE.md, docs/art/SOURCE_REGISTER.md (L01,L06).  
**ZRÓB:** różnice S1/S2/S3; 2 kamery LOCK-C01-A/LOCK-N01-A, bez zmiany prawdziwej geometrii.  
**ZAPISZ:** wyłącznie docs/art/STYLE_VARIANTS.md.  
**TEST:** są dokładnie 3 style, 2 sceny, 6 kombinacji, 5 kryteriów i 100% wag. Nie wpisuj wyniku bez renderów.  
**STOP:** jeśli brak źródeł C01/N01, przenieś do UNKNOWN zamiast projektować z pamięci.

## P2: Prompty do sześciu obrazów (B1)
**CZYTAJ:** docs/art/CONCEPT_PROMPT_LIBRARY.md i STYLE_VARIANTS.md.  
**ZRÓB:** przygotuj 6 pełnych promptów, 2 wspólne locki, global negative, pliki nazwane V02/V05 × S1–S3.  
**ZAPISZ:** tylko docs/art/CONCEPT_PROMPT_LIBRARY.md.  
**TEST:** style porównywalne; brak cudzych logo i palmiarni.
**OUTPUT:** przy braku narzędzia: PROMPT_READY_IMAGE_NOT_GENERATED; przy realnych wynikach: pliki i manifest w concepts/README.md.

## P3: Dzielnice 1–4 (B2)
**CZYTAJ:** docs/art/DISTRICT_LOOKDEV.md, docs/world/DISTRICTS_MASTERPLAN.md, docs/world/atlas/MUCHAWKA_FEATURE.md.
**ZRÓB:** przejrzyj Jackowo, Ogrody, Kolejowo, Muchawkę. Każda: 3 cechy REAL, FANTASY, paleta, nawierzchnie, zieleń, dzień/noc, minigra, ochrona i kadry.  
**ZAPISZ:** wyłącznie docs/art/DISTRICT_LOOKDEV.md.  
**TEST:** N01≠S02 i wszystkie MW-01…MW-06 obecne.

## P4: Dzielnice 5–7 (B2)
**CZYTAJ:** DISTRICT_LOOKDEV, atlas/SPORT_CARDS, atlas/NATURE_CARDS, atlas/CONSERVATION_AND_RESPECT.  
**ZRÓB:** sport, kultura, Sekuła lato/zima.  
**ZAPISZ:** tylko DISTRICT_LOOKDEV.md.  
**TEST:** S01≠S03; biegówki≠zjazdówki; N07 OPEN; bez monet na grobach/pomnikach.

## P5: Postacie i pojazdy (B3)
**CZYTAJ:** CHARACTER_AND_VEHICLES.md, ART_BIBLE.md.  
**ZRÓB:** 5+ NPC, 7 środków transportu i rodziny miejskich propów; cecha sylwetki, materiał, wariant koloru, interakcja, uproszczenie z daleka.  
**ZAPISZ:** CHARACTER_AND_VEHICLES.md.  
**TEST:** żadnych znaków firm/klubów, żadnego kopiowania Mario/GTA; to dokument, a nie model FBX.

## P6: Trzy światła (B4)
**CZYTAJ:** LIGHTING_LOOKDEV.md, SOURCE_REGISTER.md (R01–R04).  
**ZRÓB:** L1 dzień, L2 golden, L3 noc przy jednej nieruchomej kamerze C01; dopisz Sekuła lato/zima, Muchawka.  
**ZAPISZ:** LIGHTING_LOOKDEV.md.  
**TEST:** LightingStyle Soft/Realistic; nie pisać Lighting.Technology=Future jako aktualnej konfiguracji; nie twierdzić FPS. 

## P7: Dwadzieścia trzy karty (B5)
**CZYTAJ:** SHOT_CARDS_V01_V23.md, CONCEPT_SHOTS.md i SOURCE_REGISTER.md.  
**ZRÓB:** dla przydzielonych **maksimum 4 ID na jedną turę** rozbuduj realne cechy, kamerę, fantazję, wyjście i negatywny prompt.  
**ZAPISZ:** tylko SHOT_CARDS_V01_V23.md.  
**TEST:** zachowaj V01–V23, 23 unikatowe ID; V13 BLOCKED; V09 PC+mobile; V11 biegówki; V15 basen; V23 noc.

## P8: Moduły i mobile (B6/B7)
**CZYTAJ:** MODULAR_ASSET_GUIDE.md i UI_VISUAL_GUIDE.md, SOURCE_REGISTER R05–R17.  
**ZRÓB:** kit z modularnym eksportem i realistyczne mockupy PC/mobile/safe area; każda liczba techniczna oparta na źródle lub oznaczona HIPOTEZA.  
**ZAPISZ:** najpierw MODULAR_ASSET_GUIDE.md, potem osobno UI_VISUAL_GUIDE.md.  
**TEST:** 20k triangles to limit **na mesh**; normal map OpenGL; brak magicznych wartości FPS i tekstur; UI dla joysticka.

## P9: QA oraz Draft PR (B8)
**CZYTAJ:** VISUAL_REVIEW.md, STAGE_B_README.md, aktualny diff branch/main.  
**ZRÓB:** link checker, 7 stref, 23 IDs, 6 promptów, brak zmian gry, źródła i prawa, niezatwierdzone statusy; raport PASS/FAIL/BLOCKED.  
**ZAPISZ:** VISUAL_REVIEW.md, potem STAGE_B_README.md i indeks docs/README.md.  
**TEST:** żadna zmiana poza docs/, Stage A PARTIAL, B NOT PASS.  
**OUTPUT:** Draft PR do main i HEAD SHA. Bez auto-merge, bez losowych JSON-ów.

## Szablon wyników jednego packetu
~~~text
PACKET_ID: P?
BRANCH:
INPUTS_READ:
OUTPUT_PATH:
CHANGES_MADE:
SOURCE_IDS_USED:
FACTS_VS_FANTASY_CHECK:
IMAGES_CREATED: 0 (or exact files)
GATES_RUN:
PASS/FAIL/BLOCKED:
NEXT_PACKET:
HEAD_SHA:
~~~

**Nie ma raportu bez weryfikacji w repo.** Przy braku uprawnień wpisz BLOCKED_REMOTE_WRITE, nie wypisuj zmyślonego commita.
