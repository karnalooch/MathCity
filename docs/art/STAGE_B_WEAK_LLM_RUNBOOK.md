# ETAP B — instrukcja wykonawcza dla LEKKIEGO LLM (v1.0, 2026-10-19)

**Projekt:** karnalooch/MathCity. **Zadanie:** B0–B8 Art Bible, styl, lookdev i plan koncepcji Roblox, NIE kodowanie gry. Etap A ma 41 POI, 40 kandydatów minigier, 7 proponowanych stref, stan A = PARTIAL. **Nie wolno zamienić PARTIAL na PASS.**

> **Ważne:** zacznij od TEGO pliku. Wybierz potem tylko jedno [mikro-zadanie](TASK_PACKETS.md), a nie całą listę. Zapisuj wyniki na gałęzi dokumentacyjnej. Model bez generatora obrazów tworzy rzeczywiście **prompty**, nie obrazy.

## PIERWSZY OBOWIĄZKOWY KROK: ZOBACZ OBRAZY REFERENCYJNE

W repo jest już **17 oryginalnych plansz SVG**, patrz **[VISUAL_REFERENCE_ATLAS.md](VISUAL_REFERENCE_ATLAS.md)**. Nie są one zdjęciami prawdziwych miejsc ani finalnymi renderami. Zanim napiszesz prompt, kartę kadru czy opis bryły:

1. Otwórz **właściwy SVG** i odczytaj jego kształty, paletę i adnotacje.
2. Zmapuj V-ID do pliku w galerii. Dla C01 otwórz [REF01](concepts/REF01_C01_JACEK_SILHOUETTE.svg), dla N01 [REF02](concepts/REF02_N01_MUCHAWKA_HUB.svg), dla siedmiu stref [REF00](concepts/REF00_WORLD_7_ZONES.svg), a do stylów S1–S3 [REF03](concepts/REF03_C01_STYLE_TRIPTYCH.svg) i [REF04](concepts/REF04_N01_STYLE_TRIPTYCH.svg).
3. Porównaj REAL z instytucjonalnymi źródłami Lxx. SVG może być artystycznie nieprecyzyjny, nigdy nie poprawia źródła.
4. Jeśli nie możesz wizualnie obejrzeć SVG, wpisz `REFERENCE_IMAGE_NOT_INSPECTED`. **Nie udawaj, że obejrzałeś obraz.**
5. Dla Kolejowa [REF14](concepts/REF14_T01_KOLEJOWO_REFERENCE_OPEN.svg) jest kompozycją, nie fotoreferencją dworca. Dla N07 Górka Grześ nadal `BLOCKED_GEOLOCATION`; nie ma wiernego renderu.
6. Jeżeli wykonujesz docelowy render PNG, ma on własny plik i manifest, a **SVG_CONCEPT_GUIDE ≠ RENDERED_CONCEPT**.

Podręczna mapa dla agenta: **B1:** REF03+REF04; **B2:** REF00,REF01,REF02,REF06,REF07,REF08,REF14,REF15; **B3:** REF11; **B4:** REF05; **B5:** REF09,REF13,REF16 i [karty](SHOT_CARDS_V01_V23.md); **B6:** REF10; **B7:** REF12; **B8:** [manifest](concepts/README.md) + [QA](VISUAL_REVIEW.md).

## 1. Kontrakt celu

Gra ma być wielką, przyjazną, rozpoznawalną, ale **fikcyjnie przekomponowaną** wersją Siedlec z matematyką klas 2–4, przeznaczoną do działania w Roblox. Inspirowana letnim retro-miastem Vice City i energią kolorowej platformówki 3D, **bez kopii GTA/Mario**. Narzędzia UE, Blender i Material Forge z YACS mogą pomagać w przyszłej produkcji, ale nie stanowią silnika gry.

**Kluczowe priorytety, których nie wolno pominąć:**
- Ratusz Jacek C01, Pałac Ogińskich C02, Park Aleksandria C03/C04.
- N01 Zalew Muchawka jako FLAGOWA przestrzeń, nie dekoracyjna kałuża; N01 **nie jest** halą basenową S02.
- N04 Sekuła, N05 **narciarstwo BIEGOWE**, N06 ścieżka edukacyjna; N07 Górka Grześ bez potwierdzonej lokalizacji.
- S01 stadion PIŁKARSKI i S03 stadion LEKKOATLETYCZNY są różne; S02 Park Wodny to osobny obiekt.
- D7 Sekuła to siódma PROPONOWANA strefa, a nie zatwierdzona zmiana masterplanu.
- Miejsca pamięci, świątynie i chroniona Dolina Muchawki: brak wyścigów, monet, zabaw naruszających ich charakter.

## 2. Zakaz nadpisania

**Nigdy nie zmieniaj:** `MathCity.rbxl`, plików `src/**`, `assets/**`, konfiguracji publikacji Roblox, danych graczy, plików projektów UE/Blender/YACS, plików licencjonowanych assetów. Nie instaluj pluginów ani nie pobieraj do repo cudzych zdjęć bez praw.

**Wolno zmieniać:** wyłącznie dokumentację w `docs/art/**`, a gdy konieczne odpowiednie odnośniki w `docs/README.md` i `docs/planning/RESEARCH_ROADMAP.md`. Nie kasuj ustaleń Etapu A. Pracuj na osobnej gałęzi, użyj Draft PR. **Nie merge, nie force-push.**

## 3. KROK 0: Odczyt repo (zanim cokolwiek zapiszesz)

1. Otwórz `docs/art/STAGE_B_README.md` i `docs/art/SOURCE_REGISTER.md` w aktualnym HEAD.
2. Otwórz `docs/world/STAGE_A_README.md`, `docs/world/DISTRICTS_MASTERPLAN.md` i `docs/world/atlas/LANDMARK_CATALOG.md` tylko w zakresie potrzebnym do danego zadania.
3. Otwórz `docs/world/atlas/CONSERVATION_AND_RESPECT.md` zawsze przy Sekule, Muchawce, miejscach pamięci i sakralnych.
4. Wpisz `CURRENT_BRANCH` i `HEAD_SHA` z faktycznego GitHub. Jeśli narzędzie GitHub nie działa, wpisz `BLOCKED_REMOTE_ACCESS` i STOP na zapisie.
5. Sprawdź, czy żądany plik istnieje. Jeżeli istnieje, **edytuj aktualny**, nie twórz `_final_v3.md` obok.
6. Zanim dodasz zdjęcie lub render, sprawdź `SOURCE_REGISTER.md` i `concepts/README.md`.

## 4. Minimalny kontekst dla słabego modelu

**Jedno wywołanie = jeden packet P0–P9**. Zwykle maksymalnie 2 pełne dokumenty do modyfikacji w jednej sesji, 1–4 karty scen lub 1 dzielnica. Podziel duży plik, jeżeli mieści 23 shoty, na numery ID, nie na nowy chaotyczny zestaw JSON.

Jeśli zabraknie kontekstu, nie podejmuj następnego packetu. Zapisz dotychczasowe wyniki i raport stanu.

## 5. Hierarchia danych (rozpoznawalność, prawa, gry)

**Źródło prawdy w kolejności:**
1. Nowsza, jawna decyzja właściciela w `DECISION_LOG.md`.
2. 41 kart Etapu A / referencje / zasady ochrony dla realnych obiektów.
3. Aktualny 7-strefowy masterplan = **PROPOSAL**.
4. Art Bible i styl = **PROPOSAL**, do sprawdzenia w zdjęciach i obrazach.
5. Obraz AI i kopia gry = **nigdy źródło prawdy o realnym Siedlcu**.

Każdą kartę dziel na: `REAL_FACT_WITH_Lxx`, `STYLIZED_BUT_PLAUSIBLE`, `FANTASY_DECLARED`, `UNKNOWN/BLOCKED`.

## 6. Błędy, których nie wolno popełnić

| Błędna automatyczna odpowiedź | Co zrobić prawidłowo |
|---|---|
| „Ratusz” to losowy biały pałac | Jacek C01 musi mieć centralną historyczną wieżę i Atlasa [L01] |
| „Pałac Ogińskich” jest nowoczesnym zamkiem | C02 ma klasycystyczny portyk [L02] |
| „Muchawka” to tropikalna wyspa na oceanie | N01 = prawdziwe kąpielisko i akwen; MW-04 = wyspy tylko fantasy [L06] |
| „Sekuła” to stok z kolejką linową | N05 = biegówki [L12]; nie mieszać z N06 |
| „Górka Grześ jest tu” bez pinu | N07 = BLOCKED_GEOLOCATION, brak rzekomej panoramy |
| „S01 ma basen 25×21” | S01 = stadion piłkarski [L09], S02 = basen [L10] |
| „Mam render Roblox” pokazując obraz z AI | nadaj `AI_CONCEPT`; screenshot tylko z rzeczywistego Roblox |
| „4K na wszystko” | testuj rozdzielczość per obiekt, nie każ 4K na drobne prop-y [R06,R10] |
| „Future Lighting ustawione” | nowa oś to `LightingStyle Soft/Realistic` [R01] |
| „Zdjęcia miasta są publiczne, więc można wgrać” | LINK_ONLY / RIGHTS_UNKNOWN |
| „Mam PASS” bez obrazów | DOCUMENTED / PROMPT_ONLY, nie Stage B PASS |

## 7. Słownik statusów (używaj dokładnie)

- `NOT_STARTED`: nie rozpoczęto.
- `IN_PROGRESS`: pracujesz.
- `DOCUMENTED`: istnieje realny dokument z treścią i źródłami.
- `PROMPT_READY_IMAGE_NOT_GENERATED`: prompt napisany, 0 obrazów.
- `RENDERED_CONCEPT`: plik obrazu rzeczywiście istnieje i ma manifest, nie zatwierdzony.
- `BLOCKED_GEOLOCATION` / `BLOCKED_LICENSE` / `BLOCKED_TOOL` / `BLOCKED_REMOTE_ACCESS`: konkretny brak, lista jak go usunąć.
- `NOT_TESTED`: nie wykonano mierzalnego sprawdzenia.
- `REVIEW_REQUIRED`: praca czeka na recenzenta.
- `APPROVED`: właściciel wyraźnie zatwierdził dokładnie ten wariant.
- `STAGE_B_PASS`: wyłącznie po pełnym gate, wizualizacjach i akceptacji ownera.

## 8. Sesje krok po kroku

| Sesja | Packet | Czytaj najpierw | Pisz | Co sprawdzić |
|---|---|---|---|---|
| 0 | P0 | STAGE_B_README, STAGE_A_README | STAGE_B_README | 41/40/7, blokery |
| 1 | P1 | STYLE_VARIANTS + SOURCE_REGISTER | STYLE_VARIANTS | 3 style i 2 locki |
| 2 | P2 | CONCEPT_PROMPT_LIBRARY | CONCEPT_PROMPT_LIBRARY | 6 promptów, pliki V02/V05 |
| 3 | P3 | DISTRICT_LOOKDEV + masterplan | DISTRICT_LOOKDEV | D1–D4, MW-01..06 |
| 4 | P4 | DISTRICT_LOOKDEV + ochrony | DISTRICT_LOOKDEV | D5–D7, sport/las |
| 5 | P5 | CHARACTER_AND_VEHICLES | CHARACTER_AND_VEHICLES | 5 NPC, 7 pojazdów, prop-y |
| 6 | P6 | LIGHTING_LOOKDEV + R01–R04 | LIGHTING_LOOKDEV | L1/L2/L3, zima/lato |
| 7 | P7 | SHOT_CARDS_V01_V23 | SHOT_CARDS_V01_V23 | maks 4 Vxx / sesja, w sumie 23 |
| 8 | P8 | MODULAR_ASSET_GUIDE, UI_VISUAL_GUIDE | jeden plik na raz | mobile, OpenGL normals, 20k/mesh |
| 9 | P9 | VISUAL_REVIEW, STAGE_B_README | oba + linki indeksu | zgodny diff, Draft PR, brak fake PASS |

**Nie powtarzaj etapów wykonanych**: jeśli widzisz dokument, sprawdź luki i dopracuj tylko brakujące sekcje.

## 9. Procedura JEDNEGO kadru dla modelu bez generatora

1. Weź jedno ID `V-xx` i sprawdź [kartę kadru](SHOT_CARDS_V01_V23.md).
2. Sprawdź, że wszystkie `POI_IDS` istnieją w katalogu.
3. Znajdź źródła [Lxx] dla realnych cech i przeczytaj je; przy braku sieci wpisz `SOURCE_UNAVAILABLE`.
4. Wypisz dokładnie 3 cechy rozpoznawcze (w razie braków OPEN).
5. Zaznacz wszystkie fikcyjne elementy w osobnym akapicie.
6. Ustal kamerę, kadr, światło, proporcję 16:9 lub 4:3, powiązanie z innymi scenami.
7. Napisz pozytywny prompt i negative prompt z [biblioteki](CONCEPT_PROMPT_LIBRARY.md), bez kopiowania cudzych chronionych grafik.
8. Zapisz status `PROMPT_READY_IMAGE_NOT_GENERATED`, a `OUTPUT_FILE: NOT_CREATED`.
9. Przetestuj zgodność z ochroną i landmarkiem (opisowo). NIE wpisuj `RENDERED_CONCEPT`.

**Model z generatorem** może przejść do obrazu dopiero po karcie i kontroli praw. Upewnij się, że obraz fizycznie istnieje, obejrzyj go, dodaj manifest w `concepts/README.md` i status `RENDERED_CONCEPT`. Każda recenzja w [VISUAL_REVIEW](VISUAL_REVIEW.md).

## 10. Procedura porównania styli B1

Dwie sceny `LOCK-C01-A` oraz `LOCK-N01-A`. Dla każdej trzy style S1, S2, S3, czyli 6 wyników. Trzy rzeczy MUSZĄ być te same: **geometria bazowa landmarku, kamera, pora dnia**. Jeżeli generator nie obsługuje spójnych kadrów, opisz brak jako `COMPARABILITY_LIMITED`. W scoringu pięć kryteriów ważących 30/20/20/15/15; nie wpisuj cyfr przed oglądaniem konkretnych obrazów.

## 11. Wymagania techniczne do zapamiętania (po źródłach)

- Roblox 2026: `Lighting.LightingStyle` Soft albo Realistic. `Lighting.Technology` nie jest aktualną osią konfiguracji [R01].
- Atmosphere może schować odległy ratusz, więc mgłę oceniaj po zasięgu sylwetek [R02].
- SurfaceAppearance korzysta z PBR, normal map OpenGL tangent-space, UV 0–1; mesh tylko jedna materia [R06,R07].
- Blender eksportuje Z-up, Roblox używa Y-up: przyszły import wymaga kontroli transformu [R09].
- 20 000 trójkątów to limit jednego mesha, nie całego modelowanego miasta [R05].
- Streaming/SLIM/RenderFidelity i reuse są ważniejsze dla świata niż świetny render jednego rogu ulicy [R10,R11].
- Rozmiar świata, RAM, FPS, czas wejścia i mobile **niezweryfikowane** dopóki brak realnych testów z klienta [R12].
- UI: mobile safe area, notch, pasek Roblox i joystick mają pierwszeństwo [R13,R14].
- Dziecko powinno rozpoznawać symbole także bez koloru/dźwięku [R15].

## 12. Co wolno wysyłać na GitHub i jak

- Otwórz aktualny HEAD przed edycją; nie pracuj na stale zapisanym sha sprzed kilku sesji.
- Zapis dokumentacji po jednym logicznym packetcie; nazwy z indeksu, bez `COPY.md`, `FINAL2.md`, `random.json`.
- Jeśli dostępny jest GitHub connector: sprawdź gałąź, przygotuj zmianę tylko docs, użyj zwykłego fast-forward i otwórz **Draft PR**. Nie merguj, nie nadpisuj cudzej zmiany.
- Jeśli masz tylko tekstowy interfejs i nie możesz commitować: gotowe diffy/pełną treść opisz jako `REMOTE_WRITE_BLOCKED` i nie twierdź, że repo zostało zaktualizowane.
- Bezpośrednio przed finalizacją porównaj PR z main. **FAIL jeśli zmienia `MathCity.rbxl`, `src/`, `assets/`, cokolwiek YACS.**
- Sprawdź linki lokalne dokumentów i stabilne 23 ID scen. GitHub mógł zmienić gałąź w międzyczasie; odśwież HEAD.

## 13. Checklisty po każdej turze (przykład)

~~~text
PACKET: P2
INPUT_PATHS: docs/art/STYLE_VARIANTS.md; docs/art/CONCEPT_PROMPT_LIBRARY.md
ACTUALLY_READ: YES
OUTPUT_PATH: docs/art/CONCEPT_PROMPT_LIBRARY.md
SOURCE_IDS: L01,L06,R15
POI_FACTS: C01 historyczna sylwetka; N01 akwen
FICTIONAL: brama z zegarem; fantasy interakcje
IMAGES_GENERATED: 0
OUTPUT_IMAGE_FILES: NOT_CREATED
PASS: six prompts with stable camera locks
BLOCKED: no image generator
BRANCH: <real branch>
HEAD_SHA: <real sha or NOT_VERIFIED>
STATUS: PROMPT_READY_IMAGE_NOT_GENERATED
NEXT: P3
~~~

## 14. Gate końcowy i raport

[VISUAL_REVIEW.md](VISUAL_REVIEW.md) to lista dowodów. Raport końcowy wypełnij dokładnie:

~~~text
MATHCITY STAGE B
DATE:
REPOSITORY: karnalooch/MathCity
BRANCH:
HEAD_SHA:
DRAFT_PR_URL:
B0_STRUCTURE:
B1_STYLE_VARIANTS:
B2_7_DISTRICTS:
B3_CHARACTERS_VEHICLES:
B4_LIGHTING_L1_L3:
B5_SHOTS_V01_V23:
B6_MODULAR_KIT:
B7_UI:
B8_QA:
FILES_CREATED:
FILES_UPDATED:
IMAGES_ACTUALLY_CREATED:
PROMPTS_READY:
RIGHTS_BLOCKERS:
N07_GORKA_STATUS: BLOCKED_GEOLOCATION
STAGE_A_STATUS: PARTIAL
MATHCITY_RBXL_UNCHANGED: VERIFIED/NOT_VERIFIED/NO
SRC_UNCHANGED: VERIFIED/NOT_VERIFIED/NO
ASSETS_UNCHANGED: VERIFIED/NOT_VERIFIED/NO
STAGE_B_OVERALL: DOCUMENTED | PARTIAL | REVIEW_REQUIRED | PASS
OWNER_APPROVAL: PENDING | APPROVED
NEXT_ACTION:
~~~

**Minimalna definicja sukcesu tego runbooka:** Agent zawsze wie: co przeczytać, którą jedną rzecz zrobić, gdzie zapisać, jak udowodnić i kiedy przestać. Zero zmyślonych renderów, zero uszkodzenia gry, zero „DONE” bez dowodu.
