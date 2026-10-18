# MathCity — dokumentacja projektu

**Stan: 2026-10-18. Etap: research, koncepcja, wizualizacje i planowanie.**

## Zasada nadrzędna

Nowa wizja: duży, otwarty świat **Siedlec inspirowanych miastem rzeczywistym, ale nie odtworzonych 1:1**, łączący promocję miejsc, eksplorację i gry matematyczne dla klas 2–4. Głównym silnikiem jest **Roblox**; Unreal Engine, Blender i Material Forge z warsztatu YACS są narzędziami przygotowania treści. **Na tym etapie nie wdrażamy koncepcji do gry.**

Repozytorium zawiera działający prototyp wieży matematycznej. Plik **MathCity.rbxl** pozostaje źródłem istniejącej mapy. Planowanie nowego świata **nie oznacza, że opisane funkcje są już zaimplementowane**.

## Nawigacja

| Obszar | Dokument |
| --- | --- |
| **Aktualny GDD** | [GDD.md](GDD.md) |
| Wizja i kryteria sukcesu | [vision/PROJECT_CHARTER.md](vision/PROJECT_CHARTER.md) |
| Punkty charakterystyczne Siedlec | [world/SIEDLCE_LANDMARK_ATLAS.md](world/SIEDLCE_LANDMARK_ATLAS.md) |
| Dzielnice i masterplan | [world/DISTRICTS_MASTERPLAN.md](world/DISTRICTS_MASTERPLAN.md) |
| Popularne mechaniki Roblox (research) | [gameplay/ROBLOX_MARKET_RESEARCH_2026.md](gameplay/ROBLOX_MARKET_RESEARCH_2026.md) |
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
