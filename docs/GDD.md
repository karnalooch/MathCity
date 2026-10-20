# MathCity: Game Design Document v3 po decyzjach właściciela

2026-10-19. **APPROVED_DESIGN dla Q01–Q33; SPEC_READY dla kontraktów; nowa implementacja NOT_STARTED.** Poprzedni GDD v2 pozostaje w [historii pliku](https://github.com/karnalooch/MathCity/blob/030c8637010525ec0533daffe44c2e3f963bc1da/docs/GDD.md), a działająca Wieża v1 w [legacy](legacy/GDD_TOWER_V1.md). Nie zmieniono mapy.

## 1. Cel i granice świata

Duże, kolorowe, autorskie Siedlce w Roblox. Rozpoznawalne zabytki, parki, sport, Sekuła i flagowy Zalew Muchawka, ale nie odtworzenie geografii1:1. Swobodna eksploracja i lokalne przygody matematyczne klas2–4. Jedna wspólna mapa z indywidualnym zakresem zadań, nie dzielnice zamknięte według klasy.

Robocze7 stref: Jackowo, Ogrody Aleksandrii, Kolejowo, Muchawkowe Wyspy, Neonowe Błonia, Aleja Kultury, Sekuła: Leśna Ekspedycja. Nazwy i układ pozostają propozycją artystyczną. [Atlas41 miejsc](world/STAGE_A_README.md), [Muchawka](world/atlas/MUCHAWKA_FEATURE.md), [masterplan](world/DISTRICTS_MASTERPLAN.md). `N01` ≠ `S02`; narciarstwo Sekuły biegowe; lokalizacja Górki Grześ nadal otwarta. Wielkość8192/16384 studów jest hipotezą techniczną, nie wybraną granicą mapy.

## 2. Pętla gry i postęp

Odkryj miejsce → wybierz lokalną przygodę → wykonaj zadania w świecie → zobacz rezultat → zdobądź osobistą pamiątkę/wybór kosmetyczny → wróć do zwiedzania albo innej historii. Wspólne czasowe wydarzenia ożywiają miasto, a osobisty postęp pozwala każdemu przeżyć historię niezależnie od innych.

EXP daje poziomy, rangi i kosmetykę. Misje odblokowują dokonania i etapy, nie wymagany poziom EXP. Współpraca premiowana u aktywnych uczestników, początkujący otrzymują ograniczony bonus doganiania zależny od poziomu przygody. Nowe zadania i realna pomoc są ważniejsze niż powtarzanie opanowanego ćwiczenia. [Reguły nagród](gameplay/specs/PROGRESSION_AND_REWARDS.md). Wartości formuł w specyfikacji to TEST_DEFAULTS, nie zatwierdzony balans.

## 3. Edukacja

Wybór klasy na start i późniejsza adaptacja osobno dla skill. Matematyka bez presji czasu. Pierwsze przykłady ręczne, następne z kontrolowanych szablonów; brak generatywnego chatbota w runtime. Liczby stałe podczas próby. Zadania zamknięte i nieliczne otwarte z kilkoma równoważnymi rozwiązaniami. Silne podpowiedzi UI, interaktywne wspólne rozwiązywanie, bez kar za błąd. Głos po polsku później.

Pomoc obsługowa ≠ matematyczna. Guided kończy przygodę i daje podstawową nagrodę, ale nie niezależne mastery. Prywatna mapa umiejętności ma etykiety Poznaję/Ćwiczę/Rozwiązuję samodzielnie i nie jest publicznym rankingiem. [Etap D](education/STAGE_D_README.md), [model](education/stage_d/TASK_MODEL_AND_ADAPTATION.md), [UI](ux/LEARNING_UI_CONTRACT.md).

Źródła wymagają wersjonowania: [konkretne punkty i roczniki](education/stage_d/CURRICULUM_SOURCES.md). Etap IV–VI nie oznacza automatycznie klasy4. Audyt wszystkich M01–M40 jest dokumentacyjny; osiem pilotów to rekomendowany początek, nie komplet całej podstawy.

## 4. Własne miejsce i eksploracja

Pokój/mieszkanie i podstawowy transport dostępne od startu, niezależnie od tutorialu. Proste dekorowanie, goście bez prawa do niszczenia lub zabierania. Zwykłe wyposażenie za monety gry; wyjątkowe rzeczy za jawne przygody. Paszport pomaga znaleźć zadanie i nagrodę, śledzi jeden cel; sekrety pozostają do odkrywania. Darmowa szybka podróż między poznanymi punktami, bez matematycznego gate i opłat. Nie zalicza tras dostawy/wyścigu.

Krótkie skip/resume wprowadzenie w centrum i późniejsze kontekstowe instrukcje. Główna fabuła odłożona; lokalne serie zadań mają własne zakończenia. [Kontrakt miasta i pokoju](gameplay/specs/EXPLORATION_HOME_ONBOARDING.md).

## 5. Współpraca

Cel16 prawdziwych graczy na serwer; przygody solo lub w ekipie1–4. Każdy ma znaczącą rolę i prywatnie dopasowaną matematykę. Szukanie ekipy dobrowolne, na bieżącym serwerze, bez wymaganego czatu i ujawniania wyników. Dołączenie między etapami, z podsumowaniem i własną rolą; nie daje wcześniejszych nagród. Odejście partnera nie kasuje potwierdzonej pracy ani nie blokuje solo. [Kontrakt drużyn](gameplay/specs/COOP_AND_WORLD_STATE.md).

## 6. Sport i gadżety

Dobrowolne próby na czas; pewna mała nagroda za pierwsze ukończenie, brąz/srebro/złoto raz. Rekordy osobiste i opcjonalne porównanie znajomych, bez globalnej tabeli i bez zapłaty za pozycję w niej. Czyste czasy oddzielone od wyścigów z przedmiotami.

Kilka stylów prowadzenia dostępnych każdemu bez grindu; skórka i poziom nie zwiększają osiągów. Łagodne catch-up przez szanse przedmiotów zgodnie z realną stratą, nie tajne przyspieszanie. Oznaczone boty uzupełniają stawkę i nie udają ludzkiego co-op. Własne warianty banana/turbo/osłony są proponowaną pierwszą pulą, nie zatwierdzonym pełnym katalogiem. [RACING](gameplay/specs/RACING.md), [research Nintendo](gameplay/stage_c/MARIO_KART_RACING_RESEARCH.md).

## 7. Technologia i urządzenia

Roblox jest runtime. **Houdini z warsztatu YACS jest głównym wykonawcą proceduralnego świata i contentu:** HeightFields, erozja, maski, drogi/korytarze, building pads, proceduralne meshe, scatter i eksport. UE, Blender i Material Forge pomagają: UE = lookdev/review, Blender = hero-detail/retopo/UV/cleanup, Material Forge = PBR. Nie tworzymy równoległego mastera świata w UE lub Blenderze. [Houdini-first pipeline](tech/HOUDINI_FIRST_PIPELINE.md). Najpierw H00 terrain, H01 mesh i H02 material, następnie realistyczna makieta wszystkich stref. Mały pilot nie zastępuje wielkiego miasta.

Obowiązkowe punkty odniesienia: iPad6, MotorolaG54, RedmiNote14 4G, PC RTX2070/i5 10.gen./32GBDDR4. iPad6 nie jest opcjonalny; cel30FPS na mobile i60FPS1080p na PC ma zostać zmierzony. Pełne UI dotykowe, funkcjonalne obiekty widoczne na niskiej grafice. [Urządzenia](tech/DEVICE_ACCEPTANCE.md), [serwer i zapis](tech/DATA_AND_SERVER_CONTRACT.md).

## 8. Co nadal nie jest wykonane lub zatwierdzone

Stage A geografia/prawa częściowo otwarte. Stage B w [Draft PR#1](https://github.com/karnalooch/MathCity/pull/1), nie scalać bez decyzji, brak finalnych renderów3D. Stage C ma0/15 rzeczywistych sesji. Stage D nie ma recenzji nauczyciela. Brak nowych testów Studio i urządzeń. Zmienne zasady publikacji, praw do assetów i komunikacji wymagają osobnej bramki przed premierą.

Nie wybrano finalnego rozmiaru mapy, stylu S1/S2/S3, pełnej fabuły, monetyzacji, dokładnych statystyk pojazdów, cen, progów EXP i czasów medali. Nie wolno wykonywać implementacji całej listy tylko dlatego, że zapisano plan.

## 9. Co wykonawca robi następne

[START HERE](planning/WEAK_LLM_START_HERE.md) → [pakiety D00–D06](planning/EXECUTION_PACKETS.md) → źródła/review i domknięcie kart. Późniejsze P00–P10 wymagają zlecenia kodowego. [Macierz odbioru](planning/ACCEPTANCE_MATRIX.md) rozdziela dowód dokumentacyjny, logiczny, Studio, sprzęt i pedagogikę. [33 decyzje](planning/OWNER_DECISIONS_20261019.md) są źródłem prawdy przy każdym konflikcie z wcześniejszym researchiem.