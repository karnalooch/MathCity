# Ranking wzorców do MathCity i mapa istniejących minigier

**Status: rekomendacja projektanta, 2026-10-19. Nie pomiar retencji ani zatwierdzenie zakresu przez właściciela.** Materiał wejściowy: [15 kart gier](BENCHMARK_15_GAMES.md), [źródła](SOURCES_AND_METHOD.md), [M01–M40](../../world/atlas/MECHANICS_MATRIX.md).

## 1. Jak powstał ranking

W pierwszej kolejności oceniono: związek z Siedlcami, matematyczne działanie na obiektach, możliwość zabawy bez czatu, rozsądny rozmiar pierwszego eksperymentu oraz czytelność celu. To ocena jakościowa, nie pozornie precyzyjna punktacja. Bezpieczeństwo jest warunkiem dopuszczenia: wysoki potencjał rozrywkowy nie kompensuje mechaniki krzywdzącej lub niezgodnej z zasadami platformy.

**Koszt niski/średni/wysoki** oznacza względną złożoność małego prototypu, nie wycenę w godzinach. Żaden koszt nie został potwierdzony implementacją. **P0** oznacza kandydat do pierwszego eksperymentu; **P1** do drugiej fali, po wynikach; **P2** później. Przypisanie do P0 nie jest zgodą na kodowanie teraz.

## 2. Ranking adaptacji

| Miejsce | Wzorzec / inspiracja | Propozycja MathCity | Zysk projektowy | Koszt i decyzja |
| --- | --- | --- | --- | --- |
| 1 | Odkrywanie z widocznym katalogiem, G01/G15 | Paszport Siedlec, lokalne wskazówki, osobiste pieczątki | Sens wielkiej mapy i promocja konkretnych miejsc | Niski–średni; P0 |
| 2 | Krótka, samodzielna runda, G13/G09 | Stanowiska minigier przy atrakcjach, natychmiastowy start solo | Wspólny wzorzec interakcji, mało czytania i czekania | Średni; P0 |
| 3 | Zbuduj, sprawdź, popraw, G12 | Tratwa M24 lub pomost M34 na Muchawce | Matematyka staje się czynnością w świecie | Średni przy snap-gridzie; P0 |
| 4 | Wspólne zamówienie, G14/G05 | Poczta, targ i przygotowanie wyprawy | Różne role z jednym czytelnym celem | Średni; P0 |
| 5 | Widoczna przemiana własnego miejsca, G03/G02 | Klomb M03/M23, album i kosmetyka | Trwały rezultat bez utraty po nieobecności | Średni; P0, bez rozbudowanego edytora |
| 6 | Przyjazny ruch i szybka próba, G11/G09 | Sport, biegówki i parkour z checkpointami | Wartość zabawy także między zadaniami | Średni; P1 |
| 7 | Spokojna manipulacja i kolekcjonowanie, G06/G07 | Opcjonalna aktywność nad wodą | Drugi rytm gry, odpoczynek od wyścigów | Średni; P1 po próbie hold/tap |
| 8 | Transport i daleki cel, G01/G08 | Darmowy podstawowy pojazd, widoczne landmarki | Łączy duże strefy bez pustej drogi | Wysoki dla fizycznych pojazdów; najpierw prosty wariant |
| 9 | Ekspresja na regułach, G10/G02 | Kolory, wzory i dekoracje bez oceniania awatara | Wielość poprawnych rozwiązań | Średni; P1, kontrolowana biblioteka |
| 10 | Wyprawa wydarzeniowa, G13 i S02 | Opcjonalna trasa trzech atrakcji | Powrót do różnych części miasta | P2; dopiero przy stabilnych podstawach |

Nie tworzymy na starcie handlu zwierzakami, pełnego tycoona, otwartego edytora domów, rozbudowanego systemu petów i survivalu. Ta decyzja ogranicza **liczbę systemów pierwszego eksperymentu**, nie docelową wielkość miasta.

## 3. Pokrycie istniejącego banku M01–M40

Poniższy podział porządkuje istniejące kandydatury; nie zastępuje ich kart i nie zatwierdza ich zgodności z podstawą. ID są stabilne. Ta sama minigra może należeć do dwóch rodzin, ale nie powinna przez to dostawać dwóch niezależnych implementacji.

| Rodzina interakcji | Istniejące ID | Miejsca | Wzorzec do zbadania |
| --- | --- | --- | --- |
| Odkrycie, licznik i katalog | M05, M27, M32, M38, M40 | Sekuła, Dolina Muchawki, stawy, fantastyczne wyspy | G15 + G01 |
| Czas, sekwencja wydarzeń | M01, M07, M22, M36 | Jacek, Sekuła, dworzec, Muchawka | Lokalna krótka runda G13; jasny cel G09 |
| Układanie, rytm, symetria | M02, M03, M23, M28, M29, M30, M31 | Pałac, park, kultura, fontanny | Widoczny rezultat G03; twórczy wybór G10 |
| Zamówienie i dostawa | M20, M21, M26, M33 | Targ, poczta, trasy rowerowe, plażowy sklep | G14; czytelne role G01 |
| Konstrukcja i części całości | M04, M24, M25, M34 | Mostki Aleksandrii i Muchawka | G12 |
| Sport i pomiary | M06, M07, M08, M09, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M35, M36, M37, M39 | Sekuła, stadion, Park Wodny, rekreacja, Muchawka | G09/G11, ale bez eliminacji i kar za matematykę |

**Szczególna kontrola:** M08/Górka Grześ nadal wymaga potwierdzenia miejsca. M14 i M39 dotyczą zakresu pola figur do audytu dydaktycznego; etap C nie zmienia tego na automatyczną klasę 4. Wymiary basenu i terenu czerpiemy z kart Etapu A, a fikcyjne odcinki gry wyraźnie oznaczamy.

## 4. Świat: duży obszar, gęste punkty zabawy

Mapa dzieli się na trzy skale: bliski obiekt do użycia, krótka trasa między aktywnościami i panorama z dalszym celem. Proponujemy najpierw testować czas przejścia między nimi, nie liczbę dekoracyjnych kilometrów. Otwarcie paszportu ma pokazywać obrys rozpoznawalnego budynku oraz następny kierunek, nie zasypywać dziecka czterdziestoma znacznikami naraz.

Każda z 7 proponowanych stref powinna dostać: rozpoznawalną dominantę, bazową drogę dostępną bez zadań, 2–3 odmienne rodziny działań, punkt odpoczynku i logiczne przejście do sąsiedniej strefy. To wymaganie do późniejszego masterplanu, nie stwierdzenie, że takie strefy już istnieją w Roblox.

## 5. Nie mieszać postępów

**Odkrywanie:** gdzie byłem i co znalazłem. **Matematyka:** co rozumiem i jakiej pomocy użyłem. **Sprawność ruchowa:** jak przejechałem trasę. Te trzy rzeczy mają odrębne znaczenie. Szybki gracz nie powinien automatycznie być uznany za dobrego z matematyki; użycie podpowiedzi nie odbiera pieczątki miejsca. Podstawowe zwiedzanie pozostaje niezależne od klasy szkolnej.

## 6. Pięć odrzuconych antywzorców

| ID | Antywzorzec | Co zastępuje go w MathCity |
| --- | --- | --- |
| A1 | Kradzież i niszczenie cudzej progresji | Osobiste kolekcje i współpraca bez odbierania nagród |
| A2 | Płatne losowanie i kupowanie szczęścia do nauki | Jawna, pewna nagroda i bezpośredni wybór |
| A3 | Obowiązkowe czekanie, AFK i presja codziennego wejścia | Aktywne zadania, zachowanie rezultatów po przerwie |
| A4 | Śmierć/reset lub zawstydzanie za błąd szkolny | Podpowiedź, przykład, lokalna ponowna próba |
| A5 | Powtórzenia i szybkie klikanie zamiast zrozumienia | Zmiana reprezentacji, spokojne sterowanie, oddzielna ocena wiedzy |

Powiązanie z źródłowymi grami jest analizą cech, a nie ogólną oceną ich użytkowników. Szczegółowe zabezpieczenia: [ECONOMY_SAFETY_AND_SOCIAL.md](ECONOMY_SAFETY_AND_SOCIAL.md).
