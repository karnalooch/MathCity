# B8 — protokół QA i bramki wizualne MathCity

**Stan: 2026-10-19.** QA dokumentacji możliwe; bez obrazów/Studio nie wolno zaliczać QA obrazów, FPS ani rozpoznawalności. Używaj PASS / FAIL / BLOCKED / NOT_TESTED, nigdy „wydaje się OK” jako PASS.

## Gate Etapu B

| ID | Wymaganie do PASS | Status na dziś | Dowód albo blokada |
|---|---|---|---|
| BG-01 | Wszystkie dokumenty B0–B8 z linkami | DOCUMENTED | [STAGE_B_README](STAGE_B_README.md), reszta docs/art |
| BG-02 | S1/S2/S3 porównane przy stałym C01 i N01 | NOT_TESTED | tylko [prompty](CONCEPT_PROMPT_LIBRARY.md), 0 obrazów |
| BG-03 | Czytelna sylwetka C01 i N01 | NOT_TESTED | karty z cechami, brak renderów |
| BG-04 | Siedem kandydackich stref opisanych i porównanych | DOCUMENTED / NOT_TESTED | [DISTRICT_LOOKDEV](DISTRICT_LOOKDEV.md), brak obrazów |
| BG-05 | S01 piłka ≠ S03 lekkoatletyka ≠ S02 hala | DOCUMENTED | [źródła L09–L11](SOURCE_REGISTER.md) |
| BG-06 | N05 biegówki ≠ N06 nauka, N07 OPEN, miejsca pamięci chronione | DOCUMENTED | [zasady ochrony](../world/atlas/CONSERVATION_AND_RESPECT.md) |
| BG-07 | L1/L2/L3 to ten sam widok i geometria | NOT_TESTED | [lighting](LIGHTING_LOOKDEV.md), brak renderów |
| BG-08 | 23 karty V01–V23 kompletne | DOCUMENTED | [SHOT_CARDS](SHOT_CARDS_V01_V23.md); same obrazy = 0 |
| BG-09 | NPC / pojazdy rozpoznawalne wizualnie | NOT_TESTED | [specyfikacja](CHARACTER_AND_VEHICLES.md), bez modeli |
| BG-10 | Kit powtarzalnych assetów opisany | DOCUMENTED | [modular](MODULAR_ASSET_GUIDE.md), bez importu |
| BG-11 | UI czytelne na telefonie i bezpiecznym obszarze | NOT_TESTED | [specyfikacja UI](UI_VISUAL_GUIDE.md), brak urządzeniowego testu |
| BG-12 | Co najmniej 10 obrazów głównych, jakość i prawa | BLOCKED | 0 nowych obrazów, generator nieużyty |
| BG-13 | Prawa do realnych zdjęć / assetów sprawdzone | BLOCKED | referencje LINK_ONLY / RIGHTS_UNKNOWN |
| BG-14 | `MathCity.rbxl`, `src` i `assets` nienaruszone | NOT_TESTED | potwierdzić w diff PR: żadnych zmian poza docs |
| BG-15 | Akceptacja właściciela | BLOCKED | właściciel nie zaakceptował S1–S3 i 7 stref |

**Główne kryterium decyzji:** sam komplet dokumentacji to `DOCUMENTED`, nie `STAGE_B_PASS`.

## Tabela oceny sześciu pierwszych obrazów

| Obraz | Siedlce recognizability | Identical camera | Readable 360px | Copyright OK | Owner |
|---|---|---|---|---|---|
| V02_S1 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | PENDING |
| V02_S2 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | PENDING |
| V02_S3 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | PENDING |
| V05_S1 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | PENDING |
| V05_S2 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | PENDING |
| V05_S3 | NOT_TESTED | NOT_TESTED | NOT_TESTED | NOT_TESTED | PENDING |

## Rubryka jednej wizualizacji (0–5, dopiero gdy istnieje)

- Rozpoznawalność prawdziwego punktu (0–5): czy są wszystkie trzy cechy z karty? **0 = inny budynek lub niezgodny obszar**.
- Czytelność na małym ekranie (0–5): czy duże obiekty i cyfry nie zlewają się?
- Spójność kierunku artystycznego (0–5): jedna gra, a nie siedem niezależnych stylów.
- Dziecięcy UX (0–5): zrozumiały cel, brak przytłaczających efektów.
- Realność Roblox (0–5): brak dependence on Nanite/Lumen; opis materiałów i LOD jest planem do późniejszego sprawdzenia.

Dla jakiegokolwiek znaku praw autorskich bez zgody, oszustwa co do pochodzenia obrazu, zmyślenia realnej lokalizacji albo gry na miejscach pamięci: **FAIL niezależnie od sumy**.

## Karta kontrolna recenzenta

~~~text
DATE_UTC:
REVIEWER:
ASSET_OR_SHOT_ID:
FILES_READ:
SOURCE_IDS:
REAL_FACTS_VERIFIED:
FANTASY_DECLARED:
RIGHTS_STATUS:
CAMERA_LOCK_VERIFIED:
IMAGE_OPENED: YES | NO
TOOL_ORIGIN:
PASS_FAIL_BLOCKED_NOT_TESTED:
FINDINGS:
CORRECTION_NEEDED:
OWNER_APPROVAL: PENDING | APPROVED | REJECTED
EVIDENCE_URL:
~~~

## Końcowe testy GitHub (wymagane przed PR)
1. Pobierz diff gałęzi względem aktualnego main i sprawdź **tylko docs/**.
2. Czy wszystkie nowe odnośniki wewnętrzne prowadzą do istniejącego path?
3. Czy 23 IDs bez luki V01–V23? Czy sześć promptów ma poprawne locki?
4. Czy nie skopiowano cudzych zdjęć, logo, modeli ani assetów YACS?
5. Czy status Stage A nadal PARTIAL?
6. Czy Stage B ma statusy uczciwie zaznaczone (0 obrazów to 0 obrazów)?
7. Czy żaden agent nie zmergował zmian bez zatwierdzenia?

### Próby negatywne, na których słabszy agent ma się zatrzymać
- „Górka Grześ na pewno jest tutaj”: STOP / N07 OPEN.
- „Zrób stok zjazdowy na Sekule”: STOP / N05 BIEGOWE.
- „Stadion ma 2901 miejsc i 8 torów basenu”: STOP / pomieszane S01 z S02.
- „Fab z YACS = wszystkie assety bez ograniczeń”: STOP / audit licencji.
- „Wygenerowałem 23 grafiki”, ale brak plików: STOP / status PROMPT_ONLY.
- „Użyłem Lighting.Technology Future, jak w tutorialu 2021”: STOP / aktualny LightingStyle.
