# MathCity — dokumentacja projektu

**Stan: 2026-10-18. Etap: research, koncepcja, wizualizacje i planowanie.**

## Zasada nadrzędna

Nowa wizja: duży, otwarty świat **Siedlec inspirowanych miastem rzeczywistym, ale nie odtworzonych 1:1**, łączący promocję miejsc, eksplorację i gry matematyczne dla klas 2–4. Głównym silnikiem jest **Roblox**; Unreal Engine, Blender i Material Forge z warsztatu YACS są narzędziami przygotowania treści. **Na tym etapie nie wdrażamy koncepcji do gry.**

Repozytorium zawiera działający prototyp wieży matematycznej. Plik **MathCity.rbxl** pozostaje źródłem istniejącej mapy. Planowanie nowego świata **nie oznacza, że opisane funkcje są już zaimplementowane**.

## Etap B — OBRAZY i aktualna dokumentacja

**Dodano 17 autorskich graficznych referencji SVG**, które słabszy LLM ma obowiązek obejrzeć przed wykonywaniem zadań. **[Galeria obrazów, przypisanie do V01–V23](art/VISUAL_REFERENCE_ATLAS.md)**; [indeks Etapu B](art/STAGE_B_README.md), [instrukcje lekkich agentów](art/STAGE_B_WEAK_LLM_RUNBOOK.md). Obrazy SVG to wskazówki stylistyczne, nie geografia 1:1, nie fotografie i nie finalne screenshoty Roblox. **Etap B nadal nie ma PASS** (brak zatwierdzonych renderów i decyzji stylu).

## Etap A: atlas Siedlec, Sekuły i sportu (research 18.10.2026)

**WYKONANO RESEARCH DESK, ETAP A NIE JEST JESZCZE PASS.** Zebrano **41 kandydatów miejsc**, 41 kart wykonawczych, 40 propozycji minigier i linki do fotoreferencji. Do zatwierdzenia pozostają zdjęcia/licencje, dokładny pin Górki Grześ, przebieg tras Sekuły i masterplan. Wszystko ma stabilne identyfikatory, a w dokumentach fakty są oddzielone od fikcyjnych mechanik.

**Nowe rozszerzenie 2026-10-19:** szczegółowe wymagania dla Zalewu Muchawka oraz matematyki klas 2–4 dodano w [katalogu Muchawki](world/atlas/MUCHAWKA_FEATURE.md) i [CURRICULUM_2_4.md](education/CURRICULUM_2_4.md). `N01` to Zalew Muchawka; `S02` to zupełnie odrębny Park Wodny. Repozytorium gry pozostaje nietknięte.

**Główne wejście:** [world/STAGE_A_README.md](world/STAGE_A_README.md). Szczegółowe instrukcje dla słabszego LLM: [world/atlas/WEAK_LLM_RUNBOOK.md](world/atlas/WEAK_LLM_RUNBOOK.md). Proponowany masterplan został rozszerzony z 6 do **7 stref** (osobno Sekuła), ale **nie** jest zatwierdzony.

## Etap B — deep research i instrukcje dla lekkich LLM (2026-10-19)

**Dokumentacja artystyczna zaktualizowana, wizualizacje jeszcze nie wygenerowane.** B jest w stanie `STAGE_B_DOCUMENTATION_READY / STAGE_B_VISUALS_NOT_DONE`; nie PASS i bez zatwierdzonego stylu przez właściciela. Zastosowano aktualne źródła Roblox 2026 (LightingStyle, PBR/UV, mobile safe areas), porównanie 3 stylów na Jacku i Muchawce, 7-strefowy lookdev oraz dokładne karty V01–V23. **Start dla słabego modelu:** [instrukcja Etapu B](art/STAGE_B_WEAK_LLM_RUNBOOK.md) → [mikro-zadania](art/TASK_PACKETS.md). [Indeks Etapu B](art/STAGE_B_README.md).

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
| Popularne mechaniki Roblox (research) | [gameplay/ROBLOX_MARKET_RESEARCH_2026.md](gameplay/ROBLOX_MARKET_RESEARCH_2026.md) |
| Główna pętla i minigry | [gameplay/CORE_LOOP_AND_MINIGAMES.md](gameplay/CORE_LOOP_AND_MINIGAMES.md) |
| Matematyka klas 2–4 | [education/CURRICULUM_2_4.md](education/CURRICULUM_2_4.md) |
| **Etap B / galeria 17 referencji SVG** | **[art/VISUAL_REFERENCE_ATLAS.md](art/VISUAL_REFERENCE_ATLAS.md)** |
| **Etap B / status i wejście** | **[art/STAGE_B_README.md](art/STAGE_B_README.md)** |
| **Etap B / runbook dla słabszych LLM** | **[art/STAGE_B_WEAK_LLM_RUNBOOK.md](art/STAGE_B_WEAK_LLM_RUNBOOK.md)** |
| Etap B / prompty i 23 karty | [art/CONCEPT_PROMPT_LIBRARY.md](art/CONCEPT_PROMPT_LIBRARY.md), [art/SHOT_CARDS_V01_V23.md](art/SHOT_CARDS_V01_V23.md) |
| Etap B / źródła Roblox + Siedlce | [art/SOURCE_REGISTER.md](art/SOURCE_REGISTER.md) |
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
