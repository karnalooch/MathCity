# Progres, EXP, nagrody i brak grindu

2026-10-19. Q03–Q07,Q11–Q12,Q16,Q21,Q26. **Reguły właściciela wiążące; formuły i wartości niżej są TEST_DEFAULTS do symulacji, nie zatwierdzonym balansem.** Nie implementowano systemu. [Decyzje](../../planning/OWNER_DECISIONS_20261019.md).

## 1. Rozdzielone wielkości

`adventureCompletion`: odkrycia, cele i etapy; odblokowują historie. `adventureXP`: poziom i kosmetyka, nigdy przepustka do misji. `walletCoins`: jedna podstawowa waluta zdobywana w grze. `taskMoney`: pieniądze/liczmany w ćwiczeniu, nie saldo. `mastery`: prywatna wiedza per skill. `raceMedals`: osiągnięcia sportowe. Nie przeliczaj żadnych EXP na mastery; nie odejmuj pieniędzy konta za zły wynik zadania.

Wymagania odblokowania: odkryty punkt, ukończony etap albo rola. Brak `minimumAdventureLevel` w definicji misji. EXP może dać tytuł i dekorację bez wzmacniania wyścigowych statystyk.

## 2. Klasyfikacja nagrody

| Rodzaj | Kiedy | Co nie odnawia |
|---|---|---|
| FIRST_OBJECTIVE | Pierwsze spełnienie stabilnego celu osobistego | seed, pomoc, rewizja tekstu, reconnect, zmiana drużyny |
| STORY_CHAPTER | Własne wymagane etapy rozdziału ukończone | cudze wykonanie, dołączenie przy finale |
| PRACTICE | Kolejna kompletna próba rodziny | nie jest drugą nagrodą główną |
| HELP | Własna realna praca w etapie, którego inny uczestnik wcześniej nie ukończył | obecność AFK, wielokrotne wejście partnera, bot |
| SPORT_FINISH | Pierwsze ukończenie próby na danej trasie/regule nagrody | nowy rekord, nowy pojazd, drobny patch |
| SPORT_TIER | Pierwsze osiągnięcie brązu/srebra/złota | powtarzanie progu; więcej miejsc w tabeli |
| COSMETIC_CHOICE | Wybór z przyznanej puli jednorazowej | odświeżenie ekranu wyboru |

Każda definicja ma `rewardObjectiveId` oddzielne od `taskFamilyId`, `assignmentId` i wersji fizyki. Acknowledgement UI nie jest drugim zdarzeniem finansowym.

## 3. Rzeczywista współpraca

Premia występuje przy wspólnym, kooperacyjnym etapie z co najmniej dwoma ludźmi i potwierdzonym własnym wkładem. Nie wystarczy party membership, bliskość postaci, kliknięcie „gotów” lub wyścig przeciwko innym. Przygotowanie wspólnych zawodów może dawać co-op; rywalizacja na trasie sama nie. Bot nie liczy się jako partner.

Potwierdzenie wkładu nie zależy od tempa odpowiedzi i korzystania z pomocy. Każdy realizuje swoją porcję pracy. Po zaakceptowaniu wkładu odejście partnera nie odbiera tego faktu; podstawą jest serwerowy zapis ukończonego etapu, nie lista osób online w chwili wysłania animacji nagrody. Nie karz przerwy na czytanie klasyfikacją AFK. Ogranicz nadużycia dowodem zadania, nie liczbą kliknięć na minutę.

## 4. EXP: jawny wariant do pierwszej symulacji

Dla aktywnego uczestnika i: B_i = bazowe EXP za porównywalną porcję pracy; r_i = czynnik powtórki; t_i = bonus współpracy; c_i = bonus doganiania. Propozycja:

`grantXP_i = floor(B_i × r_i × (1 + t_i + c_i))`.

TEST_DEFAULTS: t=0,20 przy kwalifikowanej współpracy, inaczej0. Poziomy aktywnych ludzkich współuczestników utrwal na starcie etapu. L_ref = mediana ich poziomów z wyłączeniem gracza i (dla2osób: poziom partnera; dla parzystej liczby wartości średnia środkowych). c=min(0,30; max(0;L_ref−L_i)×0,03), ale tylko dla współpracy z realnie aktywnym partnerem. Zmiana składu wpływa dopiero na następny etap. Nie korzystaj z poziomu matematyki, liczby pomyłek, ustawień trudności czy pamięci urządzenia.

Przykład dla r=1 i B=100: solo100; senior zespołu120; osoba10 poziomów poniżej referencji150. To przykład projektu, **nie odtworzona formuła Octopath Traveler II**. Za pierwszą porównywalną pracę na różnych poziomach matematycznych podstawę ustaw jednakową. Różne bazowe wartości dopuszczalne dla faktycznie różnych zakresów pracy, nie dla wyższej klasy jako takiej.

Robocza krzywa kosztu przejścia L→L+1: `T(L)=100+25×(L−1)` dla L≥1. To łagodny punkt wyjścia. Po nagrodzie przetwarzaj wielokrotne awanse pętlą z limitem wynikającym z poprawnego EXP; nie gub nadwyżki. Przykład T1=100,T5=200,T10=325. Przyszła symulacja ma pokazać czas do pierwszych poziomów i wyrównywanie drużyny; sama formuła nie jest obietnicą tempa.

## 5. Powtórki i pomaganie

Główne nagrody są przypisane do stałych celów, a nie do liczby zaliczeń. Ćwiczenia są bez ograniczenia dostępu. TEST_DEFAULTS r dla kolejnych kompletów tej samej, już opanowanej rodziny: 0,25, potem0,10, potem0,05. Licznik obejmuje cały profil i rodzinę, nie resetuje się przez seed, zmianę serwera ani zmianę klasy. Konkretne wartości i sposób powrotu do tej rodziny po nowym rozdziale podlegają testom.

**Pomoc nie zmniejsza r.** Jeżeli celem jest nadal uczenie się, nie uznaj błędów, liczby podpowiedzi i długiego czasu za nadużycie. Nie twórz także premii ekonomicznej za celowe błędy: prawo do głównej wypłaty zależy od celu, a nie od udawanego braku umiejętności. UI pokazuje, że wyjątkowa nagroda została już zdobyta, zanim dziecko wybierze powtórkę.

Rzeczywista pomoc nowemu uczestnikowi korzysta z osobnego, kontrolowanego kanału HELP zamiast najniższego r opanowanej próby. Roboczo r_help=0,50 i normalne t/c. Kwalifikacja: serwer potwierdza, że odbiorca rzeczywiście pierwszy raz ukończył ten cel, pomocnik wykonał własną rolę, a dany udział nie był już rozliczony. Nie naliczać pomocy wielokrotnie na jednego nowego kolegę ani per każde kliknięcie. Jeśli first objective i help zachodzą naraz, jedna spójna wypłata według pierwszego celu, nie suma dwóch podstaw.

To nie gwarantuje wykrycia każdej farmy nowych kont. Potrzebne ograniczenie przyrostu powtarzalnych helper rewards i testy ekonomii bez piętnowania rodzin grających z jednej sieci. Nie blokuj osób po IP, nazwie ani przypuszczalnym wieku. Progi antyabuse mają być jawnie testowane i nie odbierać już należnego first objective.

## 6. Nagrody rzeczowe i pokój

Podstawowe meble/kolory: sklep za walutę gry. Pamiątki miejsc: stały cel albo wybrany wariant, z widoczną drogą do zdobycia. Brak losowej płatnej skrzynki; brak „zapłać za odpowiedź”. Przedmioty startowe przyznawane niezależnie od tutorialu. Wybór nagrody atomowy: próba kliknięcia dwóch wariantów naraz daje jeden wybrany przedmiot i jedno zużyte uprawnienie.

## 7. Sport i wyróżnienia

Pierwsze poprawne ukończenie daje pewną nagrodę nawet bez medalu; każdy próg raz. Przy pierwszym wyniku złotym przyznaj należne, dotąd nieodebrane nagrody niższych progów w jednej operacji albo jedno skumulowane uprawnienie, a nie zmuszaj do specjalnie gorszych przejazdów. Propozycja wdrożenia: zachowaj trzy flagi medali i finishClaim. Rekord sam nie generuje nowego grant. Nie płacić za pozycję w tabeli znajomych.

## 8. Odbiór ekonomii

Symuluj solo, równą drużynę, różnicę1/5/10/30 poziomów, nieobecnego seniora, bota, powtarzanie seedu, zmianę klasy, assisted oraz helper pierwszy/kolejny. Obserwuj wypłaty, czas aktywności i możliwość zdobycia kosmetyki różnymi drogami; nie optymalizuj dla niekończącego się czasu w grze. Raport ma uczciwie pokazać nadużycia. Trwałość i jednokrotność: [kontrakt serwera](../../tech/DATA_AND_SERVER_CONTRACT.md).
