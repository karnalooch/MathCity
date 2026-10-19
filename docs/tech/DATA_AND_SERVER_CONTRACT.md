# Kontrakt serwera, danych i jednokrotnej nagrody

2026-10-19. **Projekt przyszłego kodu; nie opis obecnej implementacji.** Przed zmianą obejrzyj `src/server/LeaderstatsAndDataStore.luau` i testy, zamiast zakładać ich zgodność z tym dokumentem. Stara mapa i magazyn `MathTowerData_v1` pozostają nietknięte podczas eksperymentów. [START HERE](../planning/WEAK_LLM_START_HERE.md).

## 1. Udokumentowane podstawy Roblox

Serwer ma sprawdzać kontekst, uprawnienia, typy, rozmiary i zakres danych klientów; sam typ number nie wyklucza NaN/Inf. Dotyczy to również wyzwalanych interakcji, nie tylko nazwanych RemoteEvents. Źródło: [Client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary).

`UpdateAsync` służy do aktualizacji pojedynczego klucza, a callback nie może wykonywać operacji yield. Nie zakładaj atomowej transakcji obejmującej cztery profile drużyny. Źródło: [Data stores](https://create.roblox.com/docs/cloud-services/data-stores). Pozostałe nazwy modułów i schematy niżej są projektem MathCity, a nie gotowym API Roblox.

## 2. Minimalny model danych profilu

| Pole | Przeznaczenie / ograniczenie |
|---|---|
| schemaVersion, profileRevision | wersja danych i kolejność zapisu; migracja jawna |
| sessionLease | jeden aktywny właściciel zapisu profilu; kontrolowana utrata/wznowienie |
| starterEntitlements | pokój i podstawowy transport, przyznawane raz |
| adventureXP, walletCoins | nieujemne liczby całkowite w zakresie projektu |
| completedObjectiveIds | trwały zbiór stabilnych celów osobistych |
| storyStageCompletions | zbiór etapów, nie samo highestStage |
| rewardClaimFlags | trwałe first/medal/choice uprawnienia, niezależne od seedu i patcha |
| activeAssignment | jedna aktywna oceniana próba na gracza w pierwszym prototypie |
| issuedSequence, resolvedSequence | monotonnie rosnące identyfikatory do deduplikacji |
| practiceCounters | powtórki per rodzina, nie reset po zmianie seedu/serwera |
| inventory, roomLayout | własność przedmiotów i legalny układ pokoju |
| discoveries, trackedObjective | poznane punkty i jeden aktywny cel |
| mastery | prywatne skill/band/evidence z ograniczonym rozmiarem historii |
| raceResults, medalClaims | wyniki z wersją reguł oraz stabilne flagi jednorazowych nagród |

Nie dodawać nieograniczonego logu kliknięć/odpowiedzi, nagrań, szkoły, adresu ani prawdziwego imienia do profilu. Dla edukacji przechowywać potrzebne podsumowania i wersje, nie pełny publiczny dziennik dziecka. Ograniczenie historii nie może usuwać flag niezbędnych do zapobiegania powtórnym nagrodom.

## 3. Proponowane granice modułów

TaskDefinitionRegistry zna recenzowane szablony. TaskAssignmentService przydziela dane. TaskValidator oblicza prawdziwy wynik. LearningStateService aktualizuje prywatne umiejętności. AdventureService zna etapy i role. PartyService organizuje dobrowolne drużyny. RewardService wylicza uprawnienie. ProfileStore jako jedyny zapisuje trwały profil. RaceService zna trasę, checkpointy, czas i gadżety. UI pokazuje wynik, nigdy go nie zatwierdza.

Najpierw sprawdź istniejące odpowiedniki; nie dodawaj drugiego systemu profilu konkurującego ze starym. W testowym miejscu stara ekonomia ma być wyraźnie odłączona od nowych celów, a nie równocześnie naliczać nagrody.

## 4. Polecenia klienta to intencje

| Intencja projektu | Minimalne dane klienta | Serwer rozstrzyga |
|---|---|---|
| StartTask | minigameId/roleId | dostępność, właściwy profil, assignmentId, seed i parametry |
| MoveTaskObject | assignmentId, actionSeq, objectId, slotId | właściciela, dozwolone obiekty/sloty, kolejność |
| CheckTask | assignmentId, actionSeq | rezultat z aktualnego zatwierdzonego stanu; brak correct=true |
| RequestHint | assignmentId, hintId | uprawnienie i zapis stopnia pomocy przed jej ujawnieniem |
| PauseTask | assignmentId | stan do wznowienia i potwierdzenie zapisu |
| RequestJoin | partyId, invitation/offerId | serwer, slot, zgoda i granica etapu |
| FastTravel | destinationId | odkrycie, stan trasy, gotowość celu |
| ClaimChoice | rewardObjectiveId, optionId | przyznane uprawnienie, legalny wybór, jednokrotność |
| PlaceDecoration | itemId, roomSlotId | właściciela pokoju, inventory, limit i położenie |
| UseRaceItem | raceId, itemSlot, intencja kierunku | legalny przedmiot, stan rundy, cele i efekt |

Nie przyjmować od klienta dowolnych ścieżek instancji, kwot nagród, cen, minigame expectedAnswer, levelu do catch-up, gotowej listy medalClaims czy klasy innych graczy. Odrzuć pola nieprzewidziane przez schemat. Ogranicz długość stringów, liczbę elementów i częstotliwość intencji osobno dla każdej kategorii. Techniczne limity chronią serwer, nie stanowią płatnego cooldownu podróży ani timera nauki.

Odpowiedź serwera: requestId, assignmentId, authoritativeRevision, wynik protokołu, dane UI dozwolone temu graczowi. UI ignoruje odpowiedzi starsze od zastosowanej rewizji. Późna odpowiedź do zamkniętego assignment nie kończy innej, nowej minigry.

## 5. Jednokrotne rozliczanie

W pierwszym prototypie serializuj operacje jednego profilu. Przed pokazaniem nowego zadania przydziel trwały `issuedSequence` i zachowaj parametry assignment. Najwyżej jedna nierozliczona próba oceniana upraszcza dowód; nie uruchamiaj równolegle drugiej bez rozszerzenia protokołu.

Po poprawnej odpowiedzi:
1. Waliduj stan zadania i wkład gracza na serwerze; przygotuj niezmienne dane rozliczenia.
2. W jednej operacji profilu sprawdź wersję/sesję, `resolvedSequence`, stan activeAssignment i stałe flagi nagród.
3. Jeśli zdarzenie już rozliczone, zwróć aktualny stan bez dodawania XP/monet/przedmiotów.
4. Jeśli nowe: zapisz completion, należny grant, inventory/flags, evidence oraz nowy resolvedSequence razem. Usuń/zamknij assignment w tej samej aktualizacji.
5. Dopiero po potwierdzeniu trwałości powiadom UI o nagrodzie. Pending ma osobną prezentację.

Callback aktualizacji jest powtarzalny i bez skutków ubocznych: nie wysyła RemoteEvents, nie przyznaje badge, nie losuje ponownie i nie wywołuje innego magazynu. Wszystkie losowe wybory, identyfikatory oraz parametry rozliczenia przygotowane wcześniej. Przy powtórzeniu callbacku rezultat nie może rosnąć. Pseudokod jest wymaganiem projektu, nie gotową biblioteką sesji.

Monotoniczny resolvedSequence pozwala odrzucić stare próby również po usunięciu krótkiej historii ich receiptów. `completedObjectiveIds` i kluczowe claimFlags pozostają trwałe. Nie czyść deduplikacji co kilka minut, żeby stare żądanie znowu wypłaciło nagrodę. Niezależne zakupy/medale także mają stabilny klucz uprawnienia albo własną serializowaną sekwencję operacji; nie wkładaj ich w sequence edukacji bez jawnego rozdzielenia.

## 6. Awaria i sesja

Nieudany odczyt nie oznacza nowego gracza: nie twórz pustego profilu do późniejszego nadpisania starych danych. Potwierdzony brak profilu i błąd odczytu są odrębnymi stanami. Błąd zapisu zatrzymuje wypłatę w GRANT_PENDING, nie pozwala farmić kolejnych potwierdzeń. Retries z ograniczeniem i odstępem; po wyczerpaniu bezpieczny komunikat o synchronizacji i brak utraty już zatwierdzonych danych.

Crash przed rozliczeniem: wznowienie zatwierdzonego stanu lub ponowne sprawdzenie tego samego assignment. Crash po rozliczeniu, przed odpowiedzią UI: po powrocie odczytaj grantFlags/sequence i pokaż istniejący wynik, bez kolejnej wypłaty. Server shutdown nie może być jedynym momentem zapisu.

Lease profilu: identyfikator sesji, wersja i jawna polityka wygaśnięcia. Utrata lease kończy prawo starego serwera do mutacji; nie wolno odświeżać lease cudzej sesji. Czas trwania dobrać do budżetów i istniejącego rozwiązania, nie zgadywać bez testu. Stary i nowy system zapisu nie pracują równolegle na tym samym kluczu.

## 7. Pomoc, postęp tymczasowy i rollback

Zapis najwyższego użytego matematycznego wsparcia musi przetrwać reconnect. Nie ujawniaj rozwiązania, a następnie po awarii oznaczaj tę samą próbę jako samodzielną. Potwierdzaj hint dopiero po utrwaleniu znacznika albo przy wznowieniu niepewnej sesji konserwatywnie ustaw assisted dla tej próby; podstawowej nagrody to nie zmienia.

Stan układania można buforować i zapisywać co pewien czas, ale „Zapisano” pokazuj wyłącznie po potwierdzeniu. Przy niespodziewanej awarii możliwy jest powrót do ostatniego checkpointu interakcji, nigdy utrata już zatwierdzonej nagrody. Obietnica pełnego zapisu każdego ruchu wymaga osobnego kosztownego dowodu, nie jest automatycznym skutkiem API.

Każda migracja ma wersję, walidację, próbkę starych danych i rollback. Nie resetować profili produkcyjnych, nie przemianowywać magazynu jako sposobu „naprawy testu”. Testy odbywają się w odrębnym prywatnym miejscu i namespace.

## 8. Prywatność i testy

Wysyłaj mastery tylko właścicielowi. Nie umieszczaj danych edukacyjnych w leaderstats, publicznych Attributes, modelach pokoju, eventach broadcast ani logach dostępnych graczom. Wynik współpracy może mówić „stanowisko gotowe”, nie „uczeń potrzebował trzech podpowiedzi”. Publikowany raport testu używa anonimowych etykiet, nie kont i danych dzieci.

Obowiązkowe przypadki: forged amount; wrong owner; NaN/Inf; ogromny payload; duplikat actionSeq; stare assignment; callback retry; crash przed/po commit; read error; lease mismatch; dwa kliknięcia wyboru; brak wycieku mastery; osobne profile drużyny przy awarii jednego zapisu. Stany wykonania pozostają NOT_RUN do faktycznej próby.
