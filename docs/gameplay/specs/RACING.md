# Kontrakt wyścigów: profile, gadżety, boty i rekordy

2026-10-19. Wiążące Q15–Q20 oraz urządzenia Q27–Q30. [Research Mario Kart](../stage_c/MARIO_KART_RACING_RESEARCH.md) jest źródłem inspiracji, nie kodem do kopiowania. Własne nazwy/model/dźwięk. Wszystkie wartości i nazwy trybów niżej to parametry testowe. **Nie wdrożono żadnego wyścigu.**

## 1. Dwa zbiory zasad i wyniki

CLEAN_TRIAL: porównywalna czysta jazda, bez losowych gadżetów, ataków i catch-up; własny duch opcjonalny. PARTY_RACE: rywale i kontrolowany chaos przedmiotów. Nie mieszaj wyników obu typów. Profil referencyjny dla CLEAN_TRIAL albo oddzielne wyniki per profil to decyzja eksperymentu; nie oznaczaj jej jako wyboru właściciela. Q17 zatwierdza kilka stylów prowadzenia, nie dowolny ukryty upgrade.

Key sportowego wyniku: routeId, routeVersion, mode, handlingProfile, physicsVersion, assistCategory. Historyczny wynik nie konkuruje z nową nieporównywalną fizyką. Key jednorazowej nagrody jest odrębny i stabilny; drobny patch albo zmiana profilu nie odnawia wszystkich monet/medali. Brak globalnej tablicy na start, znajomi opcjonalnie i zgodnie z platformową prywatnością. Brak nagród za samą pozycję w tabeli.

## 2. Profile jazdy

Roboczo3: zwrotny, zrównoważony, szybki na prostych. Dostępne każdemu od początku. Żaden nie jest lepszy we wszystkim; testuj tor kręty, prosty i mieszany. XP, wallet i skórka nie modyfikują osiągów. Profil blokowany na start rundy; zmiana w trakcie unieważnia porównywalność wyniku, nie tworzy exploita przyspieszenia.

Najpierw prosta jazda, zakręt i jawne turbo. Drift z mini-turbo i asysty prowadzenia są propozycjami następnego eksperymentu, nie obowiązkiem kopiowania pełnego Mario Kart. Asysta może poprawiać dostępność, ale jej rodzaj trzeba uwzględnić przy porównywaniu czasów. Niewykryta asysta nie daje kary; domyślne reguły muszą być widoczne przed rundą.

## 3. Dobrowolność i stoper

Matematyka jest przed/po rundzie i nie jest ograniczona czasem. Zwykłą przygodę można ukończyć bez wersji czasowej. SPORT_FINISH: mała pewna nagroda za pierwszą poprawnie ukończoną próbę; SPORT_TIER: jednorazowe brąz/srebro/złoto. Osiągnięcie złota nie wymaga wcześniejszego specjalnie gorszego przejazdu. Czas trasy/okrążenia jest serwerowy, checkpointy muszą potwierdzać legalny porządek. Teleport, pominięty odcinek, cofanie przy linii i ponowne przekroczenie mety nie zwiększają postępu.

Cała stawka NIE musi mieć16 uczestników. TEST_DEFAULT: najpierw2, potem4, potem8pojazdów, z osobnym pomiarem iPada. Liczba8 nie jest wybranym limitem produktu. Miasto nadal ma cel16klientów i nie wolno zastąpić ich botami w teście sieciowym.

## 4. Pierwsza pula przedmiotów, propozycja

Banan: widoczna pułapka, krótka utrata części prędkości i sterowania, bez wyrzucenia poza mapę. Turbo: krótki jawny efekt przyspieszenia. Osłona: blokuje jedno trafienie albo wygasa. Jedna kieszeń, jeden duży przycisk użycia. Piłka/dzwonek z researchu pozostają backlogiem, nie obowiązkową pierwszą implementacją.

Przedmioty istnieją tylko wewnątrz dobrowolnej rundy i działają wyłącznie na jej uczestników. Nie atakują spacerujących dzieci, NPC zadań ani prywatnych stanowisk matematycznych. Nie kupuje się ich za monety czy Robux. Skin efektu nie zwiększa zasięgu. Po zakończeniu/despawnie czyść obiekty i połączenia zdarzeń.

TEST_DEFAULT do prób: turbo1,5s, poślizg0,5s, odporność na ponowne trafienie1,5s, osłona5s albo1trafienie, TTL pułapki15s. To nie wyniki z Mario Kart. Ustaw w jednym wersjonowanym configu, nie rozsypuj po skryptach. Zakaz pułapek przy samym respawnie; jeśli nie można bezpiecznie postawić, przedmiot nie tworzy niewidzialnej kolizji. Wizualny wskaźnik efektu widoczny także na niskiej grafice.

## 5. Doganianie

Miara: zatwierdzony serwerowo postęp po legalnej trasie, nie sama pozycja XYZ ani zgłoszona przez klienta lokata. Wagi przedmiotów zależą od straty względem czołówki, z uwzględnieniem checkpointów i okrążeń. TEST_DEFAULT tabela do symulacji [banan,turbo,osłona] w procentach: czołówka[50,20,30], środek[25,40,35], większa strata[10,50,40]. Każdy wiersz sumuje100. Granice grup straty należy skalibrować do długości konkretnej trasy; nie ustalać jednej liczby metrów dla całego miasta.

Nie zmieniać po cichu maksymalnej prędkości, przyczepności czy czasu rywala. Lider nie dostaje obowiązkowego trafienia. RNG na serwerze; rezultat zapisany dla jednego zdarzenia skrzynki, retransmisja nie losuje ponownie. Nowy przedmiot tylko po rzeczywistym postępie do kolejnej legalnej okazji. Cofanie i czekanie przy jednej skrzynce nie odnawia losowania. Nie obiecujemy pełnej eliminacji sandbaggingu; mierzymy opłacalność celowego zwalniania i stroimy tabelę. Poziom przygody, klasa i błędy matematyczne nigdy nie są wejściem RNG.

## 6. Boty

Każdy bot ma widoczne oznaczenie. Jazda tym samym modelem i w legalnych granicach; trudność przez planowanie/reakcję/tor jazdy, nie tajną prędkość i teleporty. Bot używa przedmiotów na takich samych regułach, nie zna niewidocznej prywatnej przyszłości losowania. Jeśli utknie: jawny reset do ostatniego bezpiecznego checkpointu za nim, bez zaliczenia brakującego odcinka. Boty uzupełniają stawkę tylko przed startem, nie materializują się przed metą.

Solo+boty to aktywność solo, bez sztucznego bonusu współpracy. Rywalizacja kilku ludzi też nie daje co-op tylko za wspólny serwer; premiowana może być wcześniejsza wspólna organizacja zawodów. Odejście przeciwnika nie zamienia się w automatyczny medal bez ukończenia własnej próby.

## 7. Kolejność eksperymentu i odbiór

Czysta jazda i checkpointy → profile → prawdziwi gracze → boty → turbo → osłona → banan → catch-up. Każdy krok osobny test. Nie rób w jednym PR fizyki, siedmiu tras, gadżetów i ekonomii.

Dowody: legalny skrót vs pominiętycheckpoint, odwrócenie jazdy, teleport, podwójna meta, rozłączenie, przecinające się pociski, kilka trafień, niskiLOD, puste pole poza trasą, spawnkill,10kolejnych przejazdów bez wycieku instancji, próba zmian clientside. Dla trzech profili porównaj wyniki na trzech charakterach tras. Wyniki czasowe i opinie graczy muszą być rzeczywiste; same równe sumy parametrów nie są dowodem balansu.
