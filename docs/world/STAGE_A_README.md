# ETAP A — Atlas Siedlec, przyrody i sportu MathCity

**Wersja: A-2026-10-18-R1. Wynik desk researchu: WYKONANO. Wynik całego Etapu A: PARTIAL / WAITING_FOR_PHOTOS_AND_LOCAL_VALIDATION.**

### Cel

Zebrać rozpoznawalne miejsca Siedlec i okolic, nie kopiując miasta 1:1. Udokumentować źródła oraz konkretne kadry fotograficzne, przygotować pomysły matematycznych minigier, z góry zaznaczyć niepewności i obszary szczególnej ochrony. Materiały przeznaczone także do delegowania pracy prostszemu LLM, który ma wykonywać polecenia **bez zgadywania**.

## Stan liczbowy

- **41** rekordów miejsc i atrakcji powiązanych z miejskimi i regionalnymi źródłami, w tym **10 priorytetu A**, **23 B**, **8 C**.
- **41** kart operacyjnych (architektura/transport 19, przyroda 12, sport 10).
- **40** opisanych przykładów minigier z krokami, przykładowymi wynikami i wymaganym feedbackiem.
- **41** wpisów shot list z URL do stron/fotogalerii. **Zero** cudzych zdjęć pobranych do repo.
- **7** proponowanych stref/dzielnic (w tym nowa strefa leśna Sekuła, wyodrębniona z sześciu wcześniej szkicowanych). **Niezatwierdzone** jako układ świata.
- **Brak** potwierdzenia dokładnej Górki Grześ, przebiegu pętli narciarskich, licencji fotografii i adresu konkretnego wejścia do parku wodnego.

## Wejście dla wykonawcy

**Najpierw przeczytaj [instrukcję dla słabszego LLM](atlas/WEAK_LLM_RUNBOOK.md), a następnie dokument właściwej lokacji.** Nie tworzymy assetów i nie edytujemy gry.

| Pytanie | Plik |
| --- | --- |
| Jakie miejsca zbadano? | [Pełny katalog 41 ID](atlas/LANDMARK_CATALOG.md) |
| Jak zbudować Ratusz, Pałac, Dworzec (kiedy ruszy produkcja)? | [19 kart miasta](atlas/CITY_CARDS.md) |
| **ZALEW MUCHAWKA: osobny hub, 10 referencji, 12 minigier** | **[Pełna specyfikacja N01](atlas/MUCHAWKA_FEATURE.md)** |
| Jak potraktować Las Sekuła, biegówki, Grześ, Muchawkę? | [12 kart natury](atlas/NATURE_CARDS.md) |
| Stadion / basen / narciarstwo / skate / parkour? | [10 kart sportu](atlas/SPORT_CARDS.md) |
| Które strony mają fotografie i jakich kadrów brakuje? | [Rejestr 41 shot listów](atlas/PHOTO_REFERENCES.md) |
| Co dziecko ma robić, jakie odpowiedzi i błędy? | [32 minigry (hipotezy)](atlas/MECHANICS_MATRIX.md) |
| Które fakty i konflikty rozstrzygnięto? | [Evidence i bibliografia Stage A](atlas/SOURCE_EVIDENCE.md) |
| Gdzie absolutnie nie projektować wyścigów? | [Strefy szacunku i ochrony](atlas/CONSERVATION_AND_RESPECT.md) |
| Jak pokazać zasięg 7 stref na konceptach? | [Masterplan](DISTRICTS_MASTERPLAN.md) i [schemat 7 stref](../art/MATHCITY_WORLD_SCHEMATIC.svg) |

## Zalew Muchawka — ATRAKCJA FLAGOWA N01

**Wymóg właściciela:** Muchawka ma być wyeksponowana równie wyraźnie jak ratusz i Sekuła. Prawdziwy akwen, piaszczysta plaża, pomost, spacery, rowery i infrastruktura sportowa są podstawą dla sześciu **fikcyjnych** podstref MathCity. Podstawowe źródła: [kąpielisko](https://turystyka.siedlce.pl/267-siedlce-kapielisko-nad-zalewem-muchawka), [GIS](https://sk.gis.gov.pl/index.php/kapielisko/326) i [triathlon 2026](https://siedlce.pl/wydarzenia/2026/06-2026/triathlon-siedlecki-2026). **Karta wykonawcza dla agenta:** [MUCHAWKA_FEATURE.md](atlas/MUCHAWKA_FEATURE.md). Minigry: `M24–M27` i `M33–M40`, łącznie 12 powiązanych pomysłów, z G2–G4 jako propozycjami. **N01 (Zalew) ≠ S02 (Park Wodny)**; Dolina Muchawki N03 to obszar przyrodniczy. Zdjęcia i mapa stref nadal OPEN.

## Najważniejsze miejscówki właściciela

### Las Sekuła — obowiązkowy hub sportowy i edukacyjny (N04/N05/N06)

- Uroczysko leśne w Siedlcach: N04.
- **Biegówki przy Domanickiej 71**: N05, zimą. Nie mylić z trasami narciarstwa zjazdowego.
- **Ścieżka edukacyjna**: N06, Nadleśnictwo podaje **2,1km** pętli, portal turystyczny **8 przystanków**.
- Latem gra może użyć autorskiej pętli leśnych biegów i rowerów; faktyczne wydarzenia rowerowe w okolicy trzeba opisać oddzielnie.
- **Ważne**: istnieją miejsca pochówku i pamięci; tam nie ma minigier. Dokładne strefy sportowe i granice wymagają potwierdzenia.

### Stadion i sport — wiele odrębnych obiektów

- **S01:** Stadion ARMS **piłkarski**, ul. Jana Pawła II 6, **105×68m**, **2901 miejsc**.
- **S02:** Park Wodny, **8 torów, basen 25×21m, zjeżdżalnie 48 i 78m**, strefa rekreacyjna.
- **S03:** Stadion **lekkoatletyczny**, ul. B. Prusa 6 — **inny obiekt**.
- **S04, S05, S06:** skateplaza, parkour park, lodowisko i rolkowisko (Prusa 6).
- **S10:** kręgielnia wewnątrz kompleksu Parku Wodnego, nie dodatkowy basen.
- To potencjał na „Sportowe MathCity”, a nie jedna mini-gra piłkarska.

### Górka Grześ — zachowujemy lokalną nazwę, ale bez zgadywania

- Użytkownik wskazał rzeczywistą, lokalnie znaną Górkę Grześ.
- Wtórne opisy tras w regionie wskazują punkt „Grześ” przy Rakowcu, **ale zebrane informacje nie wystarczają do utożsamienia go z miejscem użytkownika**.
- Nie mylić z **Gryczną Górką** (N10, koło Stoku Lackiego).
- Do dalszych prac potrzebny **pin lub zdjęcie**. Wirtualne saneczki, zagadki wysokości i podchody pozostają propozycjami fantasy, NIE opisem istniejącego stoku.

## Kolejne prace potrzebne do prawdziwego PASS

| ID | Co trzeba zdobyć | Kryterium |
| --- | --- | --- |
| A-F01 | Ratusz Jacek, Pałac Ogińskich, Park Aleksandria | min. 3 ujęcia z prawami, każdy obiekt |
| A-F02 | Muchawka / grobla | min. 3 ujęcia z dozwolonej przestrzeni |
| A-F03 | Stadion piłkarski i basen | min. 3 ujęcia z legalnego źródła, 2 różne części kompleksu |
| A-F04 | Sekuła i trasy biegowe | wejście, zima, lato, znak trasy i potwierdzony przebieg |
| A-F05 | Ścieżka N06 | potwierdzone rozmieszczenie 8 stanowisk i wersja długości |
| A-F06 | Górka Grześ | potwierdzony pin/nazwa/foto od mieszkańca |
| A-F07 | Strefy pamięci na Sekule | udokumentowane wyłączenia z gameplayu |
| A-F08 | Prawa obrazów i zdjęć | licencje/zgody/autorzy, bez dorozumianego reuse |
| A-F09 | Odbiór lokalny | feedback mieszkańca dla sylwetek najważniejszych miejsc |
| A-F10 | Zatwierdzenie projektu | decyzja właściciela co do listy A i podziału na 7 stref |

**W tym commicie nie dodajemy fotografii, gotowych modeli, tekstur ani zmian w mapie Roblox.** Zebraliśmy źródła i plany referencyjne. To etap dokumentacyjny.

## Kontrola jakości

Agent sprawdza: (a) czy 41 ID się zgadza; (b) czy N05 ≠ N06, N07 ≠ N10 i S01 ≠ S03; (c) czy zdjęcia są tylko linkami; (d) czy opis działań dla dzieci nie sugeruje oficjalnej podstawy MEN bez sprawdzenia; (e) czy nie modyfikowano `MathCity.rbxl`, `src/` i `assets/`; (f) czy dokumentacja pozostaje logicznie powiązana linkami; (g) czy status **PARTIAL** nie został bezpodstawnie zastąpiony PASS.
