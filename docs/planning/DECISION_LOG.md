# MathCity: decyzje właściciela i status wcześniejszych propozycji

Aktualizacja 2026-10-20. Zachowano identyfikatory D-001…D-014, dodano uruchomienie P00/H00 jako D-015. Szczegółowe decyzje produktu znajdują się w [OWNER_DECISIONS_20261019.md](OWNER_DECISIONS_20261019.md): **Q01…Q33**. Nie zamieniaj ich z powrotem w pytania do głosowania. Zatwierdzony projekt nie oznacza wykonanej gry.

## Wcześniejsze wymagania, nadal obowiązujące

| ID | Decyzja | Konsekwencja |
|---|---|---|
| D-001 | MathCity.rbxl właściwą mapą; Roblox.rbxl zbędny | nie nadpisywać sprawdzonej mapy w etapie dokumentacji |
| D-002 | Maksymalnie duże miasto w Roblox | benchmark pełnej skali, nie sama pusta plansza |
| D-003 | Promocja Siedlec, nie replika1:1 | rozpoznawalne miejsca i autorski układ |
| D-004 | Matematyka klas2–4 na obecnym etapie | właściwe roczniki i review dydaktyczne |
| D-005 | Research modnych mechanik bez kopii1:1 | własne adaptacje, nie cudze assety |
| D-006 | UE, Blender, Material Forge z YACS jako zaplecze, łatwy test w Roblox | Roblox jedynym runtime |
| D-007 | Inspiracja Vice City i Odyssey | własna stylizacja bez kopiowania znaków i postaci |
| D-008 | Historyczny zakres etapów badawczych: research i dokumentacja, nie przebudowa gry | wyjątek P00/H00 uruchomiony później przez D-015; istniejąca gra nadal poza zakresem |
| D-009 | Wyniki w odpowiednich docs | indeks, źródła, konkretne kontrakty |
| D-010 | Sekuła i Górka Grześ w badaniu miejsc i mechanik | nie zgadywać położenia Grześ |
| D-011 | Trasy narciarskie Sekuły w researchu | biegówki według źródeł, nie stok zjazdowy |
| D-012 | Stadion i basen istotnymi ośrodkami | osobne karty i funkcje, nie dekoracyjne bryły |
| D-013 | Zalew Muchawka pełnym istotnym hubem | N01 osobno od S02; fantasy podstrefy/mechaniki nadal do odbioru |
| **D-014** | **Houdini jest głównym wykonawcą świata/contentu; UE, Blender i Material Forge z YACS są wsparciem** | Houdini jest source-of-truth proceduralnego terenu, masek, dróg/korytarzy, generatorów, scatter i eksportów; UE=lookdev, Blender=cleanup/hero, Material Forge=PBR; Roblox jedynym runtime |
| **D-015** | **Uruchomić P00 + H00 po zatwierdzonym opisie następnego kroku (2026-10-20, „dawaj”)** | kod narzędzi audytu i syntetycznego terenu na osobnej gałęzi, osobne miejsce testowe, bez zmiany `MathCity.rbxl`, gameplayu, projektu YACS i bez publikacji; [wykonanie i dowody](../tech/P00_H00_RUNBOOK.md) |

## Nowy zapis decyzji

Q01–Q07: wspólne miasto, adaptacja, rola matematyki, nagrody, solo/co-op, EXP catch-up, guided. Q08–Q14: osobiste historie i wspólny świat, misje poboczne, pokój, sklepy, powtórki, paszport, podróż. Q15–Q20: sport/stoper/medale, profile, przedmioty, boty, tablice znajomych. Q21–Q26: odkrycia zamiast level gates, UI zamiast głosu teraz, tutorial, generator, otwarte rozwiązania i prywatne umiejętności. Q27–Q33: urządzenia, obowiązkowy iPad6,16graczy,1–4co-op, szukanie grup i wejście między etapami.

Pełny tekst i ograniczenia każdego wyboru są w rejestrze Q, nie w tym skrócie. Szczególnie Q17 to odpowiedź po Mario Kart, a Q22 odkłada głos na później. Literalne wartości TEST_DEFAULTS nie są zatwierdzeniami właściciela.

## Rozstrzygnięcie dawnych propozycji P

| ID | Dawna propozycja | Status po rozmowie |
|---|---|---|
| P-001 |6 dzielnic | historyczna; research rozszerzony do7, sam układ nadal otwarty |
| P-002 | Tajemnica kuli Jacka | odłożona główna fabuła, Q09; nie narzucać |
| P-003 |8 konkretnych minigier startowych | aktualna rekomendacja ośmiu pilotów w etapieD, nie pełne zatwierdzenie treści |
| P-004 | Pętla eksploracja/zadania/kosmetyka | zasady rozstrzygnięte Q03/Q04/Q09/Q11, detale treści do testów |
| P-005 | Jeden Place i ewentualne osobne areny | technicznie otwarte; bez automatycznej rezygnacji z dużej mapy |
| P-006 |8192/16384 studów | nadal zakres eksperymentu, nie ostateczny rozmiar |
| P-007 |60PC/30mobile | cele testowe uściślone urządzeniami Q27–Q30, nie wyniki |
| P-008 | Brak śmierci za matematyczny błąd | rozstrzygnięte Q07; pomoc i zachowanie podstawowej nagrody |
| P-009 | Stary płatny admin nie strategiąv2 | nie wracać do niego jako domyślnej monetyzacji; nowa monetyzacja nadal nieustalona |
| P-010 | Adaptacja i paszport | rozstrzygnięte Q02/Q13/Q26; prywatność i ręczny wybór |
| P-011 |7 stref z osobną Sekułą | propozycja mapy pozostaje do zatwierdzenia |
| P-012 |6 podstref Muchawki i szczegółowe mechaniki | istotność miejsca zatwierdzona D-013; dokładny layout/treść wciąż do review |

## Reguła przyszłych zmian

Każdy PR podaje Qxx i test, który realizuje. Jeśli zmienia regułę właściciela, potrzebuje nowej jawnej decyzji. Jeżeli tylko stroi TEST_DEFAULT, ma podać pomiar i wersję parametru. Nie ogłaszać A/B/C/D PASS przez sam commit. [GDD](../GDD.md), [pakiety](EXECUTION_PACKETS.md), [roadmapa](RESEARCH_ROADMAP.md).
