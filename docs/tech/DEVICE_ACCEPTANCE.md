# Urządzenia obowiązkowe i warunki odbioru pierwszej wersji

2026-10-19. Q27–Q30. Urządzenia podał właściciel; wersje systemów, warianty pamięci i wydajność nie zostały zmierzone. **Wszystkie testy sprzętowe: NOT_RUN.** Dokumentacja nie oznacza zdalnego dostępu do fizycznego iPada ani telefonów.

## Zestaw docelowy

| ID | Urządzenie | Wymagane dane preflight | Cel projektowy |
|---|---|---|---|
| DEV-IP6 | iPad 6. generacji | dokładny model, iPadOS, wersja klienta Roblox, wolne miejsce | obowiązkowe pełne podstawowe funkcje, stabilne30 FPS |
| DEV-G54 | Motorola G54 | wariant RAM, Android, klient, rozdzielczość/skala | pełna rozgrywka, cel30 FPS lub więcej |
| DEV-RN14 | Redmi Note14 4G | wariant RAM, Android, klient, rozdzielczość/skala | pełna rozgrywka, cel30 FPS lub więcej |
| DEV-PC | RTX2070, i5 10.gen.,32GB DDR4 | dokładny CPU, sterownik, OS, rozdzielczość | cel60 FPS przy1080p |

Nie zastępować RTX2070 modelem Super z innego projektu. Nie zakładać wersji OS na podstawie rocznika urządzenia. Pierwsza czynność na sprzęcie: potwierdź, czy aktualny klient Roblox można uruchomić i czy ma wymagane uprawnienia; ewentualny problem zgodności zgłoś jako blocker, nie obniżaj samowolnie wymagania iPada.

## Funkcje, które muszą być takie same

Miasto i podróż; wszystkie pilotowe zadania; pełna pomoc UI; pokój i dekorowanie; paszport i prywatne umiejętności; drużyna i role; wyścig/profil/gadżet. Na słabszym sprzęcie wolno ograniczyć dekoracyjne szczegóły, refleksy, cienie i cząsteczki. Nie wolno usuwać banana, checkpointu, pola zadania, informacji o celu ani kolizji mającej znaczenie dla rozgrywki.

## Procedura pojedynczego pomiaru

Zapisz commit i wersję kontentu, urządzenie/OS, ustawienia grafiki, wariant trasy, liczbę klientów/botów, sieć oraz temperaturę/stan zasilania w dostępnym zakresie. Bez danych osobowych testerów. Uruchom świeżą sesję, zanotuj start do pierwszej interakcji; potem3min rozgrzewki i minimum10min zdefiniowanego scenariusza. Wykonaj co najmniej3 powtórzenia dla krytycznego wariantu. Są to własne parametry testowe, do korekty na podstawie powtarzalności.

Zbieraj medianę FPS, p95 czasu klatki, liczbę dłuższych przycięć, użycie pamięci według dostępnego profilera, czas doładowania obszaru i błędy klienta/serwera. FPS ze średniej nie dowodzi braku przycięć. Zrzut jednej klatki nie dowodzi stabilności.

Próg roboczy: mobile median FPS≥30 i p95 czasu klatki≤40ms; PC median FPS≥60 i p95≤20ms przy1080p. To TEST_DEFAULTS, a cel właściciela to płynna pełna gra. Przy braku danego pomiaru wpisz NOT_MEASURED, nie0. Żadnego wymyślonego budżetu RAM „PASS” bez rzeczywistego narzędzia i urządzenia. Wyniki mieszczące się na granicy muszą przejść dłuższą sesję po rozgrzaniu.

## Macierz scenariuszy

| ID | Scenariusz | Obowiązkowy wynik funkcjonalny |
|---|---|---|
| DEV-01 | Pierwsze wejście i skip/resume tutorialu | pokój/transport działają, UI czytelne |
| DEV-02 | M34 tap/drag, błąd, guided, zapis | wszystkie elementy widoczne, brak wymaganej klawiatury |
| DEV-03 | M01 i M02 | zegar i symetria czytelne bez powiększania |
| DEV-04 | Jazda przez granice sektorów + szybka podróż | brak spadania w niedoładowany świat |
| DEV-05 |4 osoby przy prywatnych zadaniach | role działają, brak wycieku odpowiedzi |
| DEV-06 |16 prawdziwych graczy rozproszonych | stabilna sieć i aktualizacje potrzebnego otoczenia |
| DEV-07 |16 prawdziwych graczy w jednym punkcie | brak ukrycia funkcjonalnych obiektów przy optymalizacji |
| DEV-08 | Wyścig2→4→8 pojazdów, w tym boty | rzeczywiste profile, gadżety, brak pogorszenia czytelności |
| DEV-09 |10 kolejnych wyścigów / wejść w minigrę | brak stale rosnącej liczby instancji i połączeń |
| DEV-10 | Pokój z dekoracjami, goście, powrót do miasta | własność zachowana, niepotrzebne wnętrza zwalniane |
| DEV-11 | Wyciszenie, duże litery, różne rozdzielczości | nadal można skończyć zadanie |
| DEV-12 | Utrata i odzyskanie sieci | bez podwójnej nagrody i fałszywej oceny matematycznej |

DEV-01…DEV-12 wymagają wskazania właściwego sprzętu i liczby klientów. Osiem pojazdów w DEV-08 to zakres eksperymentu, nie zatwierdzony limit wyścigu. Do akceptacji16klientów potrzebne rzeczywiste połączenia;16NPC nie spełnia DEV-06/07.

## Limity symulacji i duży świat

Oficjalny tryb lokalny Studio Server & Clients opisuje testy do8 klientów: [Studio testing modes](https://create.roblox.com/docs/studio/testing-modes). Test16 wymaga odpowiedniej sesji w prywatnym miejscu testowym i prawdziwych klientów; nie opisuj próby8 jako16. [Device simulator](https://create.roblox.com/docs/studio/device-simulator) służy do układu wejścia/ekranu, nie stanowi dowodu FPS fizycznego telefonu.

Masterplan obejmuje wszystkie robocze7 stref. Próby8192 i16384 studów na bok pozostają kandydatami z wcześniejszego researchu; wielkość pustej planszy nie dowodzi wydajności zabudowanego miasta. Zasymuluj docelową gęstość obiektów i ruch. Pierwszy mały fragment M34 bada interakcję, a nie kończy zakres wielkiej mapy.

## Co zrobić po FAIL

Zlokalizuj bottleneck, zmień jeden element, powtórz ten sam scenariusz i porównaj. Nie ukrywaj funkcjonalnych przeszkód i nie obniżaj wymagań bez decyzji. Brak testu iPada lub wariantu16graczy blokuje pełny DEVICE_PASS, ale nie uniemożliwia pracy nad niezależną kartą matematyczną. Celów właściciela nie zmienia LLM na podstawie własnego przypuszczenia o sprzęcie.
