# MathCity — dokumentacja projektu

**Stan: 2026-10-19. Etap: research, koncepcja, wizualizacje i planowanie.**

## Zasada nadrzędna

Nowa wizja: duży, otwarty świat **Siedlec inspirowanych miastem rzeczywistym, ale nie odtworzonych 1:1**, łączący promocję miejsc, eksplorację i gry matematyczne dla klas 2–4. Głównym silnikiem jest **Roblox**; Unreal Engine, Blender i Material Forge z warsztatu YACS są narzędziami przygotowania treści. **Na tym etapie nie wdrażamy koncepcji do gry.**

Repozytorium zawiera działający prototyp wieży matematycznej. Plik **MathCity.rbxl** pozostaje źródłem istniejącej mapy. Planowanie nowego świata **nie oznacza, że opisane funkcje są już zaimplementowane**.

## Etap A: atlas Siedlec, Sekuły i sportu (research 18.10.2026)

**WYKONANO RESEARCH DESK, ETAP A NIE JEST JESZCZE PASS.** Zebrano **41 kandydatów miejsc**, 41 kart wykonawczych, 40 propozycji minigier i linki do fotoreferencji. Do zatwierdzenia pozostają zdjęcia/licencje, dokładny pin Górki Grześ, przebieg tras Sekuły i masterplan. Wszystko ma stabilne identyfikatory, a w dokumentach fakty są oddzielone od fikcyjnych mechanik.

**Nowe rozszerzenie 2026-10-19:** szczegółowe wymagania dla Zalewu Muchawka oraz matematyki klas 2–4 dodano w [katalogu Muchawki](world/atlas/MUCHAWKA_FEATURE.md) i [CURRICULUM_2_4.md](education/CURRICULUM_2_4.md). `N01` to Zalew Muchawka; `S02` to zupełnie odrębny Park Wodny. Pliki gry pozostają nietknięte.

**Główne wejście:** [world/STAGE_A_README.md](world/STAGE_A_README.md). Szczegółowe instrukcje dla słabszego LLM: [world/atlas/WEAK_LLM_RUNBOOK.md](world/atlas/WEAK_LLM_RUNBOOK.md). Proponowany masterplan został rozszerzony z 6 do **7 stref** (osobno Sekuła), ale **nie** jest zatwierdzony.

## Etap C: mechaniki Roblox (research 19.10.2026)

**Research źródłowy dostarczony, Etap C PARTIAL.** Pakiet obejmuje 15 kart konkretnych gier, ranking 10 wzorców, pięć antywzorców, powiązanie z istniejącymi `M01–M40`, scenariusz pierwszych 20 minut MathCity oraz pięć propozycji małych eksperymentów. Nie jest to lista 15 liderów aktualnego rankingu. Fakty z opisów twórców są oddzielone od naszych interpretacji i propozycji.

**Wejście:** [gameplay/STAGE_C_README.md](gameplay/STAGE_C_README.md). Szczegółowy [runbook dla słabszego LLM](gameplay/stage_c/WEAK_LLM_RUNBOOK.md) oraz [protokół testów](gameplay/stage_c/PLAYTEST_PROTOCOL.md). **Własne sesje Roblox: 0/15; testy mobilne i kooperacyjne niewykonane.** Czas pierwszej nagrody, FPS i ceny nie zostały zmierzone. Pełny PASS wymaga rzeczywistych rozgrywek i oceny wniosków; samo zapisanie dokumentów tego nie zastępuje.

## Nawigacja

| Obszar | Dokument |
| --- | --- |
| **Aktualny GDD** | [GDD.md](GDD.md) |
| Wizja i kryteria sukcesu | [vision/PROJECT_CHARTER.md](vision/PROJECT_CHARTER.md) |
| **ZALEW MUCHAWKA: flagowa atrakcja i 12 minigier** | [world/atlas/MUCHAWKA_FEATURE.md](world/atlas/MUCHAWKA_FEATURE.md) |
| **Etap A: punkt wejścia (41 miejsc + karty)** | [world/STAGE_A_README.md](world/STAGE_A_README.md) |
| Karty sekcji A dla słabszego LLM | [world/atlas/WEAK_LLM_RUNBOOK.md](world/atlas/WEAK_LLM_RUNBOOK.md) |
| Fotografie i prawa (link-only) | [world/atlas/PHOTO_REFERENCES.md](world/atlas/PHOTO_REFERENCES.md) |
| Minigry powiązane z realnymi miejscami | [world/atlas/MECHANICS_MATRIX.md](world/atlas/MECHANICS_MATRIX.md) |
| Punkty charakterystyczne Siedlec | [world/SIEDLCE_LANDMARK_ATLAS.md](world/SIEDLCE_LANDMARK_ATLAS.md) |
| Dzielnice i masterplan | [world/DISTRICTS_MASTERPLAN.md](world/DISTRICTS_MASTERPLAN.md) |
| **Etap C: benchmark źródłowy 15 gier** | [gameplay/STAGE_C_README.md](gameplay/STAGE_C_README.md) |
| Etap C: wzorce powiązane z M01–M40 | [gameplay/stage_c/TRANSFER_MATRIX.md](gameplay/stage_c/TRANSFER_MATRIX.md) |
| Etap C: instrukcja dla słabszego LLM | [gameplay/stage_c/WEAK_LLM_RUNBOOK.md](gameplay/stage_c/WEAK_LLM_RUNBOOK.md) |
| Wstępny research mechanik z 18.10.2026 | [gameplay/ROBLOX_MARKET_RESEARCH_2026.md](gameplay/ROBLOX_MARKET_RESEARCH_2026.md) |
| Główna pętla i minigry | [gameplay/CORE_LOOP_AND_MINIGAMES.md](gameplay/CORE_LOOP_AND_MINIGAMES.md) |
| Matematyka klas 2–4 | [education/CURRICULUM_2_4.md](education/CURRICULUM_2_4.md) |
| Art bible i paleta | [art/ART_BIBLE.md](art/ART_BIBLE.md) |
| Briefy wizualizacji i kadrów | [art/CONCEPT_SHOTS.md](art/CONCEPT_SHOTS.md) |
| Schemat koncepcyjny mapy | [art/MATHCITY_WORLD_SCHEMATIC.svg](art/MATHCITY_WORLD_SCHEMATIC.svg) |
| UE / Blender / Material Forge → Roblox | [tech/CONTENT_PIPELINE.md](tech/CONTENT_PIPELINE.md) |
| Rozmiar świata i wydajność | [tech/LARGE_WORLD.md](tech/LARGE_WORLD.md) |
| Szybkie testy i praca z Wojtkiem | [tech/PLAYTESTING.md](tech/PLAYTESTING.md) |
| Publikacja, bezpieczeństwo dzieci, licencje | [legal/RIGHTS_AND_COMPLIANCE.md](legal/RIGHTS_AND_COMPLIANCE.md) |
| Bibliografia z datą dostępu | [research/SOURCES.md](research/SOURCES.md) |
| Niewiadome, ryzyka i założenia | [research/RISKS_AND_OPEN_QUESTIONS.md](research/RISKS_AND_OPEN_QUESTIONS.md) |
| Plan kolejnych badań i bramki decyzji | [planning/RESEARCH_ROADMAP.md](planning/RESEARCH_ROADMAP.md) |
| Decyzje zatwierdzone vs propozycje | [planning/DECISION_LOG.md](planning/DECISION_LOG.md) |

## Dokumenty prototypu v1 (zachowane)

- [legacy/GDD_TOWER_V1.md](legacy/GDD_TOWER_V1.md) — historyczny GDD Wieży Matematycznej; **nie** masterplan nowej gry.
- [ARCHITECTURE.md](ARCHITECTURE.md) — opis istniejącego klienta/serwera, DataStore i panelu administracyjnego.
- [MATH_CURRICULUM.md](MATH_CURRICULUM.md) — historyczny zestaw 20 pytań dla klasy 3, nie pełne pokrycie klas 2–4.
- [ROBLOX_SETUP_GUIDE.md](ROBLOX_SETUP_GUIDE.md) i [../PORADNIK_ROBLOX_STUDIO.md](../PORADNIK_ROBLOX_STUDIO.md) — instrukcje dla istniejącego prototypu.
- [../references/DOOR_BUILDING_SPECS.md](../references/DOOR_BUILDING_SPECS.md), [../references/ECONOMY_BALANCE.md](../references/ECONOMY_BALANCE.md), [../references/SHORTCUTS_AND_TOOLS.md](../references/SHORTCUTS_AND_TOOLS.md).

## Oznaczenia

- **USTALONE:** wymaganie właściciela projektu.
- **PROPOZYCJA:** pomysł do zatwierdzenia; nie jest zadaniem wdrożeniowym.
- **ZWERYFIKOWANE:** stwierdzenie z aktualnym źródłem lub stanem repo.
- **DO SPRAWDZENIA:** potrzeba dowodu, konsultacji albo benchmarku.

W razie sprzeczności **aktualny GDD i rejestr decyzji opisują kierunek**, a stare pliki dokumentują dotychczasowy prototyp. Ceny, trendy, ograniczenia Roblox i przepisy należy ponownie sprawdzić przed produkcją i publikacją.
