# Kontrakt zadania, generatora, pomocy i adaptacji

2026-10-19. Q01,Q02,Q07,Q15,Q22,Q24–Q26. Specyfikacja przyszłej implementacji; nazwy pól projektowe. Zasady są wiążące, liczbowe parametry adaptacji poniżej to **TEST_DEFAULTS**, nie zweryfikowany algorytm dydaktyczny.

## 1. Definicja i instancja to różne obiekty

Definicja: `minigameId`, `taskFamilyId`, `taskRevision`, `skillIds`, `curriculumProfileIds`, `sourceAnchors`, `gradeReviewStatus`, `bandId`, `parameterDomain`, `generatorId`, `validatorId`, `instructionKey`, `inputSchema`, `uiHelpSteps`, `mathHintSteps`, `guidedSteps`, `rewardObjectiveId`, `masteryPolicyVersion`. Instancja: `assignmentId` nadane przez serwer, `ownerUserId`, `adventureRunId`, `stageId`, niezmienny `seed`, zapisane `parameters`, wersja definicji, `uiState`, uporządkowane `objectState`, poziom użytej pomocy i identyfikatory potwierdzonych działań.

Nie mylić `taskRevision` z nagrodą. Zmiana treści poprawiająca literówkę albo seed nie tworzy nowego `rewardObjectiveId`. Po wygenerowaniu zapisuj też parametry, aby aktualizacja PRNG nie zmieniła wznowionej próby.

## 2. Granice generatora

Nie losuj dowolnych działań i nie wysyłaj do LLM pytań użytkownika. Generator wybiera z zatwierdzonego zakresu. `EqualSharing`: wybierz g i q, wylicz n=g×q; tylko g>0 i ograniczona liczba obiektów. `ClockAdd`: operuj na całkowitych minutach; wariant bazowy kończy się tego samego dnia; daty następnego dnia tylko w osobnym zatwierdzonym wariancie. `Money`: całkowite grosze, cena zakupu≤budżet. `Symmetry`: odbij współrzędne względem podanej osi. `OpenRows`: wylicz wszystkie dzielniki pasujące do granic planszy.

Przy każdym szablonie funkcja `validateParameters` sprawdza domenę przed pokazaniem UI. Brak poprawnego wariantu daje wskazany w karcie ręczny przykład zapasowy. Bez nieograniczonej pętli prób. Seed, klasa ani widok kamery nie są dowodem poprawności odpowiedzi.

## 3. Stan próby

`OFFERED → ACTIVE → CHECK_REQUESTED → FEEDBACK → ACTIVE` przy niepoprawnym wyniku. Poprawny wynik: `CHECK_REQUESTED → COMPLETED → GRANT_PENDING → GRANT_COMMITTED`. Pomoc: `ACTIVE ↔ GUIDED`. Wyjście: `ACTIVE/GUIDED → PAUSED → ACTIVE/GUIDED`. Błąd sieci: `SYNC_WAIT`, bez wyniku oceny. Zmiana na łatwiejsze zadanie zamyka starą instancję jako `REPLACED`, nie dodaje nagrody i nie tworzy błędu ucznia; nowe instancje jawnie mają inne dane. Pomoc, reconnect i zła odpowiedź NIE są taką zamianą.

Tryb guided zapisuje najwyższy wykorzystany stopień pomocy; powrót do ACTIVE tego nie czyści. Status zakończenia: `INDEPENDENT` albo `ASSISTED`. `ABANDONED`, `TECHNICAL_ERROR`, `REPLACED` nie dowodzą nieumiejętności.

## 4. Pomoc obsługowa a matematyczna

`UI_HELP`: jak wybrać deskę, obrócić element, kliknąć slot, otworzyć mapę. Może wskazać wszystkie legalne sloty, ale nie jedyny matematycznie poprawny cel. Nie obniża samodzielności.

`MATH_HINT`: wskazuje relację, grupę do porównania, rozkład działania albo poprawny krok. Odnotowuje ASSISTED. Podstawowa nagroda nie spada.

`GUIDED`: podział na małe działania wykonywane przez dziecko, np. rozłóż po jednej desce do trzech grup. Przykład na innych danych również jest pomocą matematyczną, gdy zdradza strategię. Wykonawca nie może nazwać rozwiązania „animacją UI”, aby obejść ocenę.

Informacja po świadomym „Sprawdź” może powiedzieć, który warunek nie jest spełniony (brak elementu, nierówne grupy); automatyczne pokazanie poprawnej liczby lub kierunku jest już hint. Uczeń może sam poprawić błąd bez kary; ta próba nie jest jednak jedynym dowodem mastery. Nie liczyć dotykowych chybień, przewijania lub anulowania jako błędy matematyczne.

## 5. Walidacja i prywatność

Serwer wylicza rezultat z własnego zadania i poprawnie ograniczonej odpowiedzi. Nie przyjmuje `correct=true`, kwoty EXP, liczby prób czy prywatnych umiejętności od klienta jako faktu. W zadaniu obiektowym sprawdza dozwolone ID, każdą sztukę raz, brak obcych elementów, granice slotów i spełnienie wszystkich warunków. Odpowiedź otwarta jest zbiorem warunków, nie porównaniem screenshotu.

Klient dziecka zna własne obiekty i UI, ale nie otrzymuje serwerowego magazynu odpowiedzi całego kontentu ani danych edukacyjnych kolegi. Ukrycie rozwiązania przed exploiterem nie jest gwarancją dydaktyczną; kluczowe jest prawidłowe naliczanie i prywatność.

## 6. Model umiejętności

Osobno per `skillId`: `currentBand`, `learningState`, potwierdzone przykłady, stopień pomocy, ostatnie wersje definicji i propozycja następnego kroku. Nie zapisuj nagrań głosu, prawdziwej szkoły i nieograniczonego logu kliknięć. Poziom przygody i ustawienia sportu nie są wejściem adaptacji.

TEST_DEFAULTS do pilota: 3 różne poprawne samodzielne próby, z przynajmniej 2 kontekstów/układów i ponownym sprawdzeniem po innej aktywności, mogą zaproponować `Rozwiązuję samodzielnie` dla wąskiego skill+band. Nie wymagaj codziennego logowania. Nie używaj tego progu jako diagnozy klinicznej ani oceny szkolnej. Jedna rodzina zadania nie uprawnia do stwierdzenia „opanował całą geometrię”.

Po dwóch świadomie sprawdzonych błędach zaproponuj pomoc; nie włączaj jej przymusowo. Długi czas bez odpowiedzi proponuje pokaz obsługi i przerwę, nie obniża umiejętności. Po sukcesach proponuj następny zatwierdzony band w obrębie klasy; nie przeskakuj samoczynnie do programu wyższej klasy. Ręczna zmiana poziomu nie kasuje paszportu, nagród ani wcześniejszych osiągnięć; nie zwiększa catch-up EXP.

## 7. Rozdzielenie nauki i ekonomii

Powtórzenie opanowanej rodziny jest nadal ćwiczeniem, ale nie kolejną główną wypłatą. Pomoc nie jest sygnałem nadużycia. Nowy seed nie odnawia nagrody; `INDEPENDENT` nie daje większej podstawowej nagrody niż `ASSISTED`. Błąd walidatora lub brak internetu nie nalicza porażki. Wynik wspólnej sceny nie zapisuje mastery u osoby, która tylko patrzyła.

## 8. Testy obowiązkowe

Stałość parametrów po błędzie/pomocy/wznowieniu; deterministyczne generowanie; skończona domena; wszystkie dopuszczone rozwiązania otwarte; zła jednostka; brak obiektów; obce ID; nieskończone liczby; UI_HELP vs MATH_HINT; brak wpływu sportu/EXP na skill; brak publicznego odczytu mastery. Przykłady: [TEST_VECTORS](TEST_VECTORS.md).
