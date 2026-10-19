# Drużyny 1–4, osobiste historie i wspólne miasto

2026-10-19. Q01,Q05,Q08,Q21,Q30–Q33. Kontrakt projektu, CODE_NOT_STARTED.

## Obiekty i granice

`CitySession` ma cel16 prawdziwych klientów. `Party` ma1–4 członków i leader wyłącznie organizacyjnego; leader nie ma prawa czytać cudzej edukacji ani modyfikować nagród. `AdventureRun` ma wersję historii, etapy i skład do danego etapu. `PersonalProgress` jest zbiorem własnych completion, nie tylko największym numerem ukończonego etapu. `TaskAssignment` to prywatna matematyczna porcja pracy. `WorldEvent` jest współdzieloną, czasową atrakcją.

Nie używaj jednego globalnego `CurrentStage` dla wszystkich dzieci. Wspólne modele wizualne nie mogą zależeć od prywatnego expectedAnswer. Zadania jednej drużyny nie przenoszą blokad kolizji na innych spacerowiczów.

## Tworzenie i szukanie ekipy

Paszport oferuje Solo/Zaproś znajomych/Znajdź ekipę. Publikowana oferta: adventureId, tytuł, etap dołączenia, liczba wolnych miejsc i jawny status otwartości. Nie pokazuj klasy, bandu, liczby błędów czy mastery. Na początek szukanie wyłącznie na tym samym serwerze. Zaproszenie ma odbiorcę, termin technicznego wygaśnięcia i potwierdzenie; nie teleportuje automatycznie ani nie ujawnia prywatnego pokoju.

Czwarty slot rezerwuj na serwerze atomowo; przy dwóch zgłoszeniach naraz tylko jedno może dołączyć. Odrzucenie daje informację o pełnym składzie i zachowuje możliwość solo. Nie wprowadzaj kolejki blokującej całe miasto. Lista zaproszeń ograniczona, ignorowanie/blokowanie powtarzających się zaproszeń możliwe. Interakcje to gotowe etykiety celu, nie ukryty system czatu omijający zasady Roblox.

## Granice etapów

`LOBBY → STAGE_ACTIVE → STAGE_COMMITTING → STAGE_BOUNDARY → NEXT_STAGE/FINISHED`. Rezerwacja nowej osoby może istnieć przy ACTIVE, ale dołączenie do pracy dopiero przy BOUNDARY. Przed kolejnym etapem: podsumowanie dotychczasowej historii, wybór własnej roli, prywatne zadanie dopasowane per skill. Brak wejścia w środek aktywnego wyścigu lub czyjejś planszy. Samo czekanie nie daje EXP.

Dla każdego etapu zapisz `participantsAtStart`, `roleAssignments`, `verifiedContributions`, `acceptedCompletions`. To nie muszą być nazwy istniejących klas Luau; są kontraktem danych.

## Własny wkład i podział pracy

Minimalny etap dla1osoby ma sensowną samodzielną wersję. Przy2–4 osobach dołóż równoległe porcje o porównywalnym wysiłku, a nie cztery elementy pilnowane przez najszybszego. Każdy może korzystać z guided, bez obniżenia podstawy. Nie ma zegara odpowiedzi. Gdy jedna osoba ukończy wcześniej, może dekorować gotowy fragment lub podejrzeć kolejne miejsca, ale nie odpowiada za partnera.

Wspólna scena ma stan dostępny wszystkim, prywatne wersje obiektów renderowane na indywidualnych stanowiskach. Ostateczne skompletowanie atrakcji może liczyć porcje, nie wymagać ujawniania liczb z czyjegoś ćwiczenia. Niewykonana porcja po odejściu przechodzi do wolnej puli albo zostaje usunięta, jeżeli minimum pełnego etapu jest zachowane. Już ukończone porcje nie znikają.

## Odejście, rozłączenie i zmiana lidera

Rozłączenie zapisuje własne już potwierdzone completion i stan bieżącego zadania. W toku zapisu stosuj pojedynczą kolejkę profilu. Pozostałym proponuj kontynuację mniejszym składem; nie zmuszaj do restartu i nie czekaj bez końca. Leader przekazywany deterministycznie najwcześniej dołączonemu pozostającemu graczowi; nie zmienia to jego uprawnień do danych.

TEST_DEFAULT: krótkie okno technicznego powrotu 60s może rezerwować slot, ale pozostali mogą wybrać „kontynuuj bez rezerwacji”. To wartość do testu, nie kara/czas na rozwiązanie. Powracający podczas ACTIVE odzyskuje tylko bezpiecznie zawieszone własne zadanie, jeżeli rola i instancja wciąż aktualne; w przeciwnym razie czeka do BOUNDARY. Gdy cały serwer przestał istnieć, wznawia osobiste completion w nowej instancji, nie przywraca cudzych niezatwierdzonych odpowiedzi.

## Późne wejście i rzadki błąd progresu

Przykład: A ukończył etapy1,2; B dołączył na3. Po wykonaniu3 zapis A={1,2,3}, B={3}. B nie dostaje nagród za1,2, a zakładka wskazuje możliwość ich nadrobienia. Nie zapisuj u B `highestStage=3` jako zamiennika całej historii. Nagroda rozdziału wymagająca{1,2,3} pojawia się u B dopiero po uzupełnieniu1,2. Może grać fragment z ekipą mimo brakującego osobistego wstępu; nie blokuje go EXP, ale nie udajemy kompletnego rozdziału.

Istotny dialog/wstęp można krótko streścić nowemu członkowi. Przyszły projekt głównej fabuły nie może naruszyć tych reguł bez ponownej decyzji.

## Nagrody i świat

Każdy osobno otrzymuje należny grant po zapisie własnego wkładu. Brak transakcji „wszyscy albo nikt” dla czterech profili: awaria jednego zapisu nie odbiera trzem pozostałym wyników, a oczekujący widzi stan synchronizacji. Nie wypłacaj wspólnej nagrody cztery razy jednemu graczowi. Bonusy co-op według [PROGRESSION](PROGRESSION_AND_REWARDS.md).

Wspólny festyn może czasowo rozświetlić plac lub uruchomić animację. Podstawowe atrakcje i osobiste historie nadal dostępne; nie utrwalaj miasta w stanie „wszystko już naprawiono”. Czasowe wydarzenia można ponowić bez presji codzienności i bez resetowania osobistych pamiątek. Rozliczenie udziału wydarzenia używa stabilnego eventInstance+roleReceipt, a nie obecności w pobliżu nagrody.

## Scenariusze odbioru

Solo;2/3/4 różne klasy;5.zgłoszenie;dwa zgłoszenia na ostatni slot;pełna grupa bez czatu;wejście wACTIVE vsBOUNDARY;odejście przed/po verifiedContribution;odejście lidera;wszyscy wychodzą;reconnect na nowym serwerze;B={3} bez fikcyjnych{1,2};błąd zapisu jednej osoby;personel w pokoju;wyciek mastery. Dokładne identyfikatory w [ACCEPTANCE_MATRIX](../../planning/ACCEPTANCE_MATRIX.md).
