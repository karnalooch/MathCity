# Etap C: mechaniki Roblox i ich adaptacja do MathCity

**Data researchu: 2026-10-19. Stan: SOURCE_RESEARCH_COMPLETE / PLAYTEST_PENDING. Cały Etap C: PARTIAL, nie PASS.**

## Wynik w jednym zdaniu

Rekomendowana formuła to **przygodowe Siedlce z odkrywaniem miejsc, krótkimi zadaniami, budowaniem i współpracą**, a nie sama wieża quizowa, bezcelowy hangout ani symulator losowania nagród.

Przeanalizowano publiczne materiały **15 konkretnych gier**. Potwierdzono adresy, identyfikatory miejsc i autorów, porównano opisane przez nich czynności, progresję i nagrody. Użyto dokumentacji Roblox oraz komunikatów twórców. **Nie wykonano własnych rozgrywek, oglądania nagrań ani pomiarów na telefonie. Liczba sesji manualnych: 0/15.** Czas pierwszej nagrody, FPS, rzeczywisty onboarding i ceny pozostają niezmierzone.

## Pakiet dokumentów

| Plik | Zawartość |
| --- | --- |
| [SOURCES_AND_METHOD.md](stage_c/SOURCES_AND_METHOD.md) | Źródła pierwotne, daty, ograniczenia danych, identyfikacja oryginalnych gier |
| [BENCHMARK_15_GAMES.md](stage_c/BENCHMARK_15_GAMES.md) | 15 kart: fakty z opisu, interpretacja, propozycja dla MathCity, plan obserwacji |
| [TRANSFER_MATRIX.md](stage_c/TRANSFER_MATRIX.md) | Ranking wzorców i przypisanie do istniejących M01–M40 oraz miejsc Siedlec |
| [MATHCITY_EXPERIENCE.md](stage_c/MATHCITY_EXPERIENCE.md) | Pętla gry, scenariusz pierwszych 20 minut, transport, dłuższa sesja i powroty |
| [MVP_AND_ACCEPTANCE.md](stage_c/MVP_AND_ACCEPTANCE.md) | Pięć małych eksperymentów do późniejszego wykonania, testy akceptacyjne i kolejność |
| [ECONOMY_SAFETY_AND_SOCIAL.md](stage_c/ECONOMY_SAFETY_AND_SOCIAL.md) | Pięć antywzorców, uczciwe nagrody, komunikacja i bezpieczeństwo |
| [PLAYTEST_PROTOCOL.md](stage_c/PLAYTEST_PROTOCOL.md) | Protokół 1/5/10/20 minut, rejestr 15 × NOT_RUN, testy mobilne i kooperacyjne |
| [WEAK_LLM_RUNBOOK.md](stage_c/WEAK_LLM_RUNBOOK.md) | Instrukcja używania ustaleń bez dopowiadania wyników i rozbudowy zakresu |

## Pięć najważniejszych rekomendacji

1. **Paszport odkrywcy i zadania w przestrzeni:** widoczny ratusz, ślad do kolejnego miejsca, znane nagrody za odkrycia. Wzorce G01/G15.
2. **Krótka zabawa związana z miejscem:** minigry przy atrakcjach, nie centralna kolejka odcinająca gracza od miasta. Wzorce G13/G09.
3. **Zbuduj, sprawdź, popraw:** tratwa lub pomost na Muchawce, z ograniczoną biblioteką elementów. Wzorzec G12.
4. **Wspólne miejskie zadania bez wymaganego czatu:** poczta, dostawy i kompletowanie wydarzenia. Wzorce G14/G05.
5. **Widoczny własny postęp bez grindu:** klomb, paszport i kosmetyka roweru; wzrost jako rezultat pracy, nie przymus pilnowania timera. Wzorce G03/G02.

To **rekomendacje projektowe**, nie statystycznie dowiedzione przyczyny sukcesu tych gier i nie decyzje właściciela.

## Ustalenia, które zmieniają projekt

- Fisch opisuje kontrolowanie wskaźnika, a Fish It! szybkie klikanie. Dla dzieci proponujemy sterowanie spokojne i opcję przytrzymania. Nie wrzucać obu gier do jednego ogólnego worka „łowienie”. [G06/G07 w źródłach](stage_c/SOURCES_AND_METHOD.md).
- Na platformie część odbiorców nie ma swobodnego czatu. Kooperacja musi być czytelna dzięki rolom, stanowi obiektów i automatycznym komunikatom celu. W październiku 2026 Roblox udostępnił konfigurację własnych, moderowanych Quick Words. Nie projektujemy obejścia komunikacji. [S08/S10](stage_c/SOURCES_AND_METHOD.md).
- Roleplay nie jest automatycznie tym samym co social hangout. Docelową kategorię i zawartość trzeba rzetelnie zadeklarować; samo dodanie tabliczki z zadaniem nie rozwiązuje wymagań publikacji. [S09/S11](stage_c/SOURCES_AND_METHOD.md).
- Rozmiar miasta sam nie daje powodu do grania. Najpierw badamy czas do pierwszej czynności i kolejnego ciekawego miejsca. [S04/S05/S06](stage_c/SOURCES_AND_METHOD.md).

## Zgodność z obecnym repozytorium

Punkt odniesienia: `ac942dd85f599b095af7d0922e88288175402a08`. Uwzględniono Etap A: **41 miejsc, 40 kandydatów minigier oraz propozycję 7 stref**, w tym Sekułę. Nie wracamy do starszego uproszczenia sześciu dzielnic. `N01` oznacza Zalew Muchawka; `S02` jest osobnym Parkiem Wodnym. Górka Grześ pozostaje kandydatem wymagającym potwierdzenia lokalizacji.

Nie dodano nowych identyfikatorów M41+, nie zmieniono programu szkolnego, nie zmieniono mapy ani kodu. Przypisanie G2/G3/G4 w propozycjach nadal wymaga audytu nauczyciela. Nazwy i liczby w nowych scenariuszach są fikcją gry, nie danymi geograficznymi Siedlec.

## Warunek zamknięcia Etapu C

Dokumentacja dostarcza korpus źródeł, porównanie, wybór wzorców i propozycję rozgrywki. Pełny PASS wymaga **12–15 rzeczywistych sesji**, obserwacji początku gry, testów istotnych wzorców na mobile i we dwoje oraz aktualizacji wniosków po tych obserwacjach. Właściciel zatwierdza wybór zakresu. Brak pomiaru nigdy nie jest wynikiem zero.
