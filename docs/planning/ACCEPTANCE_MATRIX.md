# Macierz odbioru: reguły produktu, błędy i dowody

2026-10-19. **Wszystkie przypadki runtime poniżej: NOT_RUN.** Nie zostały wykonane testy Roblox, urządzeń i nauczyciela. Niezależna kontrola rachunków w [TEST_VECTORS](../education/stage_d/TEST_VECTORS.md) ma własny zakres i nie zamyka tej macierzy.

## Jak czytać i zamykać przypadek

QA-Q01…QA-Q33 mają warunek odbioru w [rejestrze właściciela](OWNER_DECISIONS_20261019.md). Dodatkowe przypadki poniżej doprecyzowują ryzyka. Raport testu podaje: ID, SHA, definicje/wersje danych, urządzenie i OS, setup, kroki, wynik rzeczywisty, wynik oczekiwany, dowód, status PASS/FAIL/BLOCKED/NOT_RUN. Brak logu, zrzutu albo pomiaru to nie PASS. Przy danych dzieci używaj anonimowych etykiet, nie publikuj kont.

## Edukacja i UI

| ID | Setup i działanie | Oczekiwany wynik | Pakiet / Q |
|---|---|---|---|
| ED-01 | Dwa profile różnych klas otwierają ten sam punkt | oba mogą grać; zadania prywatnie dopasowane |P01–P05;Q01–02 |
| ED-02 | Sukcesy mnożenia, brak nowych prób zegara | rośnie wyłącznie właściwy skill, nie zegar |P01;Q02,Q26 |
| ED-03 | Błąd → pomoc → reconnect | seed i dane stałe, pomoc zachowana |P02–P03;Q07,Q24 |
| ED-04 | UI_HELP na neutralnym obiekcie | samodzielność pozostaje możliwa |P02;Q22 |
| ED-05 | MATH_HINT/GUIDED → poprawne ukończenie | assisted; pełna podstawa; brak fałszywego mastery |P02–P03;Q07,Q26 |
| ED-06 |10 nietrafionych dropów bez „Sprawdź” |0 błędów matematycznych |P02;Q22,Q27 |
| ED-07 | M13 dwa różne poprawne rozmiary | oba akceptowane, jedna główna nagroda |P09;Q25 |
| ED-08 | Symetria: poprawna liczba, błędne pozycje | niepoprawne rozwiązanie |P09;Q25 |
| ED-09 | Zmiana klasy ręcznie | zachowany postęp; nowe zadania właściwego zakresu |P04;Q02,Q26 |
| ED-10 | Uczeń czyta wolno i robi przerwę | brak timera, kary i spadku oceny za czas |P02;Q15 |
| ED-11 | M33 używa20 modelowych złotych | portfel przygody nie jest obciążany |P04;Q11 |
| ED-12 | Nieprawidłowy generator, n13/g3 | blokada niepoprawnego assignment, znany fallback |P01;Q24 |
| UI-01 | M34 tap–tap bez drag, dźwięku i klawiatury | pełne ukończenie |P02;Q22,Q27 |
| UI-02 | Telefon, duży tekst, joystick/safe area | wszystkie akcje i dane widoczne |P02;Q27 |
| UI-03 | Zaproszenie w trakcie odpowiedzi | nie zasłania/narusza bieżącej próby |P05;Q22,Q33 |
| UI-04 | Wyjście i wznowienie tutorialu | brak powtórnej wypłaty, dostępny pokój/transport |P04;Q23 |

## Postęp, ekonomia i świat

| ID | Setup i działanie | Oczekiwany wynik | Pakiet / Q |
|---|---|---|---|
| ECO-01 | Ta sama rola solo i z aktywnym człowiekiem | premia co-op należna każdemu aktywnemu |P05;Q05 |
| ECO-02 | Senior i początkujący, rosnący/malejący gap | ograniczony catch-up, maleje przy wyrównywaniu |P05;Q06 |
| ECO-03 | Niższa klasa/złe odpowiedzi bez zmiany EXP level | brak dodatkowego catch-up za matematykę |P05;Q06 |
| ECO-04 | Nowy seed starego opanowanego celu | nie odnawia firstGrant |P03;Q12,Q24 |
| ECO-05 | Prawdziwy helper wraca do pierwszego celu kolegi | potwierdzony wkład daje HELP, nie grant za samą obecność |P05;Q12 |
| ECO-06 | Celowo nowe konta, AFK i spam pomocnika | brak wielokrotnego grantu tego samego wkładu; raport pozostałych luk |P05;Q12 |
| ECO-07 | Pierwsze ukończenie sportu od razu na złoto | należne nieodebrane progi bez wymogu gorszego przejazdu |P07;Q16 |
| ECO-08 | Kolejny rekord o0,01s lepszy | rekord zapisany, brak odnawiania nagrody |P07;Q16,Q20 |
| ECO-09 | Niski EXP, ale wymagany etap osobisty ukończony | następna przygoda dostępna |P04;Q21 |
| WORLD-01 | Nowy gracz wchodzi po ukończeniu cudzej historii | nadal może przeżyć własne etapy |P04–P09;Q08 |
| WORLD-02 | Powtórka czasowego wydarzenia | nowa wspólna prezentacja, bez resetu osobistych nagród |P09;Q08 |
| WORLD-03 | Fast travel do poznanego/nieznanego punktu | darmowe tylko do poznanego; bez testu matmy |P04;Q14 |
| WORLD-04 | Teleport podczas aktywnej trasy | jawne przerwanie próby; brak zaliczenia checkpointów |P04/P07;Q14 |
| WORLD-05 | Gość próbuje przestawić/zabrać dekorację | odmowa serwera, stan właściciela bez zmian |P04;Q10 |
| WORLD-06 | Śledzenie nagrody, potem zmiana misji | jeden aktualny cel, brak lasu znaczników |P04;Q13 |

## Drużyna i sieć

| ID | Setup i działanie | Oczekiwany wynik | Pakiet / Q |
|---|---|---|---|
| CO-01 | Uruchom przygodę solo, w2,3 i4 osoby | skalowane role, zawsze możliwy koniec |P05;Q31 |
| CO-02 | Piąty gracz i dwa zgłoszenia na ostatni slot | limit4 zachowany atomowo |P05;Q31–32 |
| CO-03 | Dołączenie wACTIVE vsBOUNDARY | pierwsze oczekuje, drugie przydziela rolę i summary |P05;Q33 |
| CO-04 | B dołącza na3 po A={1,2} | po ukończeniu A={1,2,3},B={3}; bez retro-nagrody |P05;Q33 |
| CO-05 | Partner wychodzi po swoim zatwierdzonym wkładzie | praca nie znika; pozostali kończą bez restartu |P05;Q31 |
| CO-06 | Partner wychodzi przed wykonaniem zadania | brak nagrody za niewykonany wkład; minimalny etap możliwy |P05;Q31 |
| CO-07 | Lider wychodzi | kontrolowane przekazanie organizacji, bez cudzej własności |P05;Q31 |
| CO-08 | Powrót w trakcie etapu lub po restarcie serwera | bezpieczne wznowienie/oczekiwanie, bez zerowania historii |P05;Q33 |
| CO-09 | Oferta grupy przy wyłączonym czacie | dołączenie nadal działa przez gotowe akcje |P05;Q32 |
| CO-10 | Próba wyszukania na innym serwerze | brak niejawnej teleportacji i cross-server party |P05;Q32 |
| DATA-01 |2 identyczne żądania poprawnej odpowiedzi | dokładnie1 grant |P03;Q12 |
| DATA-02 | Retry callbacku podczas UpdateAsync | brak side effects i ponownego zwiększenia salda |P03 |
| DATA-03 | Crash przed commit/po commit przed ACK | wznowienie ostatniego stanu albo istniejący grant bez duplikacji |P03 |
| DATA-04 | Błąd odczytu istniejącego profilu | nie tworzy pustego zamiennika |P03 |
| DATA-05 | Stare sequence/assignment, zły owner, NaN/Inf/duży payload | odmowa bez mutacji profilu |P03 |
| DATA-06 | Jeden członek drużyny ma błąd zapisu | pozostali zachowują granty, on ma własny pending/retry |P05 |
| DATA-07 | Dwa kliknięcia różnych wariantów nagrody | dokładnie1 wybór/zużycie uprawnienia |P04 |
| DATA-08 | Klient czyta dane gracza obok / pokoju / leaderstats | brak prywatnej matematyki w replikacji |P04–P05;Q26 |
| DATA-09 | Utrata lease, stary serwer próbuje zapisać | odmowa starej sesji, brak nadpisania nowszej |P03 |

## Sport i urządzenia

| ID | Setup i działanie | Oczekiwany wynik | Pakiet / Q |
|---|---|---|---|
| RACE-01 | Nowy i stary profil otwierają wybór pojazdu | te same profile osiągów dostępne bez grindu |P08;Q17 |
| RACE-02 | Zmiana skórki/EXP/klasy | brak zmiany osiągów i RNG |P08;Q17–18 |
| RACE-03 | Większa strata legalna na trasie | zmiana wag itemów, nie fizyki/lidera |P08;Q18 |
| RACE-04 | Cofanie/stanie przy tej samej skrzynce | brak nowego losowania bez nowej legalnej okazji |P08;Q18 |
| RACE-05 | Banan wobec osoby spoza rundy | zero efektu na przechodnia/zadanie |P08 |
| RACE-06 | Kilka trafień pod rząd | czytelna czasowa odporność i powrót do sterowania |P08 |
| RACE-07 | Solo+boty lub zwykłe PvP | brak premii za współpracę bez kooperacyjnego etapu |P08;Q19 |
| RACE-08 | Bot zablokowany / ginący poza trasą | jawny powrót do legalnego checkpointu, nie przed metę |P08;Q19 |
| RACE-09 | Wynik TT i gadżety / dwie wersje fizyki | odrębne porównywalne klucze wyników |P07–P08;Q20 |
| RACE-10 | Cała runda wyciszona i niskiLOD | przeszkody/ochrona/checkpointy nadal widoczne |P08;Q27–29 |
| DEVICE-GATE | Macierz DEV-01…DEV-12 | prawdziwe raporty na4 urządzeniach i16klientach |P10;Q28–30 |

DEV-01…DEV-12 są dokładnie zdefiniowane w [DEVICE_ACCEPTANCE](../tech/DEVICE_ACCEPTANCE.md), nie zastępuje ich pojedynczy screenshot z PC. Cele40ms/20ms i rozmiar eksperymentów są parametrami testowymi, nie wynikami.

## Bramka odbioru dokumentacji vs gry

DOC_CHECKED: komplet decyzji, ścieżek, kart, źródeł i poprawnych przykładów. UNIT_PASS: uruchomiony właściwy kod logiczny. STUDIO_PASS: rzeczywiste zachowanie klient/serwer. DEVICE_PASS: wymagany sprzęt i scenariusze. TEACHER_APPROVED: podpisany zakres konkretnej rewizji. OWNER_APPROVED: wybrany zakres/styl. RELEASE_READY wymaga osobno polityk platformy, praw i prywatności.

Brak dostępu do urządzenia oznacza BLOCKED_DEVICE, nie domyślny PASS. Nie należy deklarować całego etapu C jako rozegranego ani etapu B jako zaakceptowanego przez sam fakt dodania tej macierzy.
