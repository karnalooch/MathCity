# MathCity: roadmapa po33 decyzjach i plan następnych kroków

2026-10-19. Obecny zakres: **dokumentacja**, bez przebudowy mapy/kodu i bez publicznej publikacji. Wykonawca czyta [START HERE](WEAK_LLM_START_HERE.md), [33 decyzje](OWNER_DECISIONS_20261019.md) i realizuje po jednym [pakiecie](EXECUTION_PACKETS.md). Istniejący MathCity.rbxl pozostaje bez zmian.

## A: atlas Siedlec

Desk research dostarczony:41 punktów,41 kart i40 propozycji M01–M40. [Etap A](../world/STAGE_A_README.md), [Muchawka](../world/atlas/MUCHAWKA_FEATURE.md). N01 jest flagowym zalewem, S02 odrębnym basenem. Sekuła z biegówkami, stadion, kultura, dworzec i parki mają własne identyfikatory.

**PARTIAL:** brak kompletu praw do zdjęć, potwierdzenia Grześ, dokładnych tras i akceptacji roboczego7-strefowego układu. Nie zaczynaj atlasu od zera ani nie redukuj go znowu do15 punktów; domykaj istniejące karty i brakujące dowody. Wyspy i podstrefy Muchawki pozostają fikcją gry, nie odkryciem geograficznym.

## B: wygląd

Stan odczytu [PR#1](https://github.com/karnalooch/MathCity/pull/1): Draft, niepołączony;17 autorskich SVG,23 karty ujęć. Finalne rendery3D i zatwierdzenie S1/S2/S3 oczekują. Nie merge automatycznie. Najbliższy eksperyment wizualny: ratusz i Muchawka w porównywalnych kadrach/stylach, potem dzień/zachód/noc. Wersja rzeczywista Roblox będzie oddzielnym dowodem, nie screenshotem z UE.

## C: mechaniki

[SOURCE_RESEARCH_COMPLETE / PLAYTEST_PENDING](../gameplay/STAGE_C_README.md):15 analiz, wybór wzorców, pięć eksperymentów i [research Mario Kart](../gameplay/stage_c/MARIO_KART_RACING_RESEARCH.md). **Własne sesje0/15**, brak pomiarów mobile, ekonomii i first-fun. Pełny odbiór nadal wymaga12–15 rzeczywistych sesji według [protokołu](../gameplay/stage_c/PLAYTEST_PROTOCOL.md), nie zamieniamy go w samo czytanie opisów.

33 decyzje właściciela rozstrzygnęły część dawnych propozycji. Nie oznacza to wykonania badań skuteczności. Weryfikuj istotne wzorce: odkrywanie, budowanie, krótkie zadania, współpraca i sport, zachowując dobrowolność oraz brak grindu.

## D: edukacja i wykonawczy opis zachowania

**SPEC_READY / TEACHER_REVIEW_PENDING.** [Punkt wejścia](../education/STAGE_D_README.md). Jest [audyt40 ID](../education/stage_d/M01_M40_AUDIT.md), [źródła z konkretnymi punktami](../education/stage_d/CURRICULUM_SOURCES.md), [osiem kart](../education/stage_d/PILOT_INDEX.md), [dane i kontrola810 konfiguracji](../education/stage_d/TEST_VECTORS.md), [silne UI](../ux/LEARNING_UI_CONTRACT.md). Kontrola810 dotyczy rachunkowej domeny, nie uruchomienia810 testów gry.

Następne czynności D00–D06: spójność decyzji, aktualność i pełność mapowania programu, korekty wszystkich40 kart, dopracowanie8 pilotów, recenzja nauczyciela, odbiór zakresu. Nie nadawaj wszystkim tematom IV–VI etykiety „klasa4”. Nie dodawaj M41+. Właściciel nie musi ponownie odpowiadać na pytania Q01–Q33.

## E: warsztat i transfer assetu

Dopiero po osobnym zleceniu technicznym: audyt faktycznych ścieżek UE/Blender/Material Forge, licencji i jednego reprezentatywnego modelu. Osobne prywatne miejsce testowe, kopia mapy, niezależny namespace danych. Jeden asset ma dać powtarzalny import/aktualizację z poprawną skalą, PBR, UV i kolizją. Rzeczywisty dowód w Roblox, nie sam render z innego silnika. [Pipeline](../tech/CONTENT_PIPELINE.md), pakiety P00/P06.

## F: masterplan i wielka mapa

Całość planować dla proponowanych7 stref i badać warianty8192/16384 studów z realistyczną gęstością obiektów. Jedna mała próbka M34 sprawdza interakcję, NIE kończy docelowego świata. [Urządzenia](../tech/DEVICE_ACCEPTANCE.md): iPad6 obowiązkowy, G54, RedmiNote14 4G i RTX2070/i5gen10/32GB. Cel16 prawdziwych graczy, w tym skupienie przy jednym punkcie;1–4 na przygodę, liczba wyścigowa osobno.

Bramka: wydajność i streaming na rzeczywistych urządzeniach. Nie zmniejszać zakresu świata ani nie wyrzucać iPada po cichu. Budżet szczegółu można ograniczać, nie zasady i widoczność przeszkód. Wybór jednego/wielu Places podlega benchmarkowi.

## G: prawa, bezpieczeństwo i publikacja

Prawa do materiałów i symboli, zasady współpracy/publikacji Roblox oraz prywatność sprawdzane ponownie przed premierą. [Dotychczasowy research](../legal/RIGHTS_AND_COMPLIANCE.md) nie jest niezmiennym regulaminem. Brak publicznego rankingu matematyki, zbierania danych szkoły i płatnej przewagi. Nie publikować surowych cudzych assetów z YACS bez praw.

## H: kontrolowana implementacja po upoważnieniu

P00 izolacja → P01 model zadania → P02 dotyk M34 → P03 serwer/zapis → P04 solo/paszport/pokój → P05co-op → P06 pipeline/masterplan → P07 czysty sport → P08 profile/boty/gadżety → P09 osiem kart i wydarzenie → P10 regresja i sprzęt. Szczegółowe wejścia i ograniczenia są w [EXECUTION_PACKETS](EXECUTION_PACKETS.md). Nie implementować całego łańcucha w jednym PR.

## Definition of Done

Dokument: źródła, komplet ID, instrukcje, testy i granice. Kod: rzeczywisty wynik unit/Studio. Sprzęt: fizyczne urządzenia i odpowiedni skład. Dydaktyka: review konkretnej wersji. Wygląd: właściciel zatwierdza. Publikacja: osobna decyzja i aktualne polityki. [Macierz odbioru](ACCEPTANCE_MATRIX.md) rozdziela wszystkie te warstwy. PASS jednej nie oznacza pozostałych.
