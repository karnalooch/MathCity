# MathCity: dokumentacja projektu i plan wykonawczy

**Stan: 2026-10-19. Dokumentacja po 33 decyzjach właściciela. Nowa gra NIE została zaimplementowana.** Repo zawiera działający prototyp `MathCity.rbxl`, którego ten pakiet nie zmienia.

## Skille wykonawcy: plan 2026-10-20

[LLM_SKILLS_PLAN.md](planning/LLM_SKILLS_PLAN.md) opisuje rekomendowaną bibliotekę: jeden zewnętrzny kandydat Roblox/Luau, osiem własnych skilli projektowych, selektywne procedury testów i diagnostyki, routing do istniejących kontraktów, integracje oraz 12 prób odbioru samych skilli. **PROPOSED_STACK / NOT_INSTALLED / SKILL_EVALUATIONS_NOT_RUN.** Nie zainstalowano pakietów, nie połączono Studio ani nie nadano uprawnień do implementacji gry.

## Roblox Studio MCP: oficjalna ścieżka do Studio

Roblox Studio ma wbudowany serwer MCP. Konfiguracja Windows, Quick Connect, lista narzędzi, `studio_id`, smoke test i zasady bezpieczeństwa są w **[ROBLOX_STUDIO_MCP.md](tech/ROBLOX_STUDIO_MCP.md)**. Słabszy wykonawca ma używać procedury **[MCP_REMOTE_WORKFLOW.md](planning/MCP_REMOTE_WORKFLOW.md)**.

Status: **OFFICIAL_MCP_CONFIRMED / CONFIG_DOCUMENTED / LOCAL_CONNECTION_NOT_RUN**. MCP nie został jeszcze połączony z komputerem w ramach tego commita i nie daje automatycznie pozwolenia na modyfikowanie `MathCity.rbxl`.

## Wykonawca zaczyna tutaj

**[WEAK_LLM_START_HERE.md](planning/WEAK_LLM_START_HERE.md)** wyznacza kolejność czytania i pracy. **[Gotowy prompt](planning/EXECUTOR_PROMPT.md)** uruchamia jeden mały pakiet, nie cały projekt naraz. **[33 decyzje Q01–Q33](planning/OWNER_DECISIONS_20261019.md)** są nadrzędne wobec wcześniejszych propozycji A/B/C. **[Pakiety D00–D06 i P00–P10](planning/EXECUTION_PACKETS.md)** określają wejścia, czynności, wyjścia i warunki odbioru.

Nowa wizja: ogromne, autorskie Siedlce w Roblox, nie replika1:1. Wspólna mapa, indywidualna matematyka klas2–4, lokalne przygody, progres bez grindu, własny pokój, dobrowolne wyścigi i współpraca. UE, Blender i Material Forge z YACS są zapleczem produkcyjnym; docelową grę testuje się w Roblox.

## Houdini FIRST — decyzja produkcyjna

**Houdini jest primary world/content tool.** Unreal Engine, Blender i Material Forge z YACS są wsparciem; Roblox jest runtime. Pełny kontrakt: **[HOUDINI_FIRST_PIPELINE.md](tech/HOUDINI_FIRST_PIPELINE.md)**.

**P00 + H00 uruchomione do wykonania:** [komenda Windows, generator Houdini i test importu](tech/P00_H00_RUNBOOK.md). [Raport dostarczenia kodu](reports/P00_H00_DELIVERY_20261020.md) rozdziela testy plików od niewykonanego jeszcze cooka/Studio. Recepta: [`worldgen/h00/recipe.json`](../worldgen/h00/recipe.json). Wytworzone HIP/PNG/cache pozostają w osobnym katalogu roboczym na D:.

Pierwsze trzy dowody techniczne to **H00 Terrain**, **H01 procedural mesh** i **H02 materials**. Nie budujemy miasta ręcznie w Roblox Studio jako obejścia niedziałającego generatora.

## Aktualny stan etapów

| Obszar | Co jest dostarczone | Co pozostaje otwarte |
|---|---|---|
| Decyzje produktu |33 odpowiedzi zapisane z granicami i scenariuszami QA | dokładne liczby balansu, nie ponowny wybór zasad |
| A: atlas |41 miejsc,41 kart i40 kandydatów M01–M40 | zdjęcia/prawa, Grześ, trasy, odbiór geografii |
| B: wygląd | odrębny [Draft PR #1](https://github.com/karnalooch/MathCity/pull/1),17 SVG i23 karty według stanu odczytu | nie połączony, finalne rendery3D i akceptacja stylu niewykonane |
| C: mechaniki |15 analiz źródłowych i rozszerzenie Mario Kart | rzeczywiste sesje0/15; brak runtime/mobile pomiarów |
| D: edukacja | audyt40 ID, źródła z punktami,8 kart, walidatory i scenariusze pomocy | review nauczyciela oraz wdrożenie/pilotaż niewykonane |
| Technologia i sprzęt | kontrakty danych/UI/urządzeń, plan prób1–4 i16graczy | Luau, Studio i urządzenia NOT_RUN |

Zapis specyfikacji nie kończy badań A/B/C, nie scala PR#1 ani nie dopuszcza gry do publicznej premiery. Aktualne interpretacje zasad platformy i prawa trzeba sprawdzić przed publikacją; statusów nie przenosić automatycznie z historycznych notatek.

## Dokumentacja wykonawcza

| Temat | Plik |
|---|---|
| Bieżący GDD | [GDD.md](GDD.md) |
| Zatwierdzone wybory | [OWNER_DECISIONS_20261019.md](planning/OWNER_DECISIONS_20261019.md) |
| Starsze wymagania i rozstrzygnięcie propozycji | [DECISION_LOG.md](planning/DECISION_LOG.md) |
| Etap D: wejście | [STAGE_D_README.md](education/STAGE_D_README.md) |
| Źródła programu | [CURRICULUM_SOURCES.md](education/stage_d/CURRICULUM_SOURCES.md) |
| Audyt wszystkich minigier | [M01_M40_AUDIT.md](education/stage_d/M01_M40_AUDIT.md) |
| Osiem kart do pilotów | [PILOT_INDEX.md](education/stage_d/PILOT_INDEX.md) |
| Generator, walidacja i adaptacja | [TASK_MODEL_AND_ADAPTATION.md](education/stage_d/TASK_MODEL_AND_ADAPTATION.md) |
| Przykłady, wyniki i kod kontroli rachunkowej | [TEST_VECTORS.md](education/stage_d/TEST_VECTORS.md) |
| EXP, nagrody, antygrind | [PROGRESSION_AND_REWARDS.md](gameplay/specs/PROGRESSION_AND_REWARDS.md) |
| Grupy, role, późne dołączenie | [COOP_AND_WORLD_STATE.md](gameplay/specs/COOP_AND_WORLD_STATE.md) |
| Paszport, mieszkanie, onboarding, transport | [EXPLORATION_HOME_ONBOARDING.md](gameplay/specs/EXPLORATION_HOME_ONBOARDING.md) |
| Wyścigi i przedmioty | [RACING.md](gameplay/specs/RACING.md) |
| Mocne UI i podpowiedzi | [LEARNING_UI_CONTRACT.md](ux/LEARNING_UI_CONTRACT.md) |
| Serwer i zapis profilu | [DATA_AND_SERVER_CONTRACT.md](tech/DATA_AND_SERVER_CONTRACT.md) |
| Wymagane urządzenia i test16klientów | [DEVICE_ACCEPTANCE.md](tech/DEVICE_ACCEPTANCE.md) |
| Przypadki odbioru | [ACCEPTANCE_MATRIX.md](planning/ACCEPTANCE_MATRIX.md) |
| Kolejność pakietów i bramki | [EXECUTION_PACKETS.md](planning/EXECUTION_PACKETS.md) |
| Roadmapa całości | [RESEARCH_ROADMAP.md](planning/RESEARCH_ROADMAP.md) |

## Atlas, wygląd i wcześniejszy research

[Etap A](world/STAGE_A_README.md), [pełna Muchawka N01](world/atlas/MUCHAWKA_FEATURE.md), [katalog miejsc](world/atlas/LANDMARK_CATALOG.md), [pierwotne M01–M40](world/atlas/MECHANICS_MATRIX.md), [fotoreferencje i prawa](world/atlas/PHOTO_REFERENCES.md), [runbook atlasu](world/atlas/WEAK_LLM_RUNBOOK.md). `N01` to Zalew Muchawka, `S02` to odrębny Park Wodny. Sekuła jest osobną roboczą strefą; Grześ wymaga potwierdzenia miejsca.

[Masterplan](world/DISTRICTS_MASTERPLAN.md) nadal przedstawia7 proponowanych stref, nie podział zatwierdzony geograficznie. [Art Bible na main](art/ART_BIBLE.md), [kadry](art/CONCEPT_SHOTS.md), [schemat](art/MATHCITY_WORLD_SCHEMATIC.svg) są koncepcją, nie dowodem wyglądu runtime. Rozbudowane plansze B znajdują się w odrębnym Draft PR#1 i nie wolno zakładać ich obecności w main.

[Etap C](gameplay/STAGE_C_README.md), [15 gier](gameplay/stage_c/BENCHMARK_15_GAMES.md), [protokół prawdziwych testów](gameplay/stage_c/PLAYTEST_PROTOCOL.md), [research Mario Kart](gameplay/stage_c/MARIO_KART_RACING_RESEARCH.md), [wstępna analiza rynku](gameplay/ROBLOX_MARKET_RESEARCH_2026.md). Nieaktualne statusy „propozycja” w historycznym researchu rozstrzygają obecne Qxx; nie przypisujemy jednak nowych decyzji właścicielowi bez jego odpowiedzi.

[Wstępna mapa edukacyjna](education/CURRICULUM_2_4.md) zachowana jako tło Muchawki i projektu. Źródłem bieżących kontraktów jest etap D, nie pierwsza ogólna tabela klas. [Houdini-first pipeline](tech/HOUDINI_FIRST_PIPELINE.md), [skrót pipeline'u](tech/CONTENT_PIPELINE.md), [duży świat](tech/LARGE_WORLD.md), [testowanie v1](tech/PLAYTESTING.md), [prawa i publikacja](legal/RIGHTS_AND_COMPLIANCE.md), [bibliografia researchu](research/SOURCES.md), [ryzyka](research/RISKS_AND_OPEN_QUESTIONS.md), [karta wizji](vision/PROJECT_CHARTER.md).

## Prototyp v1, nie wymagania nowej gry

[GDD wieży](legacy/GDD_TOWER_V1.md), [architektura istniejącego kodu](ARCHITECTURE.md), [20 pytań wieży](MATH_CURRICULUM.md), [instrukcja konfiguracji](ROBLOX_SETUP_GUIDE.md), [poradnik Studio](../PORADNIK_ROBLOX_STUDIO.md), [drzwi](../references/DOOR_BUILDING_SPECS.md), [stara ekonomia](../references/ECONOMY_BALANCE.md), [skrót klawiszy](../references/SHORTCUTS_AND_TOOLS.md). Śmierć za błąd i płatny panel administratora nie są zaakceptowanym kierunkiem nowej edukacyjnej gry.

## Statusy dowodów

APPROVED_DESIGN = decyzja; SPEC_READY = dokument; TEST_DEFAULT = parametr do sprawdzenia; TEACHER_REVIEW_PENDING = brak zatwierdzenia pedagogicznego; NOT_RUN = test niewykonany. Osobno DOC_CHECKED, UNIT_PASS, STUDIO_PASS i DEVICE_PASS. Pliki gry nie zmieniają się od samego utworzenia docs.
