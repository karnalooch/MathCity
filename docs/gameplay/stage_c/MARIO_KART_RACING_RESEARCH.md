# MathCity: research wyścigów inspirowanych Mario Kart

**Data sprawdzenia źródeł: 2026-10-19. Status: SOURCE_RESEARCH / DESIGN_PROPOSAL / PLAYTEST_NOT_RUN.**

Rozszerzenie [Etapu C](../STAGE_C_README.md), nie implementacja i nie nowa lista gier Roblox. Punkt wyjścia repo: `1b37f6577a575068a62c1fe5022eb8ea73f04fda`. Przejrzano dokumentację Nintendo dla Mario Kart 8 Deluxe oraz Mario Kart World. Nie grano w te tytuły w ramach tego researchu, nie zmierzono prawdopodobieństw, czasu efektów, FPS ani działania na telefonie. Nie skopiowano modeli, grafik, dźwięków ani kodu Nintendo.

## 1. Granice wynikające z rozmowy z właścicielem

**Już wybrane w rozmowie:** matematyka bez presji czasu; dobrowolne próby sportowe ze stoperem; mała pewna nagroda za pierwsze ukończenie próby oraz jednorazowe nagrody brąz/srebro/złoto; rekord nie odnawia wypłaty przy każdej poprawie. Zwiedzanie i główne przygody są dostępne solo. Współpraca jest premiowana, a niższy poziom przygody może otrzymać ograniczony bonus EXP, niezależny od opanowania matematyki. Podpowiedź nie odbiera podstawowej nagrody. Nowe zadania i autentyczna pomoc są ważniejsze od powtarzania opanowanej wersji.

**Nowe zlecenie:** zbadać Mario Kart, w tym skórki banana i inne przedmioty urozmaicające wyścigi.

**Nadal NIEUSTALONE:** identyczne parametry wszystkich pojazdów kontra różne profile prowadzenia; katalog przedmiotów; liczba uczestników; ostateczny podział trybów; dokładne nagrody sportowe; siła wspomagania graczy z tyłu. Poniżej są propozycje, nie automatyczne decyzje właściciela. Samo zlecenie researchu nie zatwierdza systemu walki w otwartym mieście.

## 2. Co potwierdzają źródła

| Wzorzec | Potwierdzenie i granica wniosku |
| --- | --- |
| Przedmioty o różnych funkcjach | W MK8 Deluxe banan powoduje obrót, Mushroom daje krótki boost, zielona muszla leci prosto, czerwona śledzi pojazd z przodu, a Spiny Shell celuje w lidera. Star łączy przyspieszenie z ochroną; Super Horn oddziałuje na pobliskie pojazdy i przedmioty. S01. |
| Obrona i moment użycia | Przedmiot można zachować. Banan lub muszla trzymane z tyłu mogą osłonić przed nadlatującym atakiem. Slipstream, skróty i dobór prowadzenia są dodatkowymi warstwami umiejętności. S03. |
| Losowanie zależne od sytuacji | Poradnik MK8 Deluxe opisuje większą dostępność mocniejszych przedmiotów dla zawodników z tyłu. To nie jest jednak opublikowana pełna formuła ani tabela procentowa. S02. |
| Czystsza próba czasu | MK8 Deluxe Time Trials to jazda bez rywali z określonym zapasem grzybków na starcie, a nie losowaniem przedmiotów od innych graczy. Dostępne są duchy przejazdów. S02. |
| Asysty | Smart Steering pomaga utrzymać trasę, Auto-Accelerate przejmuje naciskanie gazu. S08. |
| Reguły do wyboru | MK8 Deluxe ma Custom Items: można określić pulę przedmiotów w obsługiwanych trybach. S04. |
| Ograniczanie nadużyć | Aktualizacja MK8 Deluxe 3.0.0 ogranicza mocne przedmioty ze skrzynek zbieranych podczas stania, cofania lub powtarzania tego samego miejsca. Inne poprawki stroją okres odporności po trafieniu. S04. |
| Parametry nie są identyczne | W MK8 Deluxe postać i elementy pojazdu wpływają na osiągi; istnieją kompromisy prędkości, przyspieszenia, ciężaru i prowadzenia. Nie utożsamiać Mario Kart z całkowitą normalizacją sprzętu. S03. |
| Połączony świat i różne zawody | Mario Kart World łączy trasy, oferuje Time Trials, VS, tryby arenowe i eliminacyjny Knockout Tour. Jego istnienie nie oznacza, że MathCity potrzebuje wszystkich tych trybów. S06. |
| Ruch poza zwykłą jazdą | World opisuje start z doładowaniem, drift, bonus po skoku, skok ładowany, jazdę po ścianach i szynach. Cofnięcie pozycji nie cofa postępu rywali. S05. |

**Interpretacja projektowa:** warto połączyć umiejętność prowadzenia, świadome używanie przedmiotów i szansę powrotu do walki po błędzie. Nie należy przenosić wszystkich przedmiotów, stopnia chaosu ani eliminowania słabszych uczestników. To interpretacja, nie dowód przyczyn sukcesu serii.

## 3. Proponowany podział aktywności

### TRYB REKORD: kontrolowana próba sportowa

- Bez ataków innych graczy, losowych skrzynek i bonusu za stratę do lidera.
- Stały profil pojazdu przypisany do próby albo osobna klasyfikacja dla każdego profilu; decyzja po wyborze reguł sprzętu.
- Z góry określone boostery na trasie; ewentualny identyczny zapas turbo dla wszystkich. Nie nazywać tego dosłowną kopią Time Trials Nintendo.
- Duch własnego przejazdu bez kolizji i opcja jego ukrycia.
- Wynik rozdzielony według trasy, wersji trasy, zestawu reguł, profilu i istotnych asyst. Zmiana fizyki nie może bez opisu porównywać nowych wyników do starych.
- Nagrody za pierwszą próbę oraz ustalone progi zgodnie z decyzją właściciela; brak mnożenia wypłat przez zmianę ustawień.

### TRYB FESTYN: dobrowolny wyścig z przedmiotami

- Zawodnicy przed dołączeniem widzą, że wzajemne przeszkadzanie jest częścią tej aktywności.
- Czytelne skrzynki na trasie, startowo jedna aktywna kieszeń na przedmiot, jeden duży przycisk użycia i osobny prosty drift.
- Krótkie efekty, czytelna możliwość obrony i pomoc w nadrabianiu dystansu. Parametry do pomiaru, nie ustalone sekundy.
- Wyróżnienia za ukończenie, lokaty i współpracę oddzielone od rekordów czystej jazdy. Nie przenosić losowego czasu z festynu do brązu/srebra/złota trybu rekordowego.
- Wstępna skala eksperymentu: 2–4 uczestników. Docelowa liczba po próbach, bez kopiowania 24-osobowej stawki Nintendo jako wymagania.
- W przyszłości drużyny i wariant arena/zbieranie znaczników; nie w pierwszym eksperymencie.

**Swobodne miasto pozostaje poza działaniem przedmiotów sportowych.** Samo przejeżdżanie przez sąsiednią alejkę nie oznacza dołączenia do zawodów. Tryb festyn nie jest wymagany do ukończenia głównych przygód. Do wersji solo nie dodajemy automatycznie kosztownej implementacji botów bez osobnej decyzji.

## 4. Autorski zestaw pięciu przedmiotów do zbadania

Nazwy i zachowania są propozycjami MathCity. Własne modele, ikony, animacje, efekty i dźwięki; żadnej deklaracji licencji na zasoby Nintendo.

| Przedmiot roboczy | Działanie | Możliwość odpowiedzi | Priorytet |
| --- | --- | --- | --- |
| Skórka banana lub plama mydlin | Mała widoczna przeszkoda zostawiona za pojazdem; krótkie zachwianie i utrata części prędkości | Ominięcie lub aktywna osłona; bez trwałego unieruchomienia | Pierwsza próba |
| Dopalacz wiatrowy | Krótkie turbo aktywowane w dogodnym momencie | Planowanie użycia na prostej; poprawny tor jazdy nadal istotny | Pierwsza próba |
| Bańka ochronna | Zatrzymuje pojedyncze trafienie lub wygasa po określonym czasie | Przeciwnik może poczekać; brak trwałej nietykalności | Pierwsza próba |
| Piłka-pstryk | Toczy się po ograniczonym torze do przodu, powoduje lekkie potrącenie | Widoczny pocisk, możliwość uniku/osłony | Po ocenie czytelności |
| Dzwonek czyszczący | Usuwa przeszkody i pociski w małym zasięgu; nie odrzuca graczy | Wymaga właściwego momentu | Po pierwszym teście |

Opcja późniejsza: pole wiatru dające krótkie wspólne wsparcie w zawodach zespołowych. Nie dodawać nagrody EXP za samo naciskanie pomocy lub trafianie kolegi.

**Do odłożenia:** automatyczny atak na lidera, odbieranie przedmiotów, odwracanie sterowania, zasłanianie całego ekranu, długie zamrożenie, eliminacja po błędzie, dużo piętrowych efektów. Nie są potrzebne, aby wyścig miał charakter zabawy towarzyskiej.

## 5. Doganianie, uczciwość i brak grindu

Są trzy niezależne osie:

1. **Umiejętność matematyczna** decyduje o zadaniach i podpowiedziach, nie o prędkości pojazdu czy szansie na banana.
2. **Poziom przygody i różnica EXP w drużynie** dotyczą wcześniejszej decyzji o rozwoju konta. Nie dają dodatkowej mocy podczas wyścigu.
3. **Bieżąca sytuacja w konkretnym wyścigu** może wpływać na pomoc dla pozostających z tyłu. Taką regułę trzeba zatwierdzić i przetestować osobno.

Propozycja dla festynu: gracz wyraźnie z tyłu częściej otrzymuje użyteczne turbo lub osłonę, lider częściej narzędzia defensywne. Liczy się rzeczywisty postęp po trasie i strata, nie samo wysokie numerem miejsce w zbitej grupie. Nie ukrywać sztucznego spowalniania lidera ani nie gwarantować nowemu graczowi zwycięstwa. Pula musi działać sensownie również przy dwóch uczestnikach.

Sposób wyliczania straty, wagi losowania i limity pozostają DO_TESTU. Brak dokładnego algorytmu Nintendo w źródłach nie upoważnia do wpisania wymyślonych procentów jako faktu. Podany wariant dla MathCity jest nasz.

Zapobieganie nadużyciom: ponowny odbiór przy tej samej skrzynce wymaga prawidłowego postępu; cofanie i czekanie nie są metodą gromadzenia turbo; teleport nie zalicza wyścigu; odłączanie i zmiana trybu nie odnawiają jednorazowej nagrody. Premiowanie celowego oddawania zwycięstw lub farmienia trafień jest wykluczone z propozycji.

Przedmioty są zasobami wyłącznie bieżącej rundy: darmowe, bez zakupów Robux, bez sprzedaży, bez handlu i bez przenoszenia do ekwipunku po wyścigu. Losowy dobór chwilowego gadżetu nie jest proponowanym systemem płatnego losowania trwałych nagród. Podstawowe przedmioty muszą być dostępne wszystkim w ramach tych samych reguł; przygody mogą dawać warianty wizualne i pamiątki, nie silniejsze ataki.

## 6. Proponowane zabezpieczenia rozgrywki

- Po trafieniu krótka odporność, aby kolejne przeszkody nie tworzyły ciągłego blokowania; nie kumulować czasu utraty kontroli.
- Ograniczenie liczby przeszkód, czasu ich życia i obszaru użycia. Żadnych pułapek przy odrodzeniu, wyjściu z szybkiej podróży ani stanowisku matematycznym.
- Przeszkody działają tylko na aktywnych uczestników tej samej rundy. Po ukończeniu/opuszczeniu nie można atakować ani zostać trafionym.
- W trybie drużynowym proponowane wyłączenie celowego przeszkadzania własnej drużynie; współpraca rozliczana po rzeczywistym wkładzie.
- Asysty bez zawstydzających etykiet. Pamiętać, że asysta zmienia warunki porównywania czasów; nie odbierać za nią podstawowej nagrody ukończenia.
- Drgania kamery, błyski i intensywność efektów ograniczane osobno od logiki trafienia. Wyłączenie efektów nie usuwa potrzebnych ostrzeżeń.
- W przyszłej implementacji wynik, uprawnienie do użycia przedmiotu, trafienie i nagroda wymagają walidacji serwerowej; nie ufać klientowi deklarującemu wygraną.

To wymagania proponowanego testu, nie dowód, że system Roblox został już zbudowany.

## 7. Matematyka a tor: scenariusz Muchawki

Korzystamy z istniejących punktów N01/N12 i powiązanych propozycji M35/M36/M37. Nie zmieniamy automatycznie banku M01–M40 ani nie dodajemy M41+.

**Przygotowanie bez stopera:** dziecko ustawia kolejność trzech oznaczonych fragmentów trasy, odczytuje długości i oblicza sumę; w razie potrzeby otrzymuje pomoc krok po kroku. Dostaje nagrodę edukacyjnej przygody bez obowiązku ścigania się.

**Dobrowolny sport:** później wybiera próbę czasu lub festyn. Podczas jazdy nie pojawia się obowiązkowe działanie matematyczne odblokowujące gadżet. Strata przez przedmiot nie cofa nauki, EXP ani postępu misji.

**Po zawodach:** medal sportowy, pamiątka do pokoju lub kosmetyka. Podstawowy postęp edukacyjny nadal pochodzi z zadań, nie z liczby trafionych przeciwników. Cała trasa i liczby przykładu są fikcją gry, a nie twierdzeniem o prawdziwej długości zalewu.

## 8. Najbliższa decyzja właściciela, przed implementacją

Kontynuacja pytania 17: **jak traktujemy sprzęt w trybie z gadżetami?**

- **A:** jeden profil osiągów w danej konkurencji, indywidualny wygląd.
- **B:** kilka profili odmiennych w prowadzeniu, dostępnych wszystkim bez farmienia: zwrotny, zrównoważony, szybki na prostej. Założenie to kompromisy, nie hierarchia „droższy = lepszy”. Równoważność wymaga testu na trasach, nie wynika z samej sumy pasków statystyk.

Rekomendacja: B jako kierunek, ale pierwszy test na jednej wspólnej konfiguracji, aby ocenić przedmioty bez mieszania problemu z balansem sprzętu. W próbach rekordowych parametry muszą być stałe albo wyniki wyraźnie rozdzielone. Żadnego A ani B jeszcze nie zatwierdzono.

## 9. Minimalny test i warunek akceptacji

Dopiero po zgodzie na implementację: krótka makieta jednej pętli z wariantem zwykłym i rekordowym; 2 klientów, później 4; najpierw turbo, osłona i przeszkoda; pozostałe przedmioty po sprawdzeniu czytelności.

Testy: niedozwolony atak na widza; próba zbierania skrzynki przy cofaniu; serie trafień; koniec rundy i sprzątanie; gracz opuszcza drużynę; wysoka latencja; dotyk i asysty; identyczne nagrody bez podwójnej wypłaty; porównanie rekordów tylko w zgodnych warunkach. Obserwacje dzieci z opiekunem muszą sprawdzić, czy przegrana zachęca do kolejnej próby, czy wywołuje poczucie bezradności. Wszystkie sesje: NOT_RUN.

## Źródła

Odczyt 2026-10-19. Materiały Nintendo, nie wiki ani film z cudzej rozgrywki. Poradniki S02/S03 są publikowane przez Nintendo i podpisane redakcją GameWith; nie są kodem źródłowym silnika.

- **S01:** [Nintendo: MK8 Deluxe, przedmioty](https://www.nintendo.com/ph/switch/aabp/item/index.html).
- **S02:** [Nintendo: Beginner Basics, fundamental techniques](https://www.nintendo.com/jp/ichikara/aabpa/index_en.html).
- **S03:** [Nintendo: Beginner Basics, useful techniques](https://www.nintendo.com/jp/ichikara/aabpa/02_en.html).
- **S04:** [Nintendo Support: aktualizacje MK8 Deluxe](https://en-americas-support.nintendo.com/app/answers/detail/a_id/26098/), przede wszystkim 2.2.0 i 3.0.0.
- **S05:** [Nintendo: Mario Kart World, Items & Techniques](https://www.nintendo.com/en-ca/gaming-systems/switch-2/featured-games/mario-kart-world/items-and-techniques/).
- **S06:** [Nintendo: Mario Kart World, Modes](https://www.nintendo.com/en-ca/gaming-systems/switch-2/featured-games/mario-kart-world/modes/).
- **S07:** [Nintendo Support: aktualizacje Mario Kart World](https://www.nintendo.com/de-de/Support/Nintendo-Switch-2/Spiele-Updates/Das-Aktualisieren-von-Mario-Kart-World--2842542.html). Przykład zmienności wag przedmiotów; nie przenosimy całej tabeli do MathCity.
- **S08:** [Nintendo Support: Smart Steering, sterowanie żyroskopowe i Auto-Accelerate](https://support-jp.nintendo.com/app/answers/detail/a_id/34440).

Żaden wynik źródłowy nie zastępuje testu balansu. Dodanie dokumentu nie zamyka Etapu C i nie potwierdza zmian w mapie, kodzie lub silnikach YACS.
